from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    settings_id: str,
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/settings/{settingsId}/translation".format(client.hub_base_url, settingsId=settings_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "name": name,
        "version": version,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[File]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[File]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    settings_id: str,
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[File]:
    kwargs = _get_kwargs(
        settings_id=settings_id,
        client=client,
        name=name,
        version=version,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    settings_id: str,
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Optional[File]:
    """ """

    return sync_detailed(
        settings_id=settings_id,
        client=client,
        name=name,
        version=version,
    ).parsed


async def asyncio_detailed(
    settings_id: str,
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[File]:
    kwargs = _get_kwargs(
        settings_id=settings_id,
        client=client,
        name=name,
        version=version,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    settings_id: str,
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Optional[File]:
    """ """

    return (
        await asyncio_detailed(
            settings_id=settings_id,
            client=client,
            name=name,
            version=version,
        )
    ).parsed
