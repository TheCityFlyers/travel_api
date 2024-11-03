from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .config import get_settings
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
async def search_flights(request_data: dict):
    try:
        # Log the incoming request
        logger.info(f"Received search request: {request_data}")
        
        # Get settings
        settings = get_settings()
        logger.info("Settings loaded successfully")
        
        # Log API credentials (partially masked)
        logger.info(f"Using Bdfare API key: {settings.bdfare_api_key[:10]}...")
        logger.info(f"Using Flyhub API key: {settings.flyhub_api_key[:10]}...")
        
        return {
            "message": "Search request received",
            "request": request_data
        }
        
    except Exception as e:
        logger.error(f"Error in search_flights: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )
