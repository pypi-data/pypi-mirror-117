from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthorityHolder")


@attr.s(auto_attribs=True)
class AuthorityHolder:
    """ """

    type: "str"
    id: "Union[Unset, str]" = UNSET
    aliases: "Union[Unset, List[alias_m.Alias]]" = UNSET
    name: "Union[Unset, str]" = UNSET
    project_roles: "Union[Unset, List[project_role_m.ProjectRole]]" = UNSET
    transitive_project_roles: "Union[Unset, List[project_role_m.ProjectRole]]" = UNSET
    sourced_project_roles: "Union[Unset, List[sourced_project_role_m.SourcedProjectRole]]" = UNSET
    organization_roles: "Union[Unset, List[organization_role_m.OrganizationRole]]" = UNSET
    transitive_organization_roles: "Union[Unset, List[organization_role_m.OrganizationRole]]" = UNSET
    sourced_organization_roles: "Union[Unset, List[sourced_organization_role_m.SourcedOrganizationRole]]" = UNSET
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

        name = self.name
        project_roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.project_roles, Unset):
            project_roles = []
            for project_roles_item_data in self.project_roles:
                project_roles_item = project_roles_item_data.to_dict()

                project_roles.append(project_roles_item)

        transitive_project_roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transitive_project_roles, Unset):
            transitive_project_roles = []
            for transitive_project_roles_item_data in self.transitive_project_roles:
                transitive_project_roles_item = transitive_project_roles_item_data.to_dict()

                transitive_project_roles.append(transitive_project_roles_item)

        sourced_project_roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sourced_project_roles, Unset):
            sourced_project_roles = []
            for sourced_project_roles_item_data in self.sourced_project_roles:
                sourced_project_roles_item = sourced_project_roles_item_data.to_dict()

                sourced_project_roles.append(sourced_project_roles_item)

        organization_roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organization_roles, Unset):
            organization_roles = []
            for organization_roles_item_data in self.organization_roles:
                organization_roles_item = organization_roles_item_data.to_dict()

                organization_roles.append(organization_roles_item)

        transitive_organization_roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transitive_organization_roles, Unset):
            transitive_organization_roles = []
            for transitive_organization_roles_item_data in self.transitive_organization_roles:
                transitive_organization_roles_item = transitive_organization_roles_item_data.to_dict()

                transitive_organization_roles.append(transitive_organization_roles_item)

        sourced_organization_roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sourced_organization_roles, Unset):
            sourced_organization_roles = []
            for sourced_organization_roles_item_data in self.sourced_organization_roles:
                sourced_organization_roles_item = sourced_organization_roles_item_data.to_dict()

                sourced_organization_roles.append(sourced_organization_roles_item)

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
        if name is not UNSET:
            field_dict["name"] = name
        if project_roles is not UNSET:
            field_dict["projectRoles"] = project_roles
        if transitive_project_roles is not UNSET:
            field_dict["transitiveProjectRoles"] = transitive_project_roles
        if sourced_project_roles is not UNSET:
            field_dict["sourcedProjectRoles"] = sourced_project_roles
        if organization_roles is not UNSET:
            field_dict["organizationRoles"] = organization_roles
        if transitive_organization_roles is not UNSET:
            field_dict["transitiveOrganizationRoles"] = transitive_organization_roles
        if sourced_organization_roles is not UNSET:
            field_dict["sourcedOrganizationRoles"] = sourced_organization_roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import alias as alias_m
            from ..models import organization_role as organization_role_m
            from ..models import project_role as project_role_m
            from ..models import sourced_organization_role as sourced_organization_role_m
            from ..models import sourced_project_role as sourced_project_role_m
        except ImportError:
            import sys

            organization_role_m = sys.modules[__package__ + "organization_role"]
            alias_m = sys.modules[__package__ + "alias"]
            sourced_project_role_m = sys.modules[__package__ + "sourced_project_role"]
            project_role_m = sys.modules[__package__ + "project_role"]
            sourced_organization_role_m = sys.modules[__package__ + "sourced_organization_role"]

        d = src_dict.copy()

        type = d.pop("type")

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = alias_m.Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        name = d.pop("name", UNSET)

        project_roles = []
        _project_roles = d.pop("projectRoles", UNSET)
        for project_roles_item_data in _project_roles or []:
            project_roles_item = project_role_m.ProjectRole.from_dict(project_roles_item_data)

            project_roles.append(project_roles_item)

        transitive_project_roles = []
        _transitive_project_roles = d.pop("transitiveProjectRoles", UNSET)
        for transitive_project_roles_item_data in _transitive_project_roles or []:
            transitive_project_roles_item = project_role_m.ProjectRole.from_dict(transitive_project_roles_item_data)

            transitive_project_roles.append(transitive_project_roles_item)

        sourced_project_roles = []
        _sourced_project_roles = d.pop("sourcedProjectRoles", UNSET)
        for sourced_project_roles_item_data in _sourced_project_roles or []:
            sourced_project_roles_item = sourced_project_role_m.SourcedProjectRole.from_dict(
                sourced_project_roles_item_data
            )

            sourced_project_roles.append(sourced_project_roles_item)

        organization_roles = []
        _organization_roles = d.pop("organizationRoles", UNSET)
        for organization_roles_item_data in _organization_roles or []:
            organization_roles_item = organization_role_m.OrganizationRole.from_dict(organization_roles_item_data)

            organization_roles.append(organization_roles_item)

        transitive_organization_roles = []
        _transitive_organization_roles = d.pop("transitiveOrganizationRoles", UNSET)
        for transitive_organization_roles_item_data in _transitive_organization_roles or []:
            transitive_organization_roles_item = organization_role_m.OrganizationRole.from_dict(
                transitive_organization_roles_item_data
            )

            transitive_organization_roles.append(transitive_organization_roles_item)

        sourced_organization_roles = []
        _sourced_organization_roles = d.pop("sourcedOrganizationRoles", UNSET)
        for sourced_organization_roles_item_data in _sourced_organization_roles or []:
            sourced_organization_roles_item = sourced_organization_role_m.SourcedOrganizationRole.from_dict(
                sourced_organization_roles_item_data
            )

            sourced_organization_roles.append(sourced_organization_roles_item)

        authority_holder = cls(
            type=type,
            id=id,
            aliases=aliases,
            name=name,
            project_roles=project_roles,
            transitive_project_roles=transitive_project_roles,
            sourced_project_roles=sourced_project_roles,
            organization_roles=organization_roles,
            transitive_organization_roles=transitive_organization_roles,
            sourced_organization_roles=sourced_organization_roles,
        )

        authority_holder.additional_properties = d
        return authority_holder

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
