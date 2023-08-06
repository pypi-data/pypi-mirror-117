from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.project_team import ProjectTeam
from ...models.user_group import UserGroup
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_team_id: str,
    *,
    client: Client,
    json_body: UserGroup,
    absorb_members: Union[Unset, None, bool] = UNSET,
    fields: Union[Unset, None, str] = "userCount",
) -> Dict[str, Any]:
    url = "{}/projectteams/{projectTeamId}/absorb".format(client.hub_base_url, projectTeamId=project_team_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "absorbMembers": absorb_members,
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


def _parse_response(*, response: httpx.Response) -> Optional[ProjectTeam]:
    if response.status_code == 200:
        response_200 = ProjectTeam.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ProjectTeam]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    project_team_id: str,
    *,
    client: Client,
    json_body: UserGroup,
    absorb_members: Union[Unset, None, bool] = UNSET,
    fields: Union[Unset, None, str] = "userCount",
) -> Response[ProjectTeam]:
    kwargs = _get_kwargs(
        project_team_id=project_team_id,
        client=client,
        json_body=json_body,
        absorb_members=absorb_members,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    project_team_id: str,
    *,
    client: Client,
    json_body: UserGroup,
    absorb_members: Union[Unset, None, bool] = UNSET,
    fields: Union[Unset, None, str] = "userCount",
) -> Optional[ProjectTeam]:
    """ """

    return sync_detailed(
        project_team_id=project_team_id,
        client=client,
        json_body=json_body,
        absorb_members=absorb_members,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    project_team_id: str,
    *,
    client: Client,
    json_body: UserGroup,
    absorb_members: Union[Unset, None, bool] = UNSET,
    fields: Union[Unset, None, str] = "userCount",
) -> Response[ProjectTeam]:
    kwargs = _get_kwargs(
        project_team_id=project_team_id,
        client=client,
        json_body=json_body,
        absorb_members=absorb_members,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_team_id: str,
    *,
    client: Client,
    json_body: UserGroup,
    absorb_members: Union[Unset, None, bool] = UNSET,
    fields: Union[Unset, None, str] = "userCount",
) -> Optional[ProjectTeam]:
    """ """

    return (
        await asyncio_detailed(
            project_team_id=project_team_id,
            client=client,
            json_body=json_body,
            absorb_members=absorb_members,
            fields=fields,
        )
    ).parsed
