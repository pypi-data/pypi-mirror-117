from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.permission import Permission
from ...types import UNSET, Response, Unset


def _get_kwargs(
    permission_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "id,key,name,description,global,entityType,operation",
) -> Dict[str, Any]:
    url = "{}/permissions/{permissionId}".format(client.hub_base_url, permissionId=permission_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Permission]:
    if response.status_code == 200:
        response_200 = Permission.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Permission]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    permission_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "id,key,name,description,global,entityType,operation",
) -> Response[Permission]:
    kwargs = _get_kwargs(
        permission_id=permission_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    permission_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "id,key,name,description,global,entityType,operation",
) -> Optional[Permission]:
    """ """

    return sync_detailed(
        permission_id=permission_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    permission_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "id,key,name,description,global,entityType,operation",
) -> Response[Permission]:
    kwargs = _get_kwargs(
        permission_id=permission_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    permission_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "id,key,name,description,global,entityType,operation",
) -> Optional[Permission]:
    """ """

    return (
        await asyncio_detailed(
            permission_id=permission_id,
            client=client,
            fields=fields,
        )
    ).parsed
