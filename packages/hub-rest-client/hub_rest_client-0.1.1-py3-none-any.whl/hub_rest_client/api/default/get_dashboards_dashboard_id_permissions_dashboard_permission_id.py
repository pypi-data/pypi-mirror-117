from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.dashboard_permission import DashboardPermission
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dashboard_id: str,
    dashboard_permission_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "permission",
) -> Dict[str, Any]:
    url = "{}/dashboards/{dashboardId}/permissions/{dashboardPermissionId}".format(
        client.hub_base_url, dashboardId=dashboard_id, dashboardPermissionId=dashboard_permission_id
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
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


def _parse_response(*, response: httpx.Response) -> Optional[DashboardPermission]:
    if response.status_code == 200:
        response_200 = DashboardPermission.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[DashboardPermission]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    dashboard_id: str,
    dashboard_permission_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "permission",
) -> Response[DashboardPermission]:
    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        dashboard_permission_id=dashboard_permission_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    dashboard_id: str,
    dashboard_permission_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "permission",
) -> Optional[DashboardPermission]:
    """ """

    return sync_detailed(
        dashboard_id=dashboard_id,
        dashboard_permission_id=dashboard_permission_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    dashboard_id: str,
    dashboard_permission_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "permission",
) -> Response[DashboardPermission]:
    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        dashboard_permission_id=dashboard_permission_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    dashboard_id: str,
    dashboard_permission_id: str,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, None, str] = "permission",
) -> Optional[DashboardPermission]:
    """ """

    return (
        await asyncio_detailed(
            dashboard_id=dashboard_id,
            dashboard_permission_id=dashboard_permission_id,
            client=client,
            fields=fields,
        )
    ).parsed
