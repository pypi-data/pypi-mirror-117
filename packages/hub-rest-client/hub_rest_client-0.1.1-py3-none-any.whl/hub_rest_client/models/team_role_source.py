from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_team import ProjectTeam
else:
    ProjectTeam = "ProjectTeam"

from ..models.role_source import RoleSource

T = TypeVar("T", bound="TeamRoleSource")


@attr.s(auto_attribs=True)
class TeamRoleSource(RoleSource):
    """ """

    team: Union[Unset, ProjectTeam] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        _RoleSource_dict = super(RoleSource).to_dict()
        field_dict.update(_RoleSource_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _RoleSource_kwargs = super(RoleSource).from_dict(src_dict=d).to_dict()

        _team = d.pop("team", UNSET)
        team: Union[Unset, ProjectTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = ProjectTeam.from_dict(_team)

        team_role_source = cls(
            team=team,
            **_RoleSource_kwargs,
        )

        team_role_source.additional_properties = d
        return team_role_source

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
