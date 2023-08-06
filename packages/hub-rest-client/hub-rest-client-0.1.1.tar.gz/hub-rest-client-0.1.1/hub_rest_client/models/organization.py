from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alias import Alias
    from ..models.organization_role import OrganizationRole
    from ..models.project import Project
    from ..models.project_team import ProjectTeam
    from ..models.user import User
    from ..models.user_group import UserGroup
else:
    UserGroup = "UserGroup"
    ProjectTeam = "ProjectTeam"
    OrganizationRole = "OrganizationRole"
    User = "User"
    Project = "Project"
    Alias = "Alias"


T = TypeVar("T", bound="Organization")


@attr.s(auto_attribs=True)
class Organization:
    """ """

    id: Union[Unset, str] = UNSET
    aliases: Union[Unset, List[Alias]] = UNSET
    key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    email_domain: Union[Unset, str] = UNSET
    creation_time: Union[Unset, int] = UNSET
    projects: Union[Unset, List[Project]] = UNSET
    own_users: Union[Unset, List[User]] = UNSET
    users: Union[Unset, List[User]] = UNSET
    all_users: Union[Unset, bool] = UNSET
    groups: Union[Unset, List[UserGroup]] = UNSET
    teams: Union[Unset, List[ProjectTeam]] = UNSET
    projects_count: Union[Unset, int] = UNSET
    icon_url: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    default_icon: Union[Unset, bool] = UNSET
    organization_roles: Union[Unset, List[OrganizationRole]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()

                aliases.append(aliases_item)

        key = self.key
        name = self.name
        description = self.description
        email_domain = self.email_domain
        creation_time = self.creation_time
        projects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()

                projects.append(projects_item)

        own_users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.own_users, Unset):
            own_users = []
            for own_users_item_data in self.own_users:
                own_users_item = own_users_item_data.to_dict()

                own_users.append(own_users_item)

        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()

                users.append(users_item)

        all_users = self.all_users
        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()

                groups.append(groups_item)

        teams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()

                teams.append(teams_item)

        projects_count = self.projects_count
        icon_url = self.icon_url
        icon = self.icon
        default_icon = self.default_icon
        organization_roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organization_roles, Unset):
            organization_roles = []
            for organization_roles_item_data in self.organization_roles:
                organization_roles_item = organization_roles_item_data.to_dict()

                organization_roles.append(organization_roles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if email_domain is not UNSET:
            field_dict["emailDomain"] = email_domain
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if projects is not UNSET:
            field_dict["projects"] = projects
        if own_users is not UNSET:
            field_dict["ownUsers"] = own_users
        if users is not UNSET:
            field_dict["users"] = users
        if all_users is not UNSET:
            field_dict["allUsers"] = all_users
        if groups is not UNSET:
            field_dict["groups"] = groups
        if teams is not UNSET:
            field_dict["teams"] = teams
        if projects_count is not UNSET:
            field_dict["projectsCount"] = projects_count
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if icon is not UNSET:
            field_dict["icon"] = icon
        if default_icon is not UNSET:
            field_dict["defaultIcon"] = default_icon
        if organization_roles is not UNSET:
            field_dict["organizationRoles"] = organization_roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        email_domain = d.pop("emailDomain", UNSET)

        creation_time = d.pop("creationTime", UNSET)

        projects = []
        _projects = d.pop("projects", UNSET)
        for projects_item_data in _projects or []:
            projects_item = Project.from_dict(projects_item_data)

            projects.append(projects_item)

        own_users = []
        _own_users = d.pop("ownUsers", UNSET)
        for own_users_item_data in _own_users or []:
            own_users_item = User.from_dict(own_users_item_data)

            own_users.append(own_users_item)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = User.from_dict(users_item_data)

            users.append(users_item)

        all_users = d.pop("allUsers", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = UserGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = ProjectTeam.from_dict(teams_item_data)

            teams.append(teams_item)

        projects_count = d.pop("projectsCount", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        icon = d.pop("icon", UNSET)

        default_icon = d.pop("defaultIcon", UNSET)

        organization_roles = []
        _organization_roles = d.pop("organizationRoles", UNSET)
        for organization_roles_item_data in _organization_roles or []:
            organization_roles_item = OrganizationRole.from_dict(organization_roles_item_data)

            organization_roles.append(organization_roles_item)

        organization = cls(
            id=id,
            aliases=aliases,
            key=key,
            name=name,
            description=description,
            email_domain=email_domain,
            creation_time=creation_time,
            projects=projects,
            own_users=own_users,
            users=users,
            all_users=all_users,
            groups=groups,
            teams=teams,
            projects_count=projects_count,
            icon_url=icon_url,
            icon=icon,
            default_icon=default_icon,
            organization_roles=organization_roles,
        )

        organization.additional_properties = d
        return organization

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
