from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Team")


@attr.s(auto_attribs=True)
class Team:
    """ """

    role: "Union[Unset, role_m.Role]" = UNSET
    users: "Union[Unset, List[user_m.User]]" = UNSET
    users_total: "Union[Unset, int]" = UNSET
    groups: "Union[Unset, List[user_group_m.UserGroup]]" = UNSET
    groups_total: "Union[Unset, int]" = UNSET

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

        try:
            from ..models import role as role_m
            from ..models import user as user_m
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            user_group_m = sys.modules[__package__ + "user_group"]
            role_m = sys.modules[__package__ + "role"]
            user_m = sys.modules[__package__ + "user"]

        d = src_dict.copy()

        _role = d.pop("role", UNSET)
        role: Union[Unset, role_m.Role]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = role_m.Role.from_dict(_role)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = user_m.User.from_dict(users_item_data)

            users.append(users_item)

        users_total = d.pop("usersTotal", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = user_group_m.UserGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        groups_total = d.pop("groupsTotal", UNSET)

        team = cls(
            role=role,
            users=users,
            users_total=users_total,
            groups=groups,
            groups_total=groups_total,
        )

        return team
