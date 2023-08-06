from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_permission_import import DashboardPermissionImport
    from ..models.user_dashboard_import import UserDashboardImport
else:
    UserDashboardImport = "UserDashboardImport"
    DashboardPermissionImport = "DashboardPermissionImport"


T = TypeVar("T", bound="DashboardImport")


@attr.s(auto_attribs=True)
class DashboardImport:
    """ """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    json: Union[Unset, str] = UNSET
    permissions: Union[Unset, List[DashboardPermissionImport]] = UNSET
    user_dashboards: Union[Unset, List[UserDashboardImport]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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
        d = src_dict.copy()

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        owner = d.pop("owner", UNSET)

        json = d.pop("json", UNSET)

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = DashboardPermissionImport.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        user_dashboards = []
        _user_dashboards = d.pop("userDashboards", UNSET)
        for user_dashboards_item_data in _user_dashboards or []:
            user_dashboards_item = UserDashboardImport.from_dict(user_dashboards_item_data)

            user_dashboards.append(user_dashboards_item)

        dashboard_import = cls(
            id=id,
            name=name,
            owner=owner,
            json=json,
            permissions=permissions,
            user_dashboards=user_dashboards,
        )

        dashboard_import.additional_properties = d
        return dashboard_import

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
