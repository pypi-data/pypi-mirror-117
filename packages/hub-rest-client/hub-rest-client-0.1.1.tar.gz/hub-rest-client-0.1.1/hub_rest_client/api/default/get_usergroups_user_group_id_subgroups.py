from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.subgroups_page import SubgroupsPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_group_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[
        Unset, None, str
    ] = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Dict[str, Any]:
    url = "{}/usergroups/{userGroupId}/subgroups".format(client.hub_base_url, userGroupId=user_group_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[SubgroupsPage]:
    if response.status_code == 200:
        response_200 = SubgroupsPage.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SubgroupsPage]:
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
    fields: Union[
        Unset, None, str
    ] = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Response[SubgroupsPage]:
    kwargs = _get_kwargs(
        user_group_id=user_group_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_group_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[
        Unset, None, str
    ] = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Optional[SubgroupsPage]:
    """ """

    return sync_detailed(
        user_group_id=user_group_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    user_group_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[
        Unset, None, str
    ] = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Response[SubgroupsPage]:
    kwargs = _get_kwargs(
        user_group_id=user_group_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_group_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[
        Unset, None, str
    ] = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Optional[SubgroupsPage]:
    """ """

    return (
        await asyncio_detailed(
            user_group_id=user_group_id,
            client=client,
            fields=fields,
        )
    ).parsed
