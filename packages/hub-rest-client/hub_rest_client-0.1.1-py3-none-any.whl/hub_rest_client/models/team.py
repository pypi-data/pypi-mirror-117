from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role import Role
    from ..models.user import User
    from ..models.user_group import UserGroup
else:
    User = "User"
    Role = "Role"
    UserGroup = "UserGroup"


T = TypeVar("T", bound="Team")


@attr.s(auto_attribs=True)
class Team:
    """ """

    role: Union[Unset, Role] = UNSET
    users: Union[Unset, List[User]] = UNSET
    users_total: Union[Unset, int] = UNSET
    groups: Union[Unset, List[UserGroup]] = UNSET
    groups_total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()

                users.append(users_item)

        users_total = self.users_total
        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()

                groups.append(groups_item)

        groups_total = self.groups_total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if users is not UNSET:
            field_dict["users"] = users
        if users_total is not UNSET:
            field_dict["usersTotal"] = users_total
        if groups is not UNSET:
            field_dict["groups"] = groups
        if groups_total is not UNSET:
            field_dict["groupsTotal"] = groups_total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _role = d.pop("role", UNSET)
        role: Union[Unset, Role]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = Role.from_dict(_role)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = User.from_dict(users_item_data)

            users.append(users_item)

        users_total = d.pop("usersTotal", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = UserGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        groups_total = d.pop("groupsTotal", UNSET)

        team = cls(
            role=role,
            users=users,
            users_total=users_total,
            groups=groups,
            groups_total=groups_total,
        )

        team.additional_properties = d
        return team

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
