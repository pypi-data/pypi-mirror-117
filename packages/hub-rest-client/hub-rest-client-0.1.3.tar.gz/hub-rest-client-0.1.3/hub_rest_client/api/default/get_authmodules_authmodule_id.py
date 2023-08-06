from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models import authmodule as authmodule_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    authmodule_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,ordinal,accountsSize,disabled",
) -> Dict[str, Any]:
    url = "{}/authmodules/{authmoduleId}".format(client.hub_base_url, authmoduleId=authmodule_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[authmodule_m.Authmodule]:
    if response.status_code == 200:
        response_200 = authmodule_m.Authmodule.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[authmodule_m.Authmodule]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    authmodule_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,ordinal,accountsSize,disabled",
) -> Response[authmodule_m.Authmodule]:
    kwargs = _get_kwargs(
        authmodule_id=authmodule_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    authmodule_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,ordinal,accountsSize,disabled",
) -> Optional[authmodule_m.Authmodule]:
    """ """

    return sync_detailed(
        authmodule_id=authmodule_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    authmodule_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,ordinal,accountsSize,disabled",
) -> Response[authmodule_m.Authmodule]:
    kwargs = _get_kwargs(
        authmodule_id=authmodule_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    authmodule_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,ordinal,accountsSize,disabled",
) -> Optional[authmodule_m.Authmodule]:
    """ """

    return (
        await asyncio_detailed(
            authmodule_id=authmodule_id,
            client=client,
            fields=fields,
        )
    ).parsed
