from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models import user_group as user_group_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    settings_id: "str",
    user_group_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Dict[str, Any]:
    url = "{}/settings/{settingsId}/autojoingroups/{userGroupId}".format(
        client.hub_base_url, settingsId=settings_id, userGroupId=user_group_id
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


def _parse_response(*, response: httpx.Response) -> Optional[user_group_m.UserGroup]:
    if response.status_code == 200:
        response_200 = user_group_m.UserGroup.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[user_group_m.UserGroup]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    settings_id: "str",
    user_group_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Response[user_group_m.UserGroup]:
    kwargs = _get_kwargs(
        settings_id=settings_id,
        user_group_id=user_group_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    settings_id: "str",
    user_group_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Optional[user_group_m.UserGroup]:
    """ """

    return sync_detailed(
        settings_id=settings_id,
        user_group_id=user_group_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    settings_id: "str",
    user_group_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Response[user_group_m.UserGroup]:
    kwargs = _get_kwargs(
        settings_id=settings_id,
        user_group_id=user_group_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    settings_id: "str",
    user_group_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Optional[user_group_m.UserGroup]:
    """ """

    return (
        await asyncio_detailed(
            settings_id=settings_id,
            user_group_id=user_group_id,
            client=client,
            fields=fields,
        )
    ).parsed
