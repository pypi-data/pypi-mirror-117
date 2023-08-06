from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="OwnRoleSource")


try:
    from ..models import role_source
except ImportError:
    import sys

    role_source = sys.modules[__package__ + "role_source"]


@attr.s(auto_attribs=True)
class OwnRoleSource(role_source.RoleSource):
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _RoleSource_dict = super().to_dict()
        field_dict.update(_RoleSource_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        own_role_source = cls()

        return own_role_source
