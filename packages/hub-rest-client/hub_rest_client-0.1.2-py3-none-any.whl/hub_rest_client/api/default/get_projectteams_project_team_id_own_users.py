from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models import own_users_page as own_users_page_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_team_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Dict[str, Any]:
    url = "{}/projectteams/{projectTeamId}/ownUsers".format(client.hub_base_url, projectTeamId=project_team_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[own_users_page_m.OwnUsersPage]:
    if response.status_code == 200:
        response_200 = own_users_page_m.OwnUsersPage.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[own_users_page_m.OwnUsersPage]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    project_team_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Response[own_users_page_m.OwnUsersPage]:
    kwargs = _get_kwargs(
        project_team_id=project_team_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    project_team_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Optional[own_users_page_m.OwnUsersPage]:
    """ """

    return sync_detailed(
        project_team_id=project_team_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    project_team_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Response[own_users_page_m.OwnUsersPage]:
    kwargs = _get_kwargs(
        project_team_id=project_team_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_team_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Optional[own_users_page_m.OwnUsersPage]:
    """ """

    return (
        await asyncio_detailed(
            project_team_id=project_team_id,
            client=client,
            fields=fields,
        )
    ).parsed
