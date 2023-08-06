from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.sourced_project_role import SourcedProjectRole
from ...types import Response


def _get_kwargs(
    user_id: str,
    sourced_project_role_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/users/{userId}/sourcedprojectroles/{sourcedProjectRoleId}".format(
        client.hub_base_url, userId=user_id, sourcedProjectRoleId=sourced_project_role_id
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[SourcedProjectRole]:
    if response.status_code == 200:
        response_200 = SourcedProjectRole.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SourcedProjectRole]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: str,
    sourced_project_role_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[SourcedProjectRole]:
    kwargs = _get_kwargs(
        user_id=user_id,
        sourced_project_role_id=sourced_project_role_id,
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: str,
    sourced_project_role_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[SourcedProjectRole]:
    """ """

    return sync_detailed(
        user_id=user_id,
        sourced_project_role_id=sourced_project_role_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    sourced_project_role_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[SourcedProjectRole]:
    kwargs = _get_kwargs(
        user_id=user_id,
        sourced_project_role_id=sourced_project_role_id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    sourced_project_role_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[SourcedProjectRole]:
    """ """

    return (
        await asyncio_detailed(
            user_id=user_id,
            sourced_project_role_id=sourced_project_role_id,
            client=client,
        )
    ).parsed
