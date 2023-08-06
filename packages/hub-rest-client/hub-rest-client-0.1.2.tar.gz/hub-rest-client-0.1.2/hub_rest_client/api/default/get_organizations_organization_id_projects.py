from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models import projects_page as projects_page_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,key,name,archived,description,creationTime,iconUrl,icon,defaultIcon,myFavorite,global,dashboard",
) -> Dict[str, Any]:
    url = "{}/organizations/{organizationId}/projects".format(client.hub_base_url, organizationId=organization_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[projects_page_m.ProjectsPage]:
    if response.status_code == 200:
        response_200 = projects_page_m.ProjectsPage.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[projects_page_m.ProjectsPage]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    organization_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,key,name,archived,description,creationTime,iconUrl,icon,defaultIcon,myFavorite,global,dashboard",
) -> Response[projects_page_m.ProjectsPage]:
    kwargs = _get_kwargs(
        organization_id=organization_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    organization_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,key,name,archived,description,creationTime,iconUrl,icon,defaultIcon,myFavorite,global,dashboard",
) -> Optional[projects_page_m.ProjectsPage]:
    """ """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    organization_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,key,name,archived,description,creationTime,iconUrl,icon,defaultIcon,myFavorite,global,dashboard",
) -> Response[projects_page_m.ProjectsPage]:
    kwargs = _get_kwargs(
        organization_id=organization_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    organization_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,key,name,archived,description,creationTime,iconUrl,icon,defaultIcon,myFavorite,global,dashboard",
) -> Optional[projects_page_m.ProjectsPage]:
    """ """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            fields=fields,
        )
    ).parsed
