from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.organization import Organization
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Organization,
    fields: Union[
        Unset, None, str
    ] = "id,key,name,description,emailDomain,creationTime,allUsers,projectsCount,iconUrl,icon,defaultIcon",
) -> Dict[str, Any]:
    url = "{}/organizations/{organizationId}".format(client.hub_base_url, organizationId=organization_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Organization]:
    if response.status_code == 200:
        response_200 = Organization.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Organization]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Organization,
    fields: Union[
        Unset, None, str
    ] = "id,key,name,description,emailDomain,creationTime,allUsers,projectsCount,iconUrl,icon,defaultIcon",
) -> Response[Organization]:
    kwargs = _get_kwargs(
        organization_id=organization_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Organization,
    fields: Union[
        Unset, None, str
    ] = "id,key,name,description,emailDomain,creationTime,allUsers,projectsCount,iconUrl,icon,defaultIcon",
) -> Optional[Organization]:
    """ """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Organization,
    fields: Union[
        Unset, None, str
    ] = "id,key,name,description,emailDomain,creationTime,allUsers,projectsCount,iconUrl,icon,defaultIcon",
) -> Response[Organization]:
    kwargs = _get_kwargs(
        organization_id=organization_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Organization,
    fields: Union[
        Unset, None, str
    ] = "id,key,name,description,emailDomain,creationTime,allUsers,projectsCount,iconUrl,icon,defaultIcon",
) -> Optional[Organization]:
    """ """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
