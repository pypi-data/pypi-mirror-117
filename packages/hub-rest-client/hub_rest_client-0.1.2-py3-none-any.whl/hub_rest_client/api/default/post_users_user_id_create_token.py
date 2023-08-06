from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models import invite_token as invite_token_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: "str",
    *,
    client: Client,
    email: "Union[Unset, None, List[str]]" = UNSET,
    group: "Union[Unset, None, str]" = UNSET,
    base_url: "Union[Unset, None, str]" = UNSET,
    redirect_url: "Union[Unset, None, str]" = UNSET,
    fields: "Union[Unset, None, str]" = "token",
) -> Dict[str, Any]:
    url = "{}/users/{userId}/createToken".format(client.hub_base_url, userId=user_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_email: Union[Unset, None, List[str]] = UNSET
    if not isinstance(email, Unset):
        if email is None:
            json_email = None
        else:
            json_email = email

    params: Dict[str, Any] = {
        "email": json_email,
        "group": group,
        "baseUrl": base_url,
        "redirectUrl": redirect_url,
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


def _parse_response(*, response: httpx.Response) -> Optional[List[invite_token_m.InviteToken]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = invite_token_m.InviteToken.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[invite_token_m.InviteToken]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: "str",
    *,
    client: Client,
    email: "Union[Unset, None, List[str]]" = UNSET,
    group: "Union[Unset, None, str]" = UNSET,
    base_url: "Union[Unset, None, str]" = UNSET,
    redirect_url: "Union[Unset, None, str]" = UNSET,
    fields: "Union[Unset, None, str]" = "token",
) -> Response[List[invite_token_m.InviteToken]]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        email=email,
        group=group,
        base_url=base_url,
        redirect_url=redirect_url,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: "str",
    *,
    client: Client,
    email: "Union[Unset, None, List[str]]" = UNSET,
    group: "Union[Unset, None, str]" = UNSET,
    base_url: "Union[Unset, None, str]" = UNSET,
    redirect_url: "Union[Unset, None, str]" = UNSET,
    fields: "Union[Unset, None, str]" = "token",
) -> Optional[List[invite_token_m.InviteToken]]:
    """ """

    return sync_detailed(
        user_id=user_id,
        client=client,
        email=email,
        group=group,
        base_url=base_url,
        redirect_url=redirect_url,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    user_id: "str",
    *,
    client: Client,
    email: "Union[Unset, None, List[str]]" = UNSET,
    group: "Union[Unset, None, str]" = UNSET,
    base_url: "Union[Unset, None, str]" = UNSET,
    redirect_url: "Union[Unset, None, str]" = UNSET,
    fields: "Union[Unset, None, str]" = "token",
) -> Response[List[invite_token_m.InviteToken]]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        email=email,
        group=group,
        base_url=base_url,
        redirect_url=redirect_url,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: "str",
    *,
    client: Client,
    email: "Union[Unset, None, List[str]]" = UNSET,
    group: "Union[Unset, None, str]" = UNSET,
    base_url: "Union[Unset, None, str]" = UNSET,
    redirect_url: "Union[Unset, None, str]" = UNSET,
    fields: "Union[Unset, None, str]" = "token",
) -> Optional[List[invite_token_m.InviteToken]]:
    """ """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            email=email,
            group=group,
            base_url=base_url,
            redirect_url=redirect_url,
            fields=fields,
        )
    ).parsed
