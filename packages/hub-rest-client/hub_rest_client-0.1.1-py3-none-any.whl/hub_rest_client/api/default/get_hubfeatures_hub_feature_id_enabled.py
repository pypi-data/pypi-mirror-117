from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.enabled_features import EnabledFeatures
from ...types import UNSET, Response, Unset


def _get_kwargs(
    hub_feature_id: str,
    *,
    client: Client,
    key: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hubfeatures/{hubFeatureId}/enabled".format(client.hub_base_url, hubFeatureId=hub_feature_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_key: Union[Unset, None, List[str]] = UNSET
    if not isinstance(key, Unset):
        if key is None:
            json_key = None
        else:
            json_key = key

    params: Dict[str, Any] = {
        "key": json_key,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[EnabledFeatures]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EnabledFeatures.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[EnabledFeatures]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    hub_feature_id: str,
    *,
    client: Client,
    key: Union[Unset, None, List[str]] = UNSET,
) -> Response[List[EnabledFeatures]]:
    kwargs = _get_kwargs(
        hub_feature_id=hub_feature_id,
        client=client,
        key=key,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    hub_feature_id: str,
    *,
    client: Client,
    key: Union[Unset, None, List[str]] = UNSET,
) -> Optional[List[EnabledFeatures]]:
    """ """

    return sync_detailed(
        hub_feature_id=hub_feature_id,
        client=client,
        key=key,
    ).parsed


async def asyncio_detailed(
    hub_feature_id: str,
    *,
    client: Client,
    key: Union[Unset, None, List[str]] = UNSET,
) -> Response[List[EnabledFeatures]]:
    kwargs = _get_kwargs(
        hub_feature_id=hub_feature_id,
        client=client,
        key=key,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    hub_feature_id: str,
    *,
    client: Client,
    key: Union[Unset, None, List[str]] = UNSET,
) -> Optional[List[EnabledFeatures]]:
    """ """

    return (
        await asyncio_detailed(
            hub_feature_id=hub_feature_id,
            client=client,
            key=key,
        )
    ).parsed
