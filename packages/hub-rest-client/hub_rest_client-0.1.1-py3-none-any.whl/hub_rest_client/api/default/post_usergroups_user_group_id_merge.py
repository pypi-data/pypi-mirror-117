from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.user_group import UserGroup
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_group_id: str,
    *,
    client: Client,
    json_body: UserGroup,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    auto_join: Union[Unset, None, bool] = UNSET,
    required_two_factor_authentication: Union[Unset, None, bool] = UNSET,
    project: Union[Unset, None, str] = UNSET,
    parent_group: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Dict[str, Any]:
    url = "{}/usergroups/{userGroupId}/merge".format(client.hub_base_url, userGroupId=user_group_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "name": name,
        "description": description,
        "autoJoin": auto_join,
        "requiredTwoFactorAuthentication": required_two_factor_authentication,
        "project": project,
        "parentGroup": parent_group,
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


def _parse_response(*, response: httpx.Response) -> Optional[List[UserGroup]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserGroup.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[UserGroup]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_group_id: str,
    *,
    client: Client,
    json_body: UserGroup,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    auto_join: Union[Unset, None, bool] = UNSET,
    required_two_factor_authentication: Union[Unset, None, bool] = UNSET,
    project: Union[Unset, None, str] = UNSET,
    parent_group: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Response[List[UserGroup]]:
    kwargs = _get_kwargs(
        user_group_id=user_group_id,
        client=client,
        json_body=json_body,
        name=name,
        description=description,
        auto_join=auto_join,
        required_two_factor_authentication=required_two_factor_authentication,
        project=project,
        parent_group=parent_group,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_group_id: str,
    *,
    client: Client,
    json_body: UserGroup,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    auto_join: Union[Unset, None, bool] = UNSET,
    required_two_factor_authentication: Union[Unset, None, bool] = UNSET,
    project: Union[Unset, None, str] = UNSET,
    parent_group: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Optional[List[UserGroup]]:
    """ """

    return sync_detailed(
        user_group_id=user_group_id,
        client=client,
        json_body=json_body,
        name=name,
        description=description,
        auto_join=auto_join,
        required_two_factor_authentication=required_two_factor_authentication,
        project=project,
        parent_group=parent_group,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    user_group_id: str,
    *,
    client: Client,
    json_body: UserGroup,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    auto_join: Union[Unset, None, bool] = UNSET,
    required_two_factor_authentication: Union[Unset, None, bool] = UNSET,
    project: Union[Unset, None, str] = UNSET,
    parent_group: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Response[List[UserGroup]]:
    kwargs = _get_kwargs(
        user_group_id=user_group_id,
        client=client,
        json_body=json_body,
        name=name,
        description=description,
        auto_join=auto_join,
        required_two_factor_authentication=required_two_factor_authentication,
        project=project,
        parent_group=parent_group,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_group_id: str,
    *,
    client: Client,
    json_body: UserGroup,
    name: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    auto_join: Union[Unset, None, bool] = UNSET,
    required_two_factor_authentication: Union[Unset, None, bool] = UNSET,
    project: Union[Unset, None, str] = UNSET,
    parent_group: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "description,iconUrl,autoJoin,requiredTwoFactorAuthentication,parentsRequireTwoFactorAuthentication,userCount,allUsers,implicit,queriedSingleton,removable",
) -> Optional[List[UserGroup]]:
    """ """

    return (
        await asyncio_detailed(
            user_group_id=user_group_id,
            client=client,
            json_body=json_body,
            name=name,
            description=description,
            auto_join=auto_join,
            required_two_factor_authentication=required_two_factor_authentication,
            project=project,
            parent_group=parent_group,
            fields=fields,
        )
    ).parsed
