from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.profile_attribute_prototype import ProfileAttributePrototype
from ...types import UNSET, Response, Unset


def _get_kwargs(
    profile_attribute_prototype_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ProfileAttributePrototype,
    fields: Union[Unset, None, str] = "id,name,type,showOnUserList",
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

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ProfileAttributePrototype]:
    if response.status_code == 200:
        response_200 = ProfileAttributePrototype.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ProfileAttributePrototype]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    profile_attribute_prototype_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ProfileAttributePrototype,
    fields: Union[Unset, None, str] = "id,name,type,showOnUserList",
) -> Response[ProfileAttributePrototype]:
    kwargs = _get_kwargs(
        profile_attribute_prototype_id=profile_attribute_prototype_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    profile_attribute_prototype_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ProfileAttributePrototype,
    fields: Union[Unset, None, str] = "id,name,type,showOnUserList",
) -> Optional[ProfileAttributePrototype]:
    """ """

    return sync_detailed(
        profile_attribute_prototype_id=profile_attribute_prototype_id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    profile_attribute_prototype_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ProfileAttributePrototype,
    fields: Union[Unset, None, str] = "id,name,type,showOnUserList",
) -> Response[ProfileAttributePrototype]:
    kwargs = _get_kwargs(
        profile_attribute_prototype_id=profile_attribute_prototype_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    profile_attribute_prototype_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ProfileAttributePrototype,
    fields: Union[Unset, None, str] = "id,name,type,showOnUserList",
) -> Optional[ProfileAttributePrototype]:
    """ """

    return (
        await asyncio_detailed(
            profile_attribute_prototype_id=profile_attribute_prototype_id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
