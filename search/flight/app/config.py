from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import logging

logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    # Bdfare settings
    bdfare_base_url: str = Field(
        default="https://bdf.centralindia.cloudapp.azure.com/api/enterprise",
        description="Bdfare base URL"
    )
    bdfare_api_key: str = Field(..., description="Bdfare API Key")

    # Flyhub settings  
    flyhub_base_url: str = Field(
        default="https://api.flyhub.com/api/v1",
        description="Flyhub base URL"
    )
    flyhub_api_key: str = Field(..., description="Flyhub API Key")
    flyhub_username: str = Field(..., description="Flyhub Username")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding='utf-8',
        case_sensitive=False
    )

@lru_cache()
def get_settings() -> Settings:
    try:
        settings = Settings()
        logger.info("Settings loaded successfully")
        return settings
    except Exception as e:
        logger.error(f"Error loading settings: {str(e)}")
        raise
