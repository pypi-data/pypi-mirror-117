from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.credentials import Credentials
from ...models.details import Details
from ...types import UNSET, Response, Unset


def _get_kwargs(
    authmodule_id: str,
    *,
    client: Client,
    json_body: Credentials,
    fields: Union[Unset, None, str] = "id,authModuleName,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Dict[str, Any]:
    url = "{}/authmodules/{authmoduleId}/resolve".format(client.hub_base_url, authmoduleId=authmodule_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Details]:
    if response.status_code == 200:
        response_200 = Details.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Details]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    authmodule_id: str,
    *,
    client: Client,
    json_body: Credentials,
    fields: Union[Unset, None, str] = "id,authModuleName,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Response[Details]:
    kwargs = _get_kwargs(
        authmodule_id=authmodule_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    authmodule_id: str,
    *,
    client: Client,
    json_body: Credentials,
    fields: Union[Unset, None, str] = "id,authModuleName,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Optional[Details]:
    """ """

    return sync_detailed(
        authmodule_id=authmodule_id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    authmodule_id: str,
    *,
    client: Client,
    json_body: Credentials,
    fields: Union[Unset, None, str] = "id,authModuleName,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Response[Details]:
    kwargs = _get_kwargs(
        authmodule_id=authmodule_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    authmodule_id: str,
    *,
    client: Client,
    json_body: Credentials,
    fields: Union[Unset, None, str] = "id,authModuleName,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Optional[Details]:
    """ """

    return (
        await asyncio_detailed(
            authmodule_id=authmodule_id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
