from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserDashboardPermission")


try:
    from ..models import dashboard_permission
except ImportError:
    import sys

    dashboard_permission = sys.modules[__package__ + "dashboard_permission"]


@attr.s(auto_attribs=True)
class UserDashboardPermission(dashboard_permission.DashboardPermission):
    """ """

    user: "Union[Unset, user_m.User]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        _DashboardPermission_dict = super().to_dict()
        field_dict.update(_DashboardPermission_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import user as user_m
        except ImportError:
            import sys

            user_m = sys.modules[__package__ + "user"]

        d = src_dict.copy()

        _DashboardPermission_kwargs = super().from_dict(src_dict=d).to_dict()

        _user = d.pop("user", UNSET)
        user: Union[Unset, user_m.User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = user_m.User.from_dict(_user)

        user_dashboard_permission = cls(
            user=user,
            **_DashboardPermission_kwargs,
        )

        user_dashboard_permission.additional_properties = d
        return user_dashboard_permission

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
