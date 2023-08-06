from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models import key_store as key_store_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    key_store_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,certificateData",
) -> Dict[str, Any]:
    url = "{}/keystores/{keyStoreId}".format(client.hub_base_url, keyStoreId=key_store_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[key_store_m.KeyStore]:
    if response.status_code == 200:
        response_200 = key_store_m.KeyStore.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[key_store_m.KeyStore]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    key_store_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,certificateData",
) -> Response[key_store_m.KeyStore]:
    kwargs = _get_kwargs(
        key_store_id=key_store_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    key_store_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,certificateData",
) -> Optional[key_store_m.KeyStore]:
    """ """

    return sync_detailed(
        key_store_id=key_store_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    key_store_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,certificateData",
) -> Response[key_store_m.KeyStore]:
    kwargs = _get_kwargs(
        key_store_id=key_store_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    key_store_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,certificateData",
) -> Optional[key_store_m.KeyStore]:
    """ """

    return (
        await asyncio_detailed(
            key_store_id=key_store_id,
            client=client,
            fields=fields,
        )
    ).parsed
