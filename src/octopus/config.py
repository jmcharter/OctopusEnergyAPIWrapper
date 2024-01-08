from pydantic import Field
from pydantic_settings import BaseSettings


class APISettings(BaseSettings):
    api_key: str = Field(description="API Key for Octopus Energy")
    base_url: str = Field("https://api.octopus.energy", description="Base URL for Octopus API")
    request_timeout: int = Field(3, description="Seconds to wait before requests timeout")
