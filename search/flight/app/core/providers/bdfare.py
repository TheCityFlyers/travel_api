from typing import Dict
import httpx
from ...config import Settings

class BdfareClient:
    def __init__(self, settings: Settings):
        self.base_url = settings.bdfare_base_url
        self.api_key = settings.bdfare_api_key
        self.username = settings.bdfare_username

    async def search_flights(self, search_params: Dict) -> Dict:
        """
        Search flights using Bdfare API
        """
        url = f"{self.base_url}/AirShopping"
        
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json=search_params,
                headers=headers
            )
            response.raise_for_status()
            return response.json()
