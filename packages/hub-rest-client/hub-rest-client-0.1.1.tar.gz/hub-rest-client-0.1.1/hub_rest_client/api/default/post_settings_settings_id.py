from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.settings import Settings
from ...types import UNSET, Response, Unset


def _get_kwargs(
    settings_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Settings,
    fields: Union[Unset, None, str] = "id",
) -> Dict[str, Any]:
    url = "{}/settings/{settingsId}".format(client.hub_base_url, settingsId=settings_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "fields": fields,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Settings]:
    if response.status_code == 200:
        response_200 = Settings.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Settings]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    settings_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Settings,
    fields: Union[Unset, None, str] = "id",
) -> Response[Settings]:
    kwargs = _get_kwargs(
        settings_id=settings_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    settings_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Settings,
    fields: Union[Unset, None, str] = "id",
) -> Optional[Settings]:
    """ """

    return sync_detailed(
        settings_id=settings_id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    settings_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Settings,
    fields: Union[Unset, None, str] = "id",
) -> Response[Settings]:
    kwargs = _get_kwargs(
        settings_id=settings_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    settings_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Settings,
    fields: Union[Unset, None, str] = "id",
) -> Optional[Settings]:
    """ """

    return (
        await asyncio_detailed(
            settings_id=settings_id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
