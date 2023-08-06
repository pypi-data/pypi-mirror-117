from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserGroupDashboardPermission")


try:
    from ..models import dashboard_permission
except ImportError:
    import sys

    dashboard_permission = sys.modules[__package__ + "dashboard_permission"]


@attr.s(auto_attribs=True)
class UserGroupDashboardPermission(dashboard_permission.DashboardPermission):
    """ """

    user_group: "Union[Unset, user_group_m.UserGroup]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_group, Unset):
            user_group = self.user_group.to_dict()

        field_dict: Dict[str, Any] = {}
        _DashboardPermission_dict = super().to_dict()
        field_dict.update(_DashboardPermission_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_group is not UNSET:
            field_dict["userGroup"] = user_group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            user_group_m = sys.modules[__package__ + "user_group"]

        d = src_dict.copy()

        _DashboardPermission_kwargs = super().from_dict(src_dict=d).to_dict()

        _user_group = d.pop("userGroup", UNSET)
        user_group: Union[Unset, user_group_m.UserGroup]
        if isinstance(_user_group, Unset):
            user_group = UNSET
        else:
            user_group = user_group_m.UserGroup.from_dict(_user_group)

        user_group_dashboard_permission = cls(
            user_group=user_group,
            **_DashboardPermission_kwargs,
        )

        user_group_dashboard_permission.additional_properties = d
        return user_group_dashboard_permission

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
