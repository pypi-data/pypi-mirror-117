from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_group import UserGroup
else:
    UserGroup = "UserGroup"

from ..models.dashboard_permission import DashboardPermission

T = TypeVar("T", bound="UserGroupDashboardPermission")


@attr.s(auto_attribs=True)
class UserGroupDashboardPermission(DashboardPermission):
    """ """

    user_group: Union[Unset, UserGroup] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_group, Unset):
            user_group = self.user_group.to_dict()

        field_dict: Dict[str, Any] = {}
        _DashboardPermission_dict = super(DashboardPermission).to_dict()
        field_dict.update(_DashboardPermission_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_group is not UNSET:
            field_dict["userGroup"] = user_group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _DashboardPermission_kwargs = super(DashboardPermission).from_dict(src_dict=d).to_dict()

        _user_group = d.pop("userGroup", UNSET)
        user_group: Union[Unset, UserGroup]
        if isinstance(_user_group, Unset):
            user_group = UNSET
        else:
            user_group = UserGroup.from_dict(_user_group)

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
