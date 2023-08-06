from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.update_status import UpdateStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    settings_id: str,
    *,
    client: Client,
    fields: Union[Unset, None, str] = "succeed",
) -> Dict[str, Any]:
    url = "{}/settings/{settingsId}/updateStatus".format(client.hub_base_url, settingsId=settings_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "fields": fields,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[UpdateStatus]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UpdateStatus.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[UpdateStatus]]:
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
    fields: Union[Unset, None, str] = "succeed",
) -> Response[List[UpdateStatus]]:
    kwargs = _get_kwargs(
        settings_id=settings_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    settings_id: str,
    *,
    client: Client,
    fields: Union[Unset, None, str] = "succeed",
) -> Optional[List[UpdateStatus]]:
    """ """

    return sync_detailed(
        settings_id=settings_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    settings_id: str,
    *,
    client: Client,
    fields: Union[Unset, None, str] = "succeed",
) -> Response[List[UpdateStatus]]:
    kwargs = _get_kwargs(
        settings_id=settings_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    settings_id: str,
    *,
    client: Client,
    fields: Union[Unset, None, str] = "succeed",
) -> Optional[List[UpdateStatus]]:
    """ """

    return (
        await asyncio_detailed(
            settings_id=settings_id,
            client=client,
            fields=fields,
        )
    ).parsed
