from typing import Any, Dict, Type, TypeVar

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

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _OwnRoleSource_dict = super().to_dict()
        field_dict.update(_OwnRoleSource_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        own_project_role_source = cls()

        return own_project_role_source
