from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models import profile_attribute_prototype as profile_attribute_prototype_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    profile_attribute_prototype_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,type,showOnUserList",
) -> Dict[str, Any]:
    url = "{}/profileattributeprototypes/{profileAttributePrototypeId}".format(
        client.hub_base_url, profileAttributePrototypeId=profile_attribute_prototype_id
    )

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


def _parse_response(*, response: httpx.Response) -> Optional[profile_attribute_prototype_m.ProfileAttributePrototype]:
    if response.status_code == 200:
        response_200 = profile_attribute_prototype_m.ProfileAttributePrototype.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[profile_attribute_prototype_m.ProfileAttributePrototype]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    profile_attribute_prototype_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,type,showOnUserList",
) -> Response[profile_attribute_prototype_m.ProfileAttributePrototype]:
    kwargs = _get_kwargs(
        profile_attribute_prototype_id=profile_attribute_prototype_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    profile_attribute_prototype_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,type,showOnUserList",
) -> Optional[profile_attribute_prototype_m.ProfileAttributePrototype]:
    """ """

    return sync_detailed(
        profile_attribute_prototype_id=profile_attribute_prototype_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    profile_attribute_prototype_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,type,showOnUserList",
) -> Response[profile_attribute_prototype_m.ProfileAttributePrototype]:
    kwargs = _get_kwargs(
        profile_attribute_prototype_id=profile_attribute_prototype_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    profile_attribute_prototype_id: "str",
    *,
    client: AuthenticatedClient,
    fields: "Union[Unset, None, str]" = "id,name,type,showOnUserList",
) -> Optional[profile_attribute_prototype_m.ProfileAttributePrototype]:
    """ """

    return (
        await asyncio_detailed(
            profile_attribute_prototype_id=profile_attribute_prototype_id,
            client=client,
            fields=fields,
        )
    ).parsed
