from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.certificate import Certificate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    certificate_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Certificate,
    fields: Union[
        Unset, None, str
    ] = "id,disabled,name,data,certificateType,version,serialNumber,issuedBy,issuedTo,validFrom,validTo,algorithm",
) -> Dict[str, Any]:
    url = "{}/certificates/{certificateId}".format(client.hub_base_url, certificateId=certificate_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Certificate]:
    if response.status_code == 200:
        response_200 = Certificate.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Certificate]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    certificate_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Certificate,
    fields: Union[
        Unset, None, str
    ] = "id,disabled,name,data,certificateType,version,serialNumber,issuedBy,issuedTo,validFrom,validTo,algorithm",
) -> Response[Certificate]:
    kwargs = _get_kwargs(
        certificate_id=certificate_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    certificate_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Certificate,
    fields: Union[
        Unset, None, str
    ] = "id,disabled,name,data,certificateType,version,serialNumber,issuedBy,issuedTo,validFrom,validTo,algorithm",
) -> Optional[Certificate]:
    """ """

    return sync_detailed(
        certificate_id=certificate_id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    certificate_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Certificate,
    fields: Union[
        Unset, None, str
    ] = "id,disabled,name,data,certificateType,version,serialNumber,issuedBy,issuedTo,validFrom,validTo,algorithm",
) -> Response[Certificate]:
    kwargs = _get_kwargs(
        certificate_id=certificate_id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    certificate_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Certificate,
    fields: Union[
        Unset, None, str
    ] = "id,disabled,name,data,certificateType,version,serialNumber,issuedBy,issuedTo,validFrom,validTo,algorithm",
) -> Optional[Certificate]:
    """ """

    return (
        await asyncio_detailed(
            certificate_id=certificate_id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
