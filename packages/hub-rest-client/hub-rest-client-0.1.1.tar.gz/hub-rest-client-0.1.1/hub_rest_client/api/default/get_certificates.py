from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.certificates_page import CertificatesPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    disabled: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "id,disabled,name,data,certificateType,version,serialNumber,issuedBy,issuedTo,validFrom,validTo,algorithm",
) -> Dict[str, Any]:
    url = "{}/certificates".format(client.hub_base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "disabled": disabled,
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


def _parse_response(*, response: httpx.Response) -> Optional[CertificatesPage]:
    if response.status_code == 200:
        response_200 = CertificatesPage.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CertificatesPage]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    disabled: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "id,disabled,name,data,certificateType,version,serialNumber,issuedBy,issuedTo,validFrom,validTo,algorithm",
) -> Response[CertificatesPage]:
    kwargs = _get_kwargs(
        client=client,
        disabled=disabled,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    disabled: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "id,disabled,name,data,certificateType,version,serialNumber,issuedBy,issuedTo,validFrom,validTo,algorithm",
) -> Optional[CertificatesPage]:
    """ """

    return sync_detailed(
        client=client,
        disabled=disabled,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    disabled: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "id,disabled,name,data,certificateType,version,serialNumber,issuedBy,issuedTo,validFrom,validTo,algorithm",
) -> Response[CertificatesPage]:
    kwargs = _get_kwargs(
        client=client,
        disabled=disabled,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    disabled: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "id,disabled,name,data,certificateType,version,serialNumber,issuedBy,issuedTo,validFrom,validTo,algorithm",
) -> Optional[CertificatesPage]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            disabled=disabled,
            fields=fields,
        )
    ).parsed
