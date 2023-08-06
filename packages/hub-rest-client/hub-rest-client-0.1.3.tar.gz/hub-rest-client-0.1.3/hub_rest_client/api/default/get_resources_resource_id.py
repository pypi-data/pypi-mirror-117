from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models import resource as resource_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    resource_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,key,name,homeUrl,type",
) -> Dict[str, Any]:
    url = "{}/resources/{resourceId}".format(client.hub_base_url, resourceId=resource_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[resource_m.Resource]:
    if response.status_code == 200:
        response_200 = resource_m.Resource.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[resource_m.Resource]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    resource_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,key,name,homeUrl,type",
) -> Response[resource_m.Resource]:
    kwargs = _get_kwargs(
        resource_id=resource_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    resource_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,key,name,homeUrl,type",
) -> Optional[resource_m.Resource]:
    """ """

    return sync_detailed(
        resource_id=resource_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    resource_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,key,name,homeUrl,type",
) -> Response[resource_m.Resource]:
    kwargs = _get_kwargs(
        resource_id=resource_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    resource_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,key,name,homeUrl,type",
) -> Optional[resource_m.Resource]:
    """ """

    return (
        await asyncio_detailed(
            resource_id=resource_id,
            client=client,
            fields=fields,
        )
    ).parsed
