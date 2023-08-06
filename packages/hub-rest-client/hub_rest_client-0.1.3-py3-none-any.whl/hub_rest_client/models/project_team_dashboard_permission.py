from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectTeamDashboardPermission")


try:
    from ..models import dashboard_permission
except ImportError:
    import sys

    dashboard_permission = sys.modules[__package__ + "dashboard_permission"]


@attr.s(auto_attribs=True)
class ProjectTeamDashboardPermission(dashboard_permission.DashboardPermission):
    """ """

    project_team: "Union[Unset, project_team_m.ProjectTeam]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_team, Unset):
            project_team = self.project_team.to_dict()

        field_dict: Dict[str, Any] = {}
        _DashboardPermission_dict = super().to_dict()
        field_dict.update(_DashboardPermission_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_team is not UNSET:
            field_dict["projectTeam"] = project_team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import project_team as project_team_m
        except ImportError:
            import sys

            project_team_m = sys.modules[__package__ + "project_team"]

        d = src_dict.copy()

        _project_team = d.pop("projectTeam", UNSET)
        project_team: Union[Unset, project_team_m.ProjectTeam]
        if isinstance(_project_team, Unset):
            project_team = UNSET
        else:
            project_team = project_team_m.ProjectTeam.from_dict(_project_team)

        project_team_dashboard_permission = cls(
            project_team=project_team,
        )

        project_team_dashboard_permission.additional_properties = d
        return project_team_dashboard_permission

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
