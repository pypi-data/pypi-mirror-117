from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.team import Team
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    team_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "usersTotal,groupsTotal",
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/teams/{teamId}".format(client.hub_base_url, projectId=project_id, teamId=team_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Team]:
    if response.status_code == 200:
        response_200 = Team.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Team]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    project_id: str,
    team_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "usersTotal,groupsTotal",
) -> Response[Team]:
    kwargs = _get_kwargs(
        project_id=project_id,
        team_id=team_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    project_id: str,
    team_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "usersTotal,groupsTotal",
) -> Optional[Team]:
    """ """

    return sync_detailed(
        project_id=project_id,
        team_id=team_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    team_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "usersTotal,groupsTotal",
) -> Response[Team]:
    kwargs = _get_kwargs(
        project_id=project_id,
        team_id=team_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_id: str,
    team_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "usersTotal,groupsTotal",
) -> Optional[Team]:
    """ """

    return (
        await asyncio_detailed(
            project_id=project_id,
            team_id=team_id,
            client=client,
            fields=fields,
        )
    ).parsed
