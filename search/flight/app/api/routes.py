from fastapi import APIRouter, Depends
from ..core.flight_search import FlightSearchService
from ..config import get_settings, Settings
from .schemas.common import FlightSearchRequest

router = APIRouter()

@router.post("/search")
async def search_flights(
    request: FlightSearchRequest,
    settings: Settings = Depends(get_settings)
):
    """
    Search for flights across multiple providers
    """
    search_service = FlightSearchService(settings)
    results = await search_service.search_flights(request.dict())
    return {"results": results}
