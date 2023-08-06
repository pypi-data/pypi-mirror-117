from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_group import UserGroup
else:
    UserGroup = "UserGroup"

from ..models.user import User

T = TypeVar("T", bound="ProjectTeamMember")


@attr.s(auto_attribs=True)
class ProjectTeamMember(User):
    """ """

    team_own_user: Union[Unset, bool] = UNSET
    team_groups: Union[Unset, List[UserGroup]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_own_user = self.team_own_user
        team_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.team_groups, Unset):
            team_groups = []
            for team_groups_item_data in self.team_groups:
                team_groups_item = team_groups_item_data.to_dict()

                team_groups.append(team_groups_item)

        field_dict: Dict[str, Any] = {}
        _User_dict = super(User).to_dict()
        field_dict.update(_User_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team_own_user is not UNSET:
            field_dict["teamOwnUser"] = team_own_user
        if team_groups is not UNSET:
            field_dict["teamGroups"] = team_groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _User_kwargs = super(User).from_dict(src_dict=d).to_dict()

        team_own_user = d.pop("teamOwnUser", UNSET)

        team_groups = []
        _team_groups = d.pop("teamGroups", UNSET)
        for team_groups_item_data in _team_groups or []:
            team_groups_item = UserGroup.from_dict(team_groups_item_data)

            team_groups.append(team_groups_item)

        project_team_member = cls(
            team_own_user=team_own_user,
            team_groups=team_groups,
            **_User_kwargs,
        )

        project_team_member.additional_properties = d
        return project_team_member

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
