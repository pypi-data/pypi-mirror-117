from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamRoleSource")


try:
    from ..models import role_source
except ImportError:
    import sys

    role_source = sys.modules[__package__ + "role_source"]


@attr.s(auto_attribs=True)
class TeamRoleSource(role_source.RoleSource):
    """ """

    team: "Union[Unset, project_team_m.ProjectTeam]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        _RoleSource_dict = super().to_dict()
        field_dict.update(_RoleSource_dict)
        field_dict.update({})
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import project_team as project_team_m
        except ImportError:
            import sys

            project_team_m = sys.modules[__package__ + "project_team"]

        d = src_dict.copy()

        _team = d.pop("team", UNSET)
        team: Union[Unset, project_team_m.ProjectTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = project_team_m.ProjectTeam.from_dict(_team)

        team_role_source = cls(
            team=team,
        )

        return team_role_source
