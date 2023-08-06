from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alias import Alias
    from ..models.authority_holder import AuthorityHolder
    from ..models.project import Project
    from ..models.role import Role
else:
    AuthorityHolder = "AuthorityHolder"
    Role = "Role"
    Project = "Project"
    Alias = "Alias"


T = TypeVar("T", bound="ProjectRole")


@attr.s(auto_attribs=True)
class ProjectRole:
    """ """

    type: str
    id: Union[Unset, str] = UNSET
    aliases: Union[Unset, List[Alias]] = UNSET
    role: Union[Unset, Role] = UNSET
    project: Union[Unset, Project] = UNSET
    owner: Union[Unset, AuthorityHolder] = UNSET
    team_member: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        id = self.id
        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()

                aliases.append(aliases_item)

        role: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        team_member = self.team_member

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if role is not UNSET:
            field_dict["role"] = role
        if project is not UNSET:
            field_dict["project"] = project
        if owner is not UNSET:
            field_dict["owner"] = owner
        if team_member is not UNSET:
            field_dict["teamMember"] = team_member

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        type = d.pop("type")

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        _role = d.pop("role", UNSET)
        role: Union[Unset, Role]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = Role.from_dict(_role)

        _project = d.pop("project", UNSET)
        project: Union[Unset, Project]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, AuthorityHolder]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = AuthorityHolder.from_dict(_owner)

        team_member = d.pop("teamMember", UNSET)

        project_role = cls(
            type=type,
            id=id,
            aliases=aliases,
            role=role,
            project=project,
            owner=owner,
            team_member=team_member,
        )

        project_role.additional_properties = d
        return project_role

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
