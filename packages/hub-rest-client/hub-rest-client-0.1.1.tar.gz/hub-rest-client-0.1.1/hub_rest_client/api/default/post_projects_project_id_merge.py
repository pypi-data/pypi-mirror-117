from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.project import Project
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    client: Client,
    json_body: Project,
    key: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    archived: Union[Unset, None, bool] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    organization: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "id,key,name,archived,description,creationTime,iconUrl,icon,defaultIcon,myFavorite,global,dashboard",
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/merge".format(client.hub_base_url, projectId=project_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "key": key,
        "name": name,
        "description": description,
        "archived": archived,
        "owner": owner,
        "organization": organization,
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


def _parse_response(*, response: httpx.Response) -> Optional[List[Project]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Project.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Project]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: Client,
    json_body: Project,
    key: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    archived: Union[Unset, None, bool] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    organization: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "id,key,name,archived,description,creationTime,iconUrl,icon,defaultIcon,myFavorite,global,dashboard",
) -> Response[List[Project]]:
    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
        key=key,
        name=name,
        description=description,
        archived=archived,
        owner=owner,
        organization=organization,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    project_id: str,
    *,
    client: Client,
    json_body: Project,
    key: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    archived: Union[Unset, None, bool] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    organization: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "id,key,name,archived,description,creationTime,iconUrl,icon,defaultIcon,myFavorite,global,dashboard",
) -> Optional[List[Project]]:
    """ """

    return sync_detailed(
        project_id=project_id,
        client=client,
        json_body=json_body,
        key=key,
        name=name,
        description=description,
        archived=archived,
        owner=owner,
        organization=organization,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Client,
    json_body: Project,
    key: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    archived: Union[Unset, None, bool] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    organization: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "id,key,name,archived,description,creationTime,iconUrl,icon,defaultIcon,myFavorite,global,dashboard",
) -> Response[List[Project]]:
    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
        key=key,
        name=name,
        description=description,
        archived=archived,
        owner=owner,
        organization=organization,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_id: str,
    *,
    client: Client,
    json_body: Project,
    key: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    archived: Union[Unset, None, bool] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    organization: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "id,key,name,archived,description,creationTime,iconUrl,icon,defaultIcon,myFavorite,global,dashboard",
) -> Optional[List[Project]]:
    """ """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            json_body=json_body,
            key=key,
            name=name,
            description=description,
            archived=archived,
            owner=owner,
            organization=organization,
            fields=fields,
        )
    ).parsed
