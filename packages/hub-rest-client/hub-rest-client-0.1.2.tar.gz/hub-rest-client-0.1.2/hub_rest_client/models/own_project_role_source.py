from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="OwnProjectRoleSource")


try:
    from ..models import own_role_source
except ImportError:
    import sys

    own_role_source = sys.modules[__package__ + "own_role_source"]


@attr.s(auto_attribs=True)
class OwnProjectRoleSource(own_role_source.OwnRoleSource):
    """ """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _OwnRoleSource_dict = super().to_dict()
        field_dict.update(_OwnRoleSource_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _OwnRoleSource_kwargs = super().from_dict(src_dict=d).to_dict()

        own_project_role_source = cls(
            **_OwnRoleSource_kwargs,
        )

        own_project_role_source.additional_properties = d
        return own_project_role_source

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
