from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardPermission")


try:
    from ..models import uuid
except ImportError:
    import sys

    uuid = sys.modules[__package__ + "uuid"]


@attr.s(auto_attribs=True)
class DashboardPermission(uuid.Uuid):
    """ """

    permission: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        permission = self.permission

        field_dict: Dict[str, Any] = {}
        _Uuid_dict = super().to_dict()
        field_dict.update(_Uuid_dict)
        field_dict.update({})
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        permission = d.pop("permission", UNSET)

        dashboard_permission = cls(
            permission=permission,
        )

        return dashboard_permission
