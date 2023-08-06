from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    service_id: str,
    untrusted_redirect_uri_id: str,
    redirect_uri: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/services/{serviceId}/untrustedredirecturis/{untrustedRedirectURIId}/{redirectURI}/reject".format(
        client.hub_base_url,
        serviceId=service_id,
        untrustedRedirectURIId=untrusted_redirect_uri_id,
        redirectURI=redirect_uri,
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    service_id: str,
    untrusted_redirect_uri_id: str,
    redirect_uri: str,
    *,
    client: Client,
) -> Response[Any]:
    kwargs = _get_kwargs(
        service_id=service_id,
        untrusted_redirect_uri_id=untrusted_redirect_uri_id,
        redirect_uri=redirect_uri,
        client=client,
    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    service_id: str,
    untrusted_redirect_uri_id: str,
    redirect_uri: str,
    *,
    client: Client,
) -> Response[Any]:
    kwargs = _get_kwargs(
        service_id=service_id,
        untrusted_redirect_uri_id=untrusted_redirect_uri_id,
        redirect_uri=redirect_uri,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)
