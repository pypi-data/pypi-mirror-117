from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.details import Details
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Details,
    fields: Union[Unset, None, str] = "id,authModuleName,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Dict[str, Any]:
    url = "{}/users/{userId}/userdetails".format(client.hub_base_url, userId=user_id)

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
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Details,
    fields: Union[Unset, None, str] = "id,authModuleName,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Response[Details]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Details,
    fields: Union[Unset, None, str] = "id,authModuleName,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Optional[Details]:
    """ """

    return sync_detailed(
        user_id=user_id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Details,
    fields: Union[Unset, None, str] = "id,authModuleName,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Response[Details]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Details,
    fields: Union[Unset, None, str] = "id,authModuleName,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Optional[Details]:
    """ """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
