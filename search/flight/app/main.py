from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
from .config import get_settings
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
        logger.info("Settings loaded successfully")
        
        # Log API credentials (partially masked)
        logger.info(f"Using Bdfare API key: {settings.bdfare_api_key[:10]}...")
        logger.info(f"Using Flyhub API key: {settings.flyhub_api_key[:10]}...")
        
        return {
            "message": "Search request received",
            "request": request.dict()
        }
        
    except Exception as e:
        logger.error(f"Error in search_flights: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )
