from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alias import Alias
    from ..models.organization import Organization
    from ..models.project_role import ProjectRole
    from ..models.project_team import ProjectTeam
    from ..models.resource import Resource
    from ..models.user import User
else:
    Resource = "Resource"
    ProjectRole = "ProjectRole"
    Organization = "Organization"
    User = "User"
    ProjectTeam = "ProjectTeam"
    Alias = "Alias"


T = TypeVar("T", bound="Project")


@attr.s(auto_attribs=True)
class Project:
    """ """

    id: Union[Unset, str] = UNSET
    aliases: Union[Unset, List[Alias]] = UNSET
    key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    archived: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    creation_time: Union[Unset, int] = UNSET
    icon_url: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    default_icon: Union[Unset, bool] = UNSET
    resources: Union[Unset, List[Resource]] = UNSET
    project_roles: Union[Unset, List[ProjectRole]] = UNSET
    transitive_project_roles: Union[Unset, List[ProjectRole]] = UNSET
    my_favorite: Union[Unset, bool] = UNSET
    team: Union[Unset, ProjectTeam] = UNSET
    owner: Union[Unset, User] = UNSET
    global_: Union[Unset, bool] = UNSET
    dashboard: Union[Unset, str] = UNSET
    organization: Union[Unset, Organization] = UNSET
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
        archived = self.archived
        description = self.description
        creation_time = self.creation_time
        icon_url = self.icon_url
        icon = self.icon
        default_icon = self.default_icon
        resources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()

                resources.append(resources_item)

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

        my_favorite = self.my_favorite
        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        global_ = self.global_
        dashboard = self.dashboard
        organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

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
        if archived is not UNSET:
            field_dict["archived"] = archived
        if description is not UNSET:
            field_dict["description"] = description
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if icon is not UNSET:
            field_dict["icon"] = icon
        if default_icon is not UNSET:
            field_dict["defaultIcon"] = default_icon
        if resources is not UNSET:
            field_dict["resources"] = resources
        if project_roles is not UNSET:
            field_dict["projectRoles"] = project_roles
        if transitive_project_roles is not UNSET:
            field_dict["transitiveProjectRoles"] = transitive_project_roles
        if my_favorite is not UNSET:
            field_dict["myFavorite"] = my_favorite
        if team is not UNSET:
            field_dict["team"] = team
        if owner is not UNSET:
            field_dict["owner"] = owner
        if global_ is not UNSET:
            field_dict["global"] = global_
        if dashboard is not UNSET:
            field_dict["dashboard"] = dashboard
        if organization is not UNSET:
            field_dict["organization"] = organization

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

        archived = d.pop("archived", UNSET)

        description = d.pop("description", UNSET)

        creation_time = d.pop("creationTime", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        icon = d.pop("icon", UNSET)

        default_icon = d.pop("defaultIcon", UNSET)

        resources = []
        _resources = d.pop("resources", UNSET)
        for resources_item_data in _resources or []:
            resources_item = Resource.from_dict(resources_item_data)

            resources.append(resources_item)

        project_roles = []
        _project_roles = d.pop("projectRoles", UNSET)
        for project_roles_item_data in _project_roles or []:
            project_roles_item = ProjectRole.from_dict(project_roles_item_data)

            project_roles.append(project_roles_item)

        transitive_project_roles = []
        _transitive_project_roles = d.pop("transitiveProjectRoles", UNSET)
        for transitive_project_roles_item_data in _transitive_project_roles or []:
            transitive_project_roles_item = ProjectRole.from_dict(transitive_project_roles_item_data)

            transitive_project_roles.append(transitive_project_roles_item)

        my_favorite = d.pop("myFavorite", UNSET)

        _team = d.pop("team", UNSET)
        team: Union[Unset, ProjectTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = ProjectTeam.from_dict(_team)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, User]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = User.from_dict(_owner)

        global_ = d.pop("global", UNSET)

        dashboard = d.pop("dashboard", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, Organization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = Organization.from_dict(_organization)

        project = cls(
            id=id,
            aliases=aliases,
            key=key,
            name=name,
            archived=archived,
            description=description,
            creation_time=creation_time,
            icon_url=icon_url,
            icon=icon,
            default_icon=default_icon,
            resources=resources,
            project_roles=project_roles,
            transitive_project_roles=transitive_project_roles,
            my_favorite=my_favorite,
            team=team,
            owner=owner,
            global_=global_,
            dashboard=dashboard,
            organization=organization,
        )

        project.additional_properties = d
        return project

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
