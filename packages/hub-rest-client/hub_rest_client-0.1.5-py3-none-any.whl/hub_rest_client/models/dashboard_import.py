from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardImport")


@attr.s(auto_attribs=True)
class DashboardImport:
    """ """

    id: "Union[Unset, str]" = UNSET
    name: "Union[Unset, str]" = UNSET
    owner: "Union[Unset, str]" = UNSET
    json: "Union[Unset, str]" = UNSET
    permissions: "Union[Unset, List[dashboard_permission_import_m.DashboardPermissionImport]]" = UNSET
    user_dashboards: "Union[Unset, List[user_dashboard_import_m.UserDashboardImport]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        owner = self.owner
        json = self.json
        permissions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()

                permissions.append(permissions_item)

        user_dashboards: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_dashboards, Unset):
            user_dashboards = []
            for user_dashboards_item_data in self.user_dashboards:
                user_dashboards_item = user_dashboards_item_data.to_dict()

                user_dashboards.append(user_dashboards_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if json is not UNSET:
            field_dict["json"] = json
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if user_dashboards is not UNSET:
            field_dict["userDashboards"] = user_dashboards

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import dashboard_permission_import as dashboard_permission_import_m
            from ..models import user_dashboard_import as user_dashboard_import_m
        except ImportError:
            import sys

            user_dashboard_import_m = sys.modules[__package__ + "user_dashboard_import"]
            dashboard_permission_import_m = sys.modules[__package__ + "dashboard_permission_import"]

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        owner = d.pop("owner", UNSET)

        json = d.pop("json", UNSET)

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = dashboard_permission_import_m.DashboardPermissionImport.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        user_dashboards = []
        _user_dashboards = d.pop("userDashboards", UNSET)
        for user_dashboards_item_data in _user_dashboards or []:
            user_dashboards_item = user_dashboard_import_m.UserDashboardImport.from_dict(user_dashboards_item_data)

            user_dashboards.append(user_dashboards_item)

        dashboard_import = cls(
            id=id,
            name=name,
            owner=owner,
            json=json,
            permissions=permissions,
            user_dashboards=user_dashboards,
        )

        return dashboard_import
