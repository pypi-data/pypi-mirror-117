from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.role import Role
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_id: str,
    role_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "id,key,name,description",
) -> Dict[str, Any]:
    url = "{}/services/{serviceId}/defaultroles/{roleId}".format(
        client.hub_base_url, serviceId=service_id, roleId=role_id
    )

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


def _parse_response(*, response: httpx.Response) -> Optional[Role]:
    if response.status_code == 200:
        response_200 = Role.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Role]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    service_id: str,
    role_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "id,key,name,description",
) -> Response[Role]:
    kwargs = _get_kwargs(
        service_id=service_id,
        role_id=role_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    service_id: str,
    role_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "id,key,name,description",
) -> Optional[Role]:
    """ """

    return sync_detailed(
        service_id=service_id,
        role_id=role_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    service_id: str,
    role_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "id,key,name,description",
) -> Response[Role]:
    kwargs = _get_kwargs(
        service_id=service_id,
        role_id=role_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    service_id: str,
    role_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "id,key,name,description",
) -> Optional[Role]:
    """ """

    return (
        await asyncio_detailed(
            service_id=service_id,
            role_id=role_id,
            client=client,
            fields=fields,
        )
    ).parsed
