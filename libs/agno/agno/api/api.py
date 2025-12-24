from typing import Dict

from httpx import AsyncClient as HttpxAsyncClient
from httpx import Client as HttpxClient
from httpx import Response

from agno.api.settings import agno_api_settings




# api.py – Offline version for agno-dinesh

class OfflineResponse:
    """Mock Response object."""
    status_code = 200
    def json(self):
        return {}
    def text(self):
        return ""
    def __repr__(self):
        return "<OfflineResponse 200 OK>"


class OfflineClient:
    """Mock sync client."""
    def post(self, *args, **kwargs):
        return OfflineResponse()
    def get(self, *args, **kwargs):
        return OfflineResponse()
    def put(self, *args, **kwargs):
        return OfflineResponse()
    def delete(self, *args, **kwargs):
        return OfflineResponse()
    def close(self):
        pass


class OfflineAsyncClient:
    """Mock async client."""
    async def post(self, *args, **kwargs):
        return OfflineResponse()
    async def get(self, *args, **kwargs):
        return OfflineResponse()
    async def put(self, *args, **kwargs):
        return OfflineResponse()
    async def delete(self, *args, **kwargs):
        return OfflineResponse()
    async def aclose(self):
        pass


class Api:
    """Offline API wrapper."""
    def __init__(self):
        pass

    def Client(self):
        return OfflineClient()

    def AsyncClient(self):
        return OfflineAsyncClient()


api = Api()


def invalid_response(r):
    """Always false in offline mode."""
    return False












# class Api:
#     def __init__(self):
#         self.headers: Dict[str, str] = {
#             "user-agent": f"{agno_api_settings.app_name}/{agno_api_settings.app_version}",
#             "Content-Type": "application/json",
#         }

#     def Client(self) -> HttpxClient:
#         return HttpxClient(
#             base_url=agno_api_settings.api_url,
#             headers=self.headers,
#             timeout=60,
#             http2=True,
#         )

#     def AsyncClient(self) -> HttpxAsyncClient:
#         return HttpxAsyncClient(
#             base_url=agno_api_settings.api_url,
#             headers=self.headers,
#             timeout=60,
#             http2=True,
#         )


# api = Api()


# def invalid_response(r: Response) -> bool:
#     """Returns true if the response is invalid"""

#     if r.status_code >= 400:
#         return True
#     return False
