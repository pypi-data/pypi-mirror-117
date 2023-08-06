from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models import user as user_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: "str",
    *,
    client: AuthenticatedClient,
    json_body: user_m.User,
    fields: "Union[Unset, None, str]" = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Dict[str, Any]:
    url = "{}/organizations/{organizationId}/ownUsers".format(client.hub_base_url, organizationId=organization_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[user_m.User]:
    if response.status_code == 200:
        response_200 = user_m.User.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[user_m.User]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    organization_id: "str",
    *,
    client: AuthenticatedClient,
    json_body: user_m.User,
    fields: "Union[Unset, None, str]" = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Response[user_m.User]:
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
    organization_id: "str",
    *,
    client: AuthenticatedClient,
    json_body: user_m.User,
    fields: "Union[Unset, None, str]" = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Optional[user_m.User]:
    """ """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    organization_id: "str",
    *,
    client: AuthenticatedClient,
    json_body: user_m.User,
    fields: "Union[Unset, None, str]" = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Response[user_m.User]:
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
    organization_id: "str",
    *,
    client: AuthenticatedClient,
    json_body: user_m.User,
    fields: "Union[Unset, None, str]" = "login,banned,banReason,banBadge,guest,creationTime,lastAccessTime,eraseTimestamp,requiredTwoFactorAuthentication",
) -> Optional[user_m.User]:
    """ """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
