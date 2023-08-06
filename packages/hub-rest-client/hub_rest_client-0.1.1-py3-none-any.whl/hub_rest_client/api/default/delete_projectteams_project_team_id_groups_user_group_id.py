from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_team_id: str,
    user_group_id: str,
    *,
    client: AuthenticatedClient,
    keep_users: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Dict[str, Any]:
    url = "{}/projectteams/{projectTeamId}/groups/{userGroupId}".format(
        client.hub_base_url, projectTeamId=project_team_id, userGroupId=user_group_id
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "keepUsers": keep_users,
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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    project_team_id: str,
    user_group_id: str,
    *,
    client: AuthenticatedClient,
    keep_users: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Response[Any]:
    kwargs = _get_kwargs(
        project_team_id=project_team_id,
        user_group_id=user_group_id,
        client=client,
        keep_users=keep_users,
        fields=fields,
    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    project_team_id: str,
    user_group_id: str,
    *,
    client: AuthenticatedClient,
    keep_users: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Response[Any]:
    kwargs = _get_kwargs(
        project_team_id=project_team_id,
        user_group_id=user_group_id,
        client=client,
        keep_users=keep_users,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)
