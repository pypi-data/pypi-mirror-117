from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models import application_password as application_password_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: "str",
    *,
    client: AuthenticatedClient,
    json_body: application_password_m.ApplicationPassword,
    fields: "Union[Unset, None, str]" = "id,name,password,creationTime,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Dict[str, Any]:
    url = "{}/users/{userId}/applicationPasswords".format(client.hub_base_url, userId=user_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[application_password_m.ApplicationPassword]:
    if response.status_code == 200:
        response_200 = application_password_m.ApplicationPassword.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[application_password_m.ApplicationPassword]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: "str",
    *,
    client: AuthenticatedClient,
    json_body: application_password_m.ApplicationPassword,
    fields: "Union[Unset, None, str]" = "id,name,password,creationTime,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Response[application_password_m.ApplicationPassword]:
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
    user_id: "str",
    *,
    client: AuthenticatedClient,
    json_body: application_password_m.ApplicationPassword,
    fields: "Union[Unset, None, str]" = "id,name,password,creationTime,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Optional[application_password_m.ApplicationPassword]:
    """ """

    return sync_detailed(
        user_id=user_id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    user_id: "str",
    *,
    client: AuthenticatedClient,
    json_body: application_password_m.ApplicationPassword,
    fields: "Union[Unset, None, str]" = "id,name,password,creationTime,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Response[application_password_m.ApplicationPassword]:
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
    user_id: "str",
    *,
    client: AuthenticatedClient,
    json_body: application_password_m.ApplicationPassword,
    fields: "Union[Unset, None, str]" = "id,name,password,creationTime,lastAccessTime,lastAccessAddress,lastAccessUserAgent",
) -> Optional[application_password_m.ApplicationPassword]:
    """ """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
