from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models import widget as widget_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    widget_id: "str",
    *,
    client: Client,
    json_body: List[str],
    fields: "Union[Unset, None, str]" = "key,version,installedVersion,latestVersion,installedFromRepository,archiveId,manifest,disabled,repositoryUrl,repositoryIconUrl",
) -> Dict[str, Any]:
    url = "{}/widgets/{widgetId}/preview".format(client.hub_base_url, widgetId=widget_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "fields": fields,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[widget_m.Widget]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = widget_m.Widget.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[widget_m.Widget]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    widget_id: "str",
    *,
    client: Client,
    json_body: List[str],
    fields: "Union[Unset, None, str]" = "key,version,installedVersion,latestVersion,installedFromRepository,archiveId,manifest,disabled,repositoryUrl,repositoryIconUrl",
) -> Response[List[widget_m.Widget]]:
    kwargs = _get_kwargs(
        widget_id=widget_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    widget_id: "str",
    *,
    client: Client,
    json_body: List[str],
    fields: "Union[Unset, None, str]" = "key,version,installedVersion,latestVersion,installedFromRepository,archiveId,manifest,disabled,repositoryUrl,repositoryIconUrl",
) -> Optional[List[widget_m.Widget]]:
    """ """

    return sync_detailed(
        widget_id=widget_id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    widget_id: "str",
    *,
    client: Client,
    json_body: List[str],
    fields: "Union[Unset, None, str]" = "key,version,installedVersion,latestVersion,installedFromRepository,archiveId,manifest,disabled,repositoryUrl,repositoryIconUrl",
) -> Response[List[widget_m.Widget]]:
    kwargs = _get_kwargs(
        widget_id=widget_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    widget_id: "str",
    *,
    client: Client,
    json_body: List[str],
    fields: "Union[Unset, None, str]" = "key,version,installedVersion,latestVersion,installedFromRepository,archiveId,manifest,disabled,repositoryUrl,repositoryIconUrl",
) -> Optional[List[widget_m.Widget]]:
    """ """

    return (
        await asyncio_detailed(
            widget_id=widget_id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
