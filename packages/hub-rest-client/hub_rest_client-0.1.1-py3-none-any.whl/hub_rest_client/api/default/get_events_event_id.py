from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.event import Event
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[
        Unset, None, str
    ] = "id,targetId,targetType,targetPresentation,author,authorPresentation,authorType,type,timestamp,eraseTimestamp",
) -> Dict[str, Any]:
    url = "{}/events/{eventId}".format(client.hub_base_url, eventId=event_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Event]:
    if response.status_code == 200:
        response_200 = Event.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Event]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[
        Unset, None, str
    ] = "id,targetId,targetType,targetPresentation,author,authorPresentation,authorType,type,timestamp,eraseTimestamp",
) -> Response[Event]:
    kwargs = _get_kwargs(
        event_id=event_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    event_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[
        Unset, None, str
    ] = "id,targetId,targetType,targetPresentation,author,authorPresentation,authorType,type,timestamp,eraseTimestamp",
) -> Optional[Event]:
    """ """

    return sync_detailed(
        event_id=event_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[
        Unset, None, str
    ] = "id,targetId,targetType,targetPresentation,author,authorPresentation,authorType,type,timestamp,eraseTimestamp",
) -> Response[Event]:
    kwargs = _get_kwargs(
        event_id=event_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    event_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[
        Unset, None, str
    ] = "id,targetId,targetType,targetPresentation,author,authorPresentation,authorType,type,timestamp,eraseTimestamp",
) -> Optional[Event]:
    """ """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            fields=fields,
        )
    ).parsed
