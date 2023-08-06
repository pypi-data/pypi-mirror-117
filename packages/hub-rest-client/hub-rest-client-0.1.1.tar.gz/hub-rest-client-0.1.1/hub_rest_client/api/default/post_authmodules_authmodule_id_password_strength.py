from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.password_strength import PasswordStrength
from ...models.plainpassword import Plainpassword
from ...types import UNSET, Response, Unset


def _get_kwargs(
    authmodule_id: str,
    *,
    client: Client,
    json_body: Plainpassword,
    user: Union[Unset, None, str] = UNSET,
    username: Union[Unset, None, List[str]] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "referenceScore,score,maxScore,referenceEntropy,entropy,maxEntropy,feedbackMessage",
) -> Dict[str, Any]:
    url = "{}/authmodules/{authmoduleId}/password/strength".format(client.hub_base_url, authmoduleId=authmodule_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_username: Union[Unset, None, List[str]] = UNSET
    if not isinstance(username, Unset):
        if username is None:
            json_username = None
        else:
            json_username = username

    params: Dict[str, Any] = {
        "user": user,
        "username": json_username,
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


def _parse_response(*, response: httpx.Response) -> Optional[List[PasswordStrength]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PasswordStrength.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[PasswordStrength]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    authmodule_id: str,
    *,
    client: Client,
    json_body: Plainpassword,
    user: Union[Unset, None, str] = UNSET,
    username: Union[Unset, None, List[str]] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "referenceScore,score,maxScore,referenceEntropy,entropy,maxEntropy,feedbackMessage",
) -> Response[List[PasswordStrength]]:
    kwargs = _get_kwargs(
        authmodule_id=authmodule_id,
        client=client,
        json_body=json_body,
        user=user,
        username=username,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    authmodule_id: str,
    *,
    client: Client,
    json_body: Plainpassword,
    user: Union[Unset, None, str] = UNSET,
    username: Union[Unset, None, List[str]] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "referenceScore,score,maxScore,referenceEntropy,entropy,maxEntropy,feedbackMessage",
) -> Optional[List[PasswordStrength]]:
    """ """

    return sync_detailed(
        authmodule_id=authmodule_id,
        client=client,
        json_body=json_body,
        user=user,
        username=username,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    authmodule_id: str,
    *,
    client: Client,
    json_body: Plainpassword,
    user: Union[Unset, None, str] = UNSET,
    username: Union[Unset, None, List[str]] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "referenceScore,score,maxScore,referenceEntropy,entropy,maxEntropy,feedbackMessage",
) -> Response[List[PasswordStrength]]:
    kwargs = _get_kwargs(
        authmodule_id=authmodule_id,
        client=client,
        json_body=json_body,
        user=user,
        username=username,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    authmodule_id: str,
    *,
    client: Client,
    json_body: Plainpassword,
    user: Union[Unset, None, str] = UNSET,
    username: Union[Unset, None, List[str]] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "referenceScore,score,maxScore,referenceEntropy,entropy,maxEntropy,feedbackMessage",
) -> Optional[List[PasswordStrength]]:
    """ """

    return (
        await asyncio_detailed(
            authmodule_id=authmodule_id,
            client=client,
            json_body=json_body,
            user=user,
            username=username,
            fields=fields,
        )
    ).parsed
