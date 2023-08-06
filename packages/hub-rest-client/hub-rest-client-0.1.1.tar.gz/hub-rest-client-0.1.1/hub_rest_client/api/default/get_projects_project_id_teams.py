from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.teams_page import TeamsPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "usersTotal,groupsTotal",
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/teams".format(client.hub_base_url, projectId=project_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[TeamsPage]:
    if response.status_code == 200:
        response_200 = TeamsPage.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[TeamsPage]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "usersTotal,groupsTotal",
) -> Response[TeamsPage]:
    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "usersTotal,groupsTotal",
) -> Optional[TeamsPage]:
    """ """

    return sync_detailed(
        project_id=project_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "usersTotal,groupsTotal",
) -> Response[TeamsPage]:
    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "usersTotal,groupsTotal",
) -> Optional[TeamsPage]:
    """ """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            fields=fields,
        )
    ).parsed
