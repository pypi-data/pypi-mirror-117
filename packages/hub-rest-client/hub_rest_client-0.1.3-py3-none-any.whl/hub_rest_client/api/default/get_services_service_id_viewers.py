from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models import viewers_page as viewers_page_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name",
) -> Dict[str, Any]:
    url = "{}/services/{serviceId}/viewers".format(client.hub_base_url, serviceId=service_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[viewers_page_m.ViewersPage]:
    if response.status_code == 200:
        response_200 = viewers_page_m.ViewersPage.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[viewers_page_m.ViewersPage]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    service_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name",
) -> Response[viewers_page_m.ViewersPage]:
    kwargs = _get_kwargs(
        service_id=service_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    service_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name",
) -> Optional[viewers_page_m.ViewersPage]:
    """ """

    return sync_detailed(
        service_id=service_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    service_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name",
) -> Response[viewers_page_m.ViewersPage]:
    kwargs = _get_kwargs(
        service_id=service_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    service_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name",
) -> Optional[viewers_page_m.ViewersPage]:
    """ """

    return (
        await asyncio_detailed(
            service_id=service_id,
            client=client,
            fields=fields,
        )
    ).parsed
