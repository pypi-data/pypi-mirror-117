from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.uuid import Uuid
from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardPermission")


@attr.s(auto_attribs=True)
class DashboardPermission(Uuid):
    """ """

    permission: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permission = self.permission

        field_dict: Dict[str, Any] = {}
        _Uuid_dict = super(Uuid).to_dict()
        field_dict.update(_Uuid_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Uuid_kwargs = super(Uuid).from_dict(src_dict=d).to_dict()

        permission = d.pop("permission", UNSET)

        dashboard_permission = cls(
            permission=permission,
            **_Uuid_kwargs,
        )

        dashboard_permission.additional_properties = d
        return dashboard_permission

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
