from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.team_role_source import TeamRoleSource

T = TypeVar("T", bound="TeamProjectRoleSource")


@attr.s(auto_attribs=True)
class TeamProjectRoleSource(TeamRoleSource):
    """ """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _TeamRoleSource_dict = super(TeamRoleSource).to_dict()
        field_dict.update(_TeamRoleSource_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _TeamRoleSource_kwargs = super(TeamRoleSource).from_dict(src_dict=d).to_dict()

        team_project_role_source = cls(
            **_TeamRoleSource_kwargs,
        )

        team_project_role_source.additional_properties = d
        return team_project_role_source

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
