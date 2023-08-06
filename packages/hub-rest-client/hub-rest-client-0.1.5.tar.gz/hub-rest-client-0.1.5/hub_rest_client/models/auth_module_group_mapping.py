from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthModuleGroupMapping")


@attr.s(auto_attribs=True)
class AuthModuleGroupMapping:
    """ """

    external_group_name: "Union[Unset, str]" = UNSET
    group: "Union[Unset, user_group_m.UserGroup]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        external_group_name = self.external_group_name
        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if external_group_name is not UNSET:
            field_dict["externalGroupName"] = external_group_name
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

        external_group_name = d.pop("externalGroupName", UNSET)

        _group = d.pop("group", UNSET)
        group: Union[Unset, user_group_m.UserGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = user_group_m.UserGroup.from_dict(_group)

        auth_module_group_mapping = cls(
            external_group_name=external_group_name,
            group=group,
        )

        return auth_module_group_mapping
