from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.user import User
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: User,
    fields: Union[
        Unset, None, str
    ] = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Dict[str, Any]:
    url = "{}/usergroups/{userGroupId}/users".format(client.hub_base_url, userGroupId=user_group_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[User]:
    if response.status_code == 200:
        response_200 = User.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[User]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: User,
    fields: Union[
        Unset, None, str
    ] = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Response[User]:
    kwargs = _get_kwargs(
        user_group_id=user_group_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: User,
    fields: Union[
        Unset, None, str
    ] = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Optional[User]:
    """ """

    return sync_detailed(
        user_group_id=user_group_id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    user_group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: User,
    fields: Union[
        Unset, None, str
    ] = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Response[User]:
    kwargs = _get_kwargs(
        user_group_id=user_group_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: User,
    fields: Union[
        Unset, None, str
    ] = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Optional[User]:
    """ """

    return (
        await asyncio_detailed(
            user_group_id=user_group_id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
