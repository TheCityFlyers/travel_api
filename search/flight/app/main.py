from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
import httpx
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define request models based on documentation
class OriginDepRequest(BaseModel):
    date: str
    iatA_LocationCode: str

class DestArrivalRequest(BaseModel):
    iatA_LocationCode: str

class OriginDest(BaseModel):
    origin_dep_request: OriginDepRequest
    dest_arrival_request: DestArrivalRequest

class Passenger(BaseModel):
    pax_id: str
    ptc: str  # ADT, CHD, or INF

class TravelPreferences(BaseModel):
    cabinCode: str
    vendorPref: List[str] = []

class ShoppingCriteria(BaseModel):
    returnUPSellInfo: bool
    travelPreferences: TravelPreferences
    tripType: str  # Oneway, Return, or Multi

class FlightSearchRequest(BaseModel):
    point_of_sale: str
    origin_dest: List[OriginDest]
    pax: List[Passenger]
    shopping_criteria: ShoppingCriteria

app = FastAPI(
    title="Flight Search API",
    description="API for searching flights across multiple providers"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(500)
async def internal_error_handler(request, exc):
    logger.error(f"Internal Server Error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error", "message": str(exc)}
    )

# Changed from /api/v1/search to just /search since we're mounted at /search/flight
@app.post("/search")
async def search_flights(request: FlightSearchRequest):
    try:
        logger.info(f"Received search request: {request.dict()}")
        settings = get_settings()
        
        # Initialize results list
        search_results = []
        
        # Search BDFare
        try:
            async with httpx.AsyncClient() as client:
                bdfare_response = await client.post(
                    f"{settings.bdfare_base_url}/AirShopping",
                    headers={
                        "Authorization": f"Bearer {settings.bdfare_api_key}",
                        "Content-Type": "application/json"
                    },
                    json=request.dict()
                )
                if bdfare_response.status_code == 200:
                    search_results.extend(bdfare_response.json().get("results", []))
                    logger.info("BDFare search completed successfully")
                else:
                    logger.error(f"BDFare search failed: {bdfare_response.text}")
        except Exception as e:
            logger.error(f"Error searching BDFare: {str(e)}")

        # Search Flyhub
        try:
            async with httpx.AsyncClient() as client:
                flyhub_response = await client.post(
                    f"{settings.flyhub_base_url}/AirSearch",
                    headers={
                        "Authorization": f"Bearer {settings.flyhub_api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "username": settings.flyhub_username,
                        **request.dict()
                    }
                )
                if flyhub_response.status_code == 200:
                    search_results.extend(flyhub_response.json().get("results", []))
                    logger.info("Flyhub search completed successfully")
                else:
                    logger.error(f"Flyhub search failed: {flyhub_response.text}")
        except Exception as e:
            logger.error(f"Error searching Flyhub: {str(e)}")

        # Return combined results
        return {
            "status": "success",
            "message": "Flight search completed",
            "results": search_results,
            "providers": {
                "bdfare": len([r for r in search_results if r.get("provider") == "bdfare"]),
                "flyhub": len([r for r in search_results if r.get("provider") == "flyhub"])
            }
        }
        
    except Exception as e:
        logger.error(f"Error in search_flights: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )
