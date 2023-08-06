from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models import profile as profile_m
from ...types import Response


def _get_kwargs(
    user_id: "str",
    *,
    client: Client,
    json_body: profile_m.Profile,
) -> Dict[str, Any]:
    url = "{}/users/{userId}/verifyContact".format(client.hub_base_url, userId=user_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[profile_m.Profile]:
    if response.status_code == 200:
        response_200 = profile_m.Profile.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[profile_m.Profile]:
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
    json_body: profile_m.Profile,
) -> Response[profile_m.Profile]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: "str",
    *,
    client: Client,
    json_body: profile_m.Profile,
) -> Optional[profile_m.Profile]:
    """ """

    return sync_detailed(
        user_id=user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    user_id: "str",
    *,
    client: Client,
    json_body: profile_m.Profile,
) -> Response[profile_m.Profile]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: "str",
    *,
    client: Client,
    json_body: profile_m.Profile,
) -> Optional[profile_m.Profile]:
    """ """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
