from typing import Dict
import httpx
from ...config import Settings

class FlyhubClient:
    def __init__(self, settings: Settings):
        self.base_url = settings.flyhub_base_url
        self.api_key = settings.flyhub_api_key
        self.username = settings.flyhub_username
        self._token = None

    async def authenticate(self) -> str:
        """Get authentication token"""
        url = f"{self.base_url}/Authenticate"
        payload = {
            "username": self.username,
            "apikey": self.api_key
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            self._token = data["TokenId"]
            return self._token

    async def search_flights(self, search_params: Dict) -> Dict:
        """
        Search flights using Flyhub API
        """
        if not self._token:
            await self.authenticate()

        url = f"{self.base_url}/AirSearch"
        
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self._token}"
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json=search_params,
                headers=headers
            )
            response.raise_for_status()
            return response.json()
