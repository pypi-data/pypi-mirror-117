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

        d = src_dict.copy()

        _OwnRoleSource_kwargs = super().from_dict(src_dict=d).to_dict()
        _OwnRoleSource_kwargs.pop("$type")

        own_project_role_source = cls(
            **_OwnRoleSource_kwargs,
        )

        return own_project_role_source
