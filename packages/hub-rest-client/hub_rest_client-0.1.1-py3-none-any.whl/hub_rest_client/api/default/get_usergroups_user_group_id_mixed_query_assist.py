from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.query_assist import QueryAssist
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_group_id: str,
    *,
    client: Client,
    query: Union[Unset, None, str] = UNSET,
    caret: Union[Unset, None, int] = UNSET,
    fields: Union[Unset, None, str] = "query,caret",
) -> Dict[str, Any]:
    url = "{}/usergroups/{userGroupId}/mixed/queryAssist".format(client.hub_base_url, userGroupId=user_group_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "query": query,
        "caret": caret,
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


def _parse_response(*, response: httpx.Response) -> Optional[List[QueryAssist]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = QueryAssist.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[QueryAssist]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_group_id: str,
    *,
    client: Client,
    query: Union[Unset, None, str] = UNSET,
    caret: Union[Unset, None, int] = UNSET,
    fields: Union[Unset, None, str] = "query,caret",
) -> Response[List[QueryAssist]]:
    kwargs = _get_kwargs(
        user_group_id=user_group_id,
        client=client,
        query=query,
        caret=caret,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_group_id: str,
    *,
    client: Client,
    query: Union[Unset, None, str] = UNSET,
    caret: Union[Unset, None, int] = UNSET,
    fields: Union[Unset, None, str] = "query,caret",
) -> Optional[List[QueryAssist]]:
    """ """

    return sync_detailed(
        user_group_id=user_group_id,
        client=client,
        query=query,
        caret=caret,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    user_group_id: str,
    *,
    client: Client,
    query: Union[Unset, None, str] = UNSET,
    caret: Union[Unset, None, int] = UNSET,
    fields: Union[Unset, None, str] = "query,caret",
) -> Response[List[QueryAssist]]:
    kwargs = _get_kwargs(
        user_group_id=user_group_id,
        client=client,
        query=query,
        caret=caret,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_group_id: str,
    *,
    client: Client,
    query: Union[Unset, None, str] = UNSET,
    caret: Union[Unset, None, int] = UNSET,
    fields: Union[Unset, None, str] = "query,caret",
) -> Optional[List[QueryAssist]]:
    """ """

    return (
        await asyncio_detailed(
            user_group_id=user_group_id,
            client=client,
            query=query,
            caret=caret,
            fields=fields,
        )
    ).parsed
