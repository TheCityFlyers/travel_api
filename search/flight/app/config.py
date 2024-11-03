from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    # Bdfare settings
    bdfare_base_url: str = "https://bdf.centralindia.cloudapp.azure.com/api/enterprise"
    bdfare_api_key: str = Field(..., description="Bdfare API Key")
    #bdfare_username: str = Field(..., description="Bdfare Username")

    # Flyhub settings  
    flyhub_base_url: str = "https://api.flyhub.com/api/v1"
    flyhub_api_key: str = Field(..., description="Flyhub API Key")
    flyhub_username: str = Field(..., description="Flyhub Username")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding='utf-8',
        case_sensitive=False
    )

@lru_cache()
def get_settings() -> Settings:
    return Settings()
