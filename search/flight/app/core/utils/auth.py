from datetime import datetime, timedelta
from typing import Optional
import asyncio
import httpx
from ...config import settings

class TokenManager:
    def __init__(self):
        self._token: Optional[str] = None
        self._expiry: Optional[datetime] = None
        self._lock = asyncio.Lock()

    @property
    def is_token_valid(self) -> bool:
        if not self._token or not self._expiry:
            return False
        # Add 5 minutes buffer before expiry
        return datetime.now() < (self._expiry - timedelta(minutes=5))

    async def get_valid_token(self) -> str:
        async with self._lock:
            if not self.is_token_valid:
                await self.refresh_token()
            return self._token

    async def refresh_token(self):
        raise NotImplementedError("Subclasses must implement refresh_token")

class FlyhubTokenManager(TokenManager):
    async def refresh_token(self):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.flyhub_production_url}/Authenticate",
                json={
                    "username": settings.flyhub_username,
                    "apikey": settings.flyhub_api_key
                }
            )
            response.raise_for_status()
            data = response.json()
            
            self._token = data["TokenId"]
            # Flyhub tokens typically expire in 24 hours
            self._expiry = datetime.now() + timedelta(hours=24)

class BdFareTokenManager(TokenManager):
    async def refresh_token(self):
        # BdFare uses API key directly, but we'll implement token management
        # in case they change to token-based auth in the future
        self._token = settings.bdfare_api_key
        # Set a long expiry since API key doesn't expire
        self._expiry = datetime.now() + timedelta(days=365)
