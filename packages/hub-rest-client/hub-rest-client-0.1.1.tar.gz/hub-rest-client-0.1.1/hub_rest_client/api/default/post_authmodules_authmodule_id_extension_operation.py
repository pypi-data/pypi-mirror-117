from typing import Any, Dict

import httpx

from ...client import Client
from ...models.post_authmodules_authmodule_id_extension_operation_json_body import (
    PostAuthmodulesAuthmoduleIdExtensionOperationJsonBody,
)
from ...types import Response


def _get_kwargs(
    authmodule_id: str,
    operation: str,
    *,
    client: Client,
    json_body: PostAuthmodulesAuthmoduleIdExtensionOperationJsonBody,
) -> Dict[str, Any]:
    url = "{}/authmodules/{authmoduleId}/extension/{operation}".format(
        client.hub_base_url, authmoduleId=authmodule_id, operation=operation
    )

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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    authmodule_id: str,
    operation: str,
    *,
    client: Client,
    json_body: PostAuthmodulesAuthmoduleIdExtensionOperationJsonBody,
) -> Response[Any]:
    kwargs = _get_kwargs(
        authmodule_id=authmodule_id,
        operation=operation,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    authmodule_id: str,
    operation: str,
    *,
    client: Client,
    json_body: PostAuthmodulesAuthmoduleIdExtensionOperationJsonBody,
) -> Response[Any]:
    kwargs = _get_kwargs(
        authmodule_id=authmodule_id,
        operation=operation,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
