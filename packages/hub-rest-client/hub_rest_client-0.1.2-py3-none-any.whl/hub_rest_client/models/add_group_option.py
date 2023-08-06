from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddGroupOption")


try:
    from ..models import access_grant_option
except ImportError:
    import sys

    access_grant_option = sys.modules[__package__ + "access_grant_option"]


@attr.s(auto_attribs=True)
class AddGroupOption(access_grant_option.AccessGrantOption):
    """ """

    group: "Union[Unset, user_group_m.UserGroup]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        field_dict: Dict[str, Any] = {}
        _AccessGrantOption_dict = super().to_dict()
        field_dict.update(_AccessGrantOption_dict)
        field_dict.update(self.additional_properties)
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

        _AccessGrantOption_kwargs = super().from_dict(src_dict=d).to_dict()

        _group = d.pop("group", UNSET)
        group: Union[Unset, user_group_m.UserGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = user_group_m.UserGroup.from_dict(_group)

        add_group_option = cls(
            group=group,
            **_AccessGrantOption_kwargs,
        )

        add_group_option.additional_properties = d
        return add_group_option

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
