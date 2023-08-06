from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization import Organization
    from ..models.project import Project
    from ..models.project_team import ProjectTeam
    from ..models.user import User
else:
    ProjectTeam = "ProjectTeam"
    Organization = "Organization"
    User = "User"
    Project = "Project"

from ..models.authority_holder import AuthorityHolder

T = TypeVar("T", bound="UserGroup")


@attr.s(auto_attribs=True)
class UserGroup(AuthorityHolder):
    """ """

    description: Union[Unset, str] = UNSET
    icon_url: Union[Unset, str] = UNSET
    auto_join: Union[Unset, bool] = UNSET
    required_two_factor_authentication: Union[Unset, bool] = UNSET
    parents_require_two_factor_authentication: Union[Unset, bool] = UNSET
    users: Union[Unset, List[User]] = UNSET
    own_users: Union[Unset, List[User]] = UNSET
    user_count: Union[Unset, int] = UNSET
    parent: Union[Unset, T] = UNSET
    subgroups: Union[Unset, List[T]] = UNSET
    teams: Union[Unset, List[ProjectTeam]] = UNSET
    organizations: Union[Unset, List[Organization]] = UNSET
    project: Union[Unset, Project] = UNSET
    all_users: Union[Unset, bool] = UNSET
    implicit: Union[Unset, bool] = UNSET
    queried_singleton: Union[Unset, bool] = UNSET
    removable: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        icon_url = self.icon_url
        auto_join = self.auto_join
        required_two_factor_authentication = self.required_two_factor_authentication
        parents_require_two_factor_authentication = self.parents_require_two_factor_authentication
        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()

                users.append(users_item)

        own_users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.own_users, Unset):
            own_users = []
            for own_users_item_data in self.own_users:
                own_users_item = own_users_item_data.to_dict()

                own_users.append(own_users_item)

        user_count = self.user_count
        parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        subgroups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subgroups, Unset):
            subgroups = []
            for subgroups_item_data in self.subgroups:
                subgroups_item = subgroups_item_data.to_dict()

                subgroups.append(subgroups_item)

        teams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()

                teams.append(teams_item)

        organizations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()

                organizations.append(organizations_item)

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        all_users = self.all_users
        implicit = self.implicit
        queried_singleton = self.queried_singleton
        removable = self.removable

        field_dict: Dict[str, Any] = {}
        _AuthorityHolder_dict = super(AuthorityHolder).to_dict()
        field_dict.update(_AuthorityHolder_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if auto_join is not UNSET:
            field_dict["autoJoin"] = auto_join
        if required_two_factor_authentication is not UNSET:
            field_dict["requiredTwoFactorAuthentication"] = required_two_factor_authentication
        if parents_require_two_factor_authentication is not UNSET:
            field_dict["parentsRequireTwoFactorAuthentication"] = parents_require_two_factor_authentication
        if users is not UNSET:
            field_dict["users"] = users
        if own_users is not UNSET:
            field_dict["ownUsers"] = own_users
        if user_count is not UNSET:
            field_dict["userCount"] = user_count
        if parent is not UNSET:
            field_dict["parent"] = parent
        if subgroups is not UNSET:
            field_dict["subgroups"] = subgroups
        if teams is not UNSET:
            field_dict["teams"] = teams
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if project is not UNSET:
            field_dict["project"] = project
        if all_users is not UNSET:
            field_dict["allUsers"] = all_users
        if implicit is not UNSET:
            field_dict["implicit"] = implicit
        if queried_singleton is not UNSET:
            field_dict["queriedSingleton"] = queried_singleton
        if removable is not UNSET:
            field_dict["removable"] = removable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _AuthorityHolder_kwargs = super(AuthorityHolder).from_dict(src_dict=d).to_dict()

        description = d.pop("description", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        auto_join = d.pop("autoJoin", UNSET)

        required_two_factor_authentication = d.pop("requiredTwoFactorAuthentication", UNSET)

        parents_require_two_factor_authentication = d.pop("parentsRequireTwoFactorAuthentication", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = User.from_dict(users_item_data)

            users.append(users_item)

        own_users = []
        _own_users = d.pop("ownUsers", UNSET)
        for own_users_item_data in _own_users or []:
            own_users_item = User.from_dict(own_users_item_data)

            own_users.append(own_users_item)

        user_count = d.pop("userCount", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, UserGroup]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = UserGroup.from_dict(_parent)

        subgroups = []
        _subgroups = d.pop("subgroups", UNSET)
        for subgroups_item_data in _subgroups or []:
            subgroups_item = UserGroup.from_dict(subgroups_item_data)

            subgroups.append(subgroups_item)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = ProjectTeam.from_dict(teams_item_data)

            teams.append(teams_item)

        organizations = []
        _organizations = d.pop("organizations", UNSET)
        for organizations_item_data in _organizations or []:
            organizations_item = Organization.from_dict(organizations_item_data)

            organizations.append(organizations_item)

        _project = d.pop("project", UNSET)
        project: Union[Unset, Project]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)

        all_users = d.pop("allUsers", UNSET)

        implicit = d.pop("implicit", UNSET)

        queried_singleton = d.pop("queriedSingleton", UNSET)

        removable = d.pop("removable", UNSET)

        user_group = cls(
            description=description,
            icon_url=icon_url,
            auto_join=auto_join,
            required_two_factor_authentication=required_two_factor_authentication,
            parents_require_two_factor_authentication=parents_require_two_factor_authentication,
            users=users,
            own_users=own_users,
            user_count=user_count,
            parent=parent,
            subgroups=subgroups,
            teams=teams,
            organizations=organizations,
            project=project,
            all_users=all_users,
            implicit=implicit,
            queried_singleton=queried_singleton,
            removable=removable,
            **_AuthorityHolder_kwargs,
        )

        user_group.additional_properties = d
        return user_group

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
