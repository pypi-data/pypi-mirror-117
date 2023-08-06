from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_group import UserGroup
else:
    UserGroup = "UserGroup"

from ..models.role_source import RoleSource

T = TypeVar("T", bound="GroupRoleSource")


@attr.s(auto_attribs=True)
class GroupRoleSource(RoleSource):
    """ """

    group: Union[Unset, UserGroup] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        field_dict: Dict[str, Any] = {}
        _RoleSource_dict = super(RoleSource).to_dict()
        field_dict.update(_RoleSource_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _RoleSource_kwargs = super(RoleSource).from_dict(src_dict=d).to_dict()

        _group = d.pop("group", UNSET)
        group: Union[Unset, UserGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = UserGroup.from_dict(_group)

        group_role_source = cls(
            group=group,
            **_RoleSource_kwargs,
        )

        group_role_source.additional_properties = d
        return group_role_source

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
