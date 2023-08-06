from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.role import Role
from ...types import UNSET, Response, Unset


def _get_kwargs(
    role_id: str,
    *,
    client: Client,
    json_body: Role,
    key: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, str] = "id,key,name,description",
) -> Dict[str, Any]:
    url = "{}/roles/{roleId}/merge".format(client.hub_base_url, roleId=role_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "key": key,
        "name": name,
        "description": description,
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


def _parse_response(*, response: httpx.Response) -> Optional[List[Role]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Role.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Role]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    role_id: str,
    *,
    client: Client,
    json_body: Role,
    key: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, str] = "id,key,name,description",
) -> Response[List[Role]]:
    kwargs = _get_kwargs(
        role_id=role_id,
        client=client,
        json_body=json_body,
        key=key,
        name=name,
        description=description,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    role_id: str,
    *,
    client: Client,
    json_body: Role,
    key: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, str] = "id,key,name,description",
) -> Optional[List[Role]]:
    """ """

    return sync_detailed(
        role_id=role_id,
        client=client,
        json_body=json_body,
        key=key,
        name=name,
        description=description,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    role_id: str,
    *,
    client: Client,
    json_body: Role,
    key: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, str] = "id,key,name,description",
) -> Response[List[Role]]:
    kwargs = _get_kwargs(
        role_id=role_id,
        client=client,
        json_body=json_body,
        key=key,
        name=name,
        description=description,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    role_id: str,
    *,
    client: Client,
    json_body: Role,
    key: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, str] = "id,key,name,description",
) -> Optional[List[Role]]:
    """ """

    return (
        await asyncio_detailed(
            role_id=role_id,
            client=client,
            json_body=json_body,
            key=key,
            name=name,
            description=description,
            fields=fields,
        )
    ).parsed
