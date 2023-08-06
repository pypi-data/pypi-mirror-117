from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.smtp_message import SmtpMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    settings_id: str,
    *,
    client: Client,
    json_body: SmtpMessage,
    require_email_verification: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/settings/{settingsId}/smtp/message".format(client.hub_base_url, settingsId=settings_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "requireEmailVerification": require_email_verification,
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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    settings_id: str,
    *,
    client: Client,
    json_body: SmtpMessage,
    require_email_verification: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        settings_id=settings_id,
        client=client,
        json_body=json_body,
        require_email_verification=require_email_verification,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    settings_id: str,
    *,
    client: Client,
    json_body: SmtpMessage,
    require_email_verification: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        settings_id=settings_id,
        client=client,
        json_body=json_body,
        require_email_verification=require_email_verification,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
