from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models import permission as permission_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: permission_m.Permission,
    fields: "Union[Unset, None, str]" = "id,key,name,description,global,entityType,operation",
) -> Dict[str, Any]:
    url = "{}/permissions".format(client.hub_base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[permission_m.Permission]:
    if response.status_code == 200:
        response_200 = permission_m.Permission.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[permission_m.Permission]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: permission_m.Permission,
    fields: "Union[Unset, None, str]" = "id,key,name,description,global,entityType,operation",
) -> Response[permission_m.Permission]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: permission_m.Permission,
    fields: "Union[Unset, None, str]" = "id,key,name,description,global,entityType,operation",
) -> Optional[permission_m.Permission]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: permission_m.Permission,
    fields: "Union[Unset, None, str]" = "id,key,name,description,global,entityType,operation",
) -> Response[permission_m.Permission]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: permission_m.Permission,
    fields: "Union[Unset, None, str]" = "id,key,name,description,global,entityType,operation",
) -> Optional[permission_m.Permission]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
