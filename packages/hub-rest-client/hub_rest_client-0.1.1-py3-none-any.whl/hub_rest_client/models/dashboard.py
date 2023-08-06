from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_permission import DashboardPermission
    from ..models.user import User
else:
    DashboardPermission = "DashboardPermission"
    User = "User"

from ..models.uuid import Uuid

T = TypeVar("T", bound="Dashboard")


@attr.s(auto_attribs=True)
class Dashboard(Uuid):
    """ """

    name: Union[Unset, str] = UNSET
    owner: Union[Unset, User] = UNSET
    data: Union[Unset, str] = UNSET
    permission: Union[Unset, str] = UNSET
    access: Union[Unset, str] = UNSET
    permissions: Union[Unset, List[DashboardPermission]] = UNSET
    favorite: Union[Unset, bool] = UNSET
    ordinal: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        data = self.data
        permission = self.permission
        access = self.access
        permissions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()

                permissions.append(permissions_item)

        favorite = self.favorite
        ordinal = self.ordinal

        field_dict: Dict[str, Any] = {}
        _Uuid_dict = super(Uuid).to_dict()
        field_dict.update(_Uuid_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if data is not UNSET:
            field_dict["data"] = data
        if permission is not UNSET:
            field_dict["permission"] = permission
        if access is not UNSET:
            field_dict["access"] = access
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Uuid_kwargs = super(Uuid).from_dict(src_dict=d).to_dict()

        name = d.pop("name", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, User]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = User.from_dict(_owner)

        data = d.pop("data", UNSET)

        permission = d.pop("permission", UNSET)

        access = d.pop("access", UNSET)

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = DashboardPermission.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        favorite = d.pop("favorite", UNSET)

        ordinal = d.pop("ordinal", UNSET)

        dashboard = cls(
            name=name,
            owner=owner,
            data=data,
            permission=permission,
            access=access,
            permissions=permissions,
            favorite=favorite,
            ordinal=ordinal,
            **_Uuid_kwargs,
        )

        dashboard.additional_properties = d
        return dashboard

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
