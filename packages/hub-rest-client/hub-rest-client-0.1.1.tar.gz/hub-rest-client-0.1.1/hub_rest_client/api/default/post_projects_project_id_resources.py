from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.resource import Resource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Resource,
    fields: Union[Unset, None, str] = "id,key,name,homeUrl,type",
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/resources".format(client.hub_base_url, projectId=project_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
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


def _parse_response(*, response: httpx.Response) -> Optional[Resource]:
    if response.status_code == 200:
        response_200 = Resource.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Resource]:
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
    json_body: Resource,
    fields: Union[Unset, None, str] = "id,key,name,homeUrl,type",
) -> Response[Resource]:
    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Resource,
    fields: Union[Unset, None, str] = "id,key,name,homeUrl,type",
) -> Optional[Resource]:
    """ """

    return sync_detailed(
        project_id=project_id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Resource,
    fields: Union[Unset, None, str] = "id,key,name,homeUrl,type",
) -> Response[Resource]:
    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Resource,
    fields: Union[Unset, None, str] = "id,key,name,homeUrl,type",
) -> Optional[Resource]:
    """ """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
