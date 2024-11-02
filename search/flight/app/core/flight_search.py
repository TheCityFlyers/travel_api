from typing import Dict, List
from ..core.providers.bdfare import BdfareClient
from ..core.providers.flyhub import FlyhubClient
from ..config import Settings

class FlightSearchService:
    def __init__(self, settings: Settings):
        self.bdfare_client = BdfareClient(settings)
        self.flyhub_client = FlyhubClient(settings)

    async def search_flights(self, search_params: Dict) -> List[Dict]:
        """
        Search flights across multiple providers
        """
        results = []
        
        # Search Bdfare
        try:
            bdfare_results = await self.bdfare_client.search_flights(search_params)
            results.extend(bdfare_results.get("Results", []))
        except Exception as e:
            print(f"Bdfare search error: {e}")

        # Search Flyhub
        try:
            flyhub_results = await self.flyhub_client.search_flights(search_params)
            results.extend(flyhub_results.get("Results", []))
        except Exception as e:
            print(f"Flyhub search error: {e}")

        return results
