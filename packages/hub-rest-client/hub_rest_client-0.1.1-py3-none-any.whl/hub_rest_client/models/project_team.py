from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization import Organization
    from ..models.project import Project
    from ..models.user import User
    from ..models.user_group import UserGroup
else:
    Organization = "Organization"
    User = "User"
    UserGroup = "UserGroup"
    Project = "Project"

from ..models.authority_holder import AuthorityHolder

T = TypeVar("T", bound="ProjectTeam")


@attr.s(auto_attribs=True)
class ProjectTeam(AuthorityHolder):
    """ """

    groups: Union[Unset, List[UserGroup]] = UNSET
    users: Union[Unset, List[User]] = UNSET
    own_users: Union[Unset, List[User]] = UNSET
    project: Union[Unset, Project] = UNSET
    user_count: Union[Unset, int] = UNSET
    organizations: Union[Unset, List[Organization]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()

                groups.append(groups_item)

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

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        user_count = self.user_count
        organizations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()

                organizations.append(organizations_item)

        field_dict: Dict[str, Any] = {}
        _AuthorityHolder_dict = super(AuthorityHolder).to_dict()
        field_dict.update(_AuthorityHolder_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups
        if users is not UNSET:
            field_dict["users"] = users
        if own_users is not UNSET:
            field_dict["ownUsers"] = own_users
        if project is not UNSET:
            field_dict["project"] = project
        if user_count is not UNSET:
            field_dict["userCount"] = user_count
        if organizations is not UNSET:
            field_dict["organizations"] = organizations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _AuthorityHolder_kwargs = super(AuthorityHolder).from_dict(src_dict=d).to_dict()

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = UserGroup.from_dict(groups_item_data)

            groups.append(groups_item)

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

        _project = d.pop("project", UNSET)
        project: Union[Unset, Project]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)

        user_count = d.pop("userCount", UNSET)

        organizations = []
        _organizations = d.pop("organizations", UNSET)
        for organizations_item_data in _organizations or []:
            organizations_item = Organization.from_dict(organizations_item_data)

            organizations.append(organizations_item)

        project_team = cls(
            groups=groups,
            users=users,
            own_users=own_users,
            project=project,
            user_count=user_count,
            organizations=organizations,
            **_AuthorityHolder_kwargs,
        )

        project_team.additional_properties = d
        return project_team

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
