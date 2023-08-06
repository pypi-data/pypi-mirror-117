from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models import authmodules_page as authmodules_page_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,ordinal,accountsSize,disabled",
) -> Dict[str, Any]:
    url = "{}/authmodules".format(client.hub_base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[authmodules_page_m.AuthmodulesPage]:
    if response.status_code == 200:
        response_200 = authmodules_page_m.AuthmodulesPage.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[authmodules_page_m.AuthmodulesPage]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,ordinal,accountsSize,disabled",
) -> Response[authmodules_page_m.AuthmodulesPage]:
    kwargs = _get_kwargs(
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,ordinal,accountsSize,disabled",
) -> Optional[authmodules_page_m.AuthmodulesPage]:
    """ """

    return sync_detailed(
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,ordinal,accountsSize,disabled",
) -> Response[authmodules_page_m.AuthmodulesPage]:
    kwargs = _get_kwargs(
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,ordinal,accountsSize,disabled",
) -> Optional[authmodules_page_m.AuthmodulesPage]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
        )
    ).parsed
