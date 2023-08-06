from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.user import User
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
    json_body: User,
    login: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    jabber: Union[Unset, None, str] = UNSET,
    banned: Union[Unset, None, bool] = UNSET,
    ban_badge: Union[Unset, None, str] = UNSET,
    two_factor_authentication: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Dict[str, Any]:
    url = "{}/users/{userId}/merge".format(client.hub_base_url, userId=user_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "login": login,
        "name": name,
        "email": email,
        "jabber": jabber,
        "banned": banned,
        "banBadge": ban_badge,
        "twoFactorAuthentication": two_factor_authentication,
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


def _parse_response(*, response: httpx.Response) -> Optional[List[User]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = User.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[User]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: Client,
    json_body: User,
    login: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    jabber: Union[Unset, None, str] = UNSET,
    banned: Union[Unset, None, bool] = UNSET,
    ban_badge: Union[Unset, None, str] = UNSET,
    two_factor_authentication: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Response[List[User]]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
        login=login,
        name=name,
        email=email,
        jabber=jabber,
        banned=banned,
        ban_badge=ban_badge,
        two_factor_authentication=two_factor_authentication,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: str,
    *,
    client: Client,
    json_body: User,
    login: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    jabber: Union[Unset, None, str] = UNSET,
    banned: Union[Unset, None, bool] = UNSET,
    ban_badge: Union[Unset, None, str] = UNSET,
    two_factor_authentication: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Optional[List[User]]:
    """ """

    return sync_detailed(
        user_id=user_id,
        client=client,
        json_body=json_body,
        login=login,
        name=name,
        email=email,
        jabber=jabber,
        banned=banned,
        ban_badge=ban_badge,
        two_factor_authentication=two_factor_authentication,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Client,
    json_body: User,
    login: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    jabber: Union[Unset, None, str] = UNSET,
    banned: Union[Unset, None, bool] = UNSET,
    ban_badge: Union[Unset, None, str] = UNSET,
    two_factor_authentication: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Response[List[User]]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
        login=login,
        name=name,
        email=email,
        jabber=jabber,
        banned=banned,
        ban_badge=ban_badge,
        two_factor_authentication=two_factor_authentication,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    *,
    client: Client,
    json_body: User,
    login: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    jabber: Union[Unset, None, str] = UNSET,
    banned: Union[Unset, None, bool] = UNSET,
    ban_badge: Union[Unset, None, str] = UNSET,
    two_factor_authentication: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Optional[List[User]]:
    """ """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
            login=login,
            name=name,
            email=email,
            jabber=jabber,
            banned=banned,
            ban_badge=ban_badge,
            two_factor_authentication=two_factor_authentication,
            fields=fields,
        )
    ).parsed
