from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.role_source import RoleSource

T = TypeVar("T", bound="OwnRoleSource")


@attr.s(auto_attribs=True)
class OwnRoleSource(RoleSource):
    """ """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _RoleSource_dict = super(RoleSource).to_dict()
        field_dict.update(_RoleSource_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _RoleSource_kwargs = super(RoleSource).from_dict(src_dict=d).to_dict()

        own_role_source = cls(
            **_RoleSource_kwargs,
        )

        own_role_source.additional_properties = d
        return own_role_source

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
