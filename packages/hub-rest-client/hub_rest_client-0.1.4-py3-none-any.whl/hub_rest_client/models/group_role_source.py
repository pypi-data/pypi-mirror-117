from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupRoleSource")


try:
    from ..models import role_source
except ImportError:
    import sys

    role_source = sys.modules[__package__ + "role_source"]


@attr.s(auto_attribs=True)
class GroupRoleSource(role_source.RoleSource):
    """ """

    group: "Union[Unset, user_group_m.UserGroup]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        field_dict: Dict[str, Any] = {}
        _RoleSource_dict = super().to_dict()
        field_dict.update(_RoleSource_dict)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            user_group_m = sys.modules[__package__ + "user_group"]

        d = src_dict.copy()

        _group = d.pop("group", UNSET)
        group: Union[Unset, user_group_m.UserGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = user_group_m.UserGroup.from_dict(_group)

        group_role_source = cls(
            group=group,
        )

        return group_role_source
