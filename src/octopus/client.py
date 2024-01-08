from typing import Optional
import httpx

from octopus.config import APISettings


class Client:
    """A client for Octopus Energy API"""

    def __init__(self, api_settings: APISettings):
        self.api_key = api_settings.api_key
        self.base_url = api_settings.base_url
        self.request_timeout = api_settings.request_timeout
        self.client = httpx.AsyncClient(auth=(self.api_key, ""), timeout=self.request_timeout)

    def _close(self):
        self.client.aclose()

    def __enter__(self):
        raise TypeError("Use async context manager")

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._close()

    async def _get(self, endpoint: str, *args, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        response = await self.client.get(url)
        return response

    # def get(self):
    #     await self._get()
