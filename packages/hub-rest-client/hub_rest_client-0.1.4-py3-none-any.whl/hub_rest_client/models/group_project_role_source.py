from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="GroupProjectRoleSource")


try:
    from ..models import group_role_source
except ImportError:
    import sys

    group_role_source = sys.modules[__package__ + "group_role_source"]


@attr.s(auto_attribs=True)
class GroupProjectRoleSource(group_role_source.GroupRoleSource):
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _GroupRoleSource_dict = super().to_dict()
        field_dict.update(_GroupRoleSource_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        group_project_role_source = cls()

        return group_project_role_source
