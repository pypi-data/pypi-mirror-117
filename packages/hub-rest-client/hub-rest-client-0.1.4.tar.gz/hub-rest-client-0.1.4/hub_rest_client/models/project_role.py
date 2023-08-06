from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectRole")


@attr.s(auto_attribs=True)
class ProjectRole:
    """ """

    type: "str"
    id: "Union[Unset, str]" = UNSET
    aliases: "Union[Unset, List[alias_m.Alias]]" = UNSET
    role: "Union[Unset, role_m.Role]" = UNSET
    project: "Union[Unset, project_m.Project]" = UNSET
    owner: "Union[Unset, authority_holder_m.AuthorityHolder]" = UNSET
    team_member: "Union[Unset, bool]" = UNSET

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

        try:
            from ..models import alias as alias_m
            from ..models import authority_holder as authority_holder_m
            from ..models import project as project_m
            from ..models import role as role_m
        except ImportError:
            import sys

            authority_holder_m = sys.modules[__package__ + "authority_holder"]
            project_m = sys.modules[__package__ + "project"]
            role_m = sys.modules[__package__ + "role"]
            alias_m = sys.modules[__package__ + "alias"]

        d = src_dict.copy()

        type = d.pop("type")

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = alias_m.Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        _role = d.pop("role", UNSET)
        role: Union[Unset, role_m.Role]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = role_m.Role.from_dict(_role)

        _project = d.pop("project", UNSET)
        project: Union[Unset, project_m.Project]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = project_m.Project.from_dict(_project)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, authority_holder_m.AuthorityHolder]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = authority_holder_m.AuthorityHolder.from_dict(_owner)

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

        return project_role
