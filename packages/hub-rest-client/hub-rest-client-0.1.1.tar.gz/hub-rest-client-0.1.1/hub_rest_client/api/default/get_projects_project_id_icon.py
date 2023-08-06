from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    client: Client,
    size: Union[Unset, None, int] = UNSET,
    dpr: Union[Unset, None, float] = UNSET,
    default: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/icon".format(client.hub_base_url, projectId=project_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "size": size,
        "dpr": dpr,
        "default": default,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[File]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[File]:
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
    size: Union[Unset, None, int] = UNSET,
    dpr: Union[Unset, None, float] = UNSET,
    default: Union[Unset, None, bool] = UNSET,
) -> Response[File]:
    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        size=size,
        dpr=dpr,
        default=default,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    project_id: str,
    *,
    client: Client,
    size: Union[Unset, None, int] = UNSET,
    dpr: Union[Unset, None, float] = UNSET,
    default: Union[Unset, None, bool] = UNSET,
) -> Optional[File]:
    """ """

    return sync_detailed(
        project_id=project_id,
        client=client,
        size=size,
        dpr=dpr,
        default=default,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Client,
    size: Union[Unset, None, int] = UNSET,
    dpr: Union[Unset, None, float] = UNSET,
    default: Union[Unset, None, bool] = UNSET,
) -> Response[File]:
    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        size=size,
        dpr=dpr,
        default=default,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_id: str,
    *,
    client: Client,
    size: Union[Unset, None, int] = UNSET,
    dpr: Union[Unset, None, float] = UNSET,
    default: Union[Unset, None, bool] = UNSET,
) -> Optional[File]:
    """ """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            size=size,
            dpr=dpr,
            default=default,
        )
    ).parsed
