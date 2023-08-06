from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="TeamProjectRoleSource")


try:
    from ..models import team_role_source
except ImportError:
    import sys

    team_role_source = sys.modules[__package__ + "team_role_source"]


@attr.s(auto_attribs=True)
class TeamProjectRoleSource(team_role_source.TeamRoleSource):
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _TeamRoleSource_dict = super().to_dict()
        field_dict.update(_TeamRoleSource_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        team_project_role_source = cls()

        return team_project_role_source
