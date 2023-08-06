from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models import cached_permission as cached_permission_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    permission_id: "str",
    *,
    client: Client,
    query: "Union[Unset, None, str]" = UNSET,
    principal: "Union[Unset, None, str]" = UNSET,
    fields: "Union[Unset, None, str]" = "global",
) -> Dict[str, Any]:
    url = "{}/permissions/{permissionId}/cache".format(client.hub_base_url, permissionId=permission_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "query": query,
        "principal": principal,
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


def _parse_response(*, response: httpx.Response) -> Optional[List[cached_permission_m.CachedPermission]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = cached_permission_m.CachedPermission.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[cached_permission_m.CachedPermission]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    permission_id: "str",
    *,
    client: Client,
    query: "Union[Unset, None, str]" = UNSET,
    principal: "Union[Unset, None, str]" = UNSET,
    fields: "Union[Unset, None, str]" = "global",
) -> Response[List[cached_permission_m.CachedPermission]]:
    kwargs = _get_kwargs(
        permission_id=permission_id,
        client=client,
        query=query,
        principal=principal,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    permission_id: "str",
    *,
    client: Client,
    query: "Union[Unset, None, str]" = UNSET,
    principal: "Union[Unset, None, str]" = UNSET,
    fields: "Union[Unset, None, str]" = "global",
) -> Optional[List[cached_permission_m.CachedPermission]]:
    """ """

    return sync_detailed(
        permission_id=permission_id,
        client=client,
        query=query,
        principal=principal,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    permission_id: "str",
    *,
    client: Client,
    query: "Union[Unset, None, str]" = UNSET,
    principal: "Union[Unset, None, str]" = UNSET,
    fields: "Union[Unset, None, str]" = "global",
) -> Response[List[cached_permission_m.CachedPermission]]:
    kwargs = _get_kwargs(
        permission_id=permission_id,
        client=client,
        query=query,
        principal=principal,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    permission_id: "str",
    *,
    client: Client,
    query: "Union[Unset, None, str]" = UNSET,
    principal: "Union[Unset, None, str]" = UNSET,
    fields: "Union[Unset, None, str]" = "global",
) -> Optional[List[cached_permission_m.CachedPermission]]:
    """ """

    return (
        await asyncio_detailed(
            permission_id=permission_id,
            client=client,
            query=query,
            principal=principal,
            fields=fields,
        )
    ).parsed
