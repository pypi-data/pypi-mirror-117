from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duplicate_user import DuplicateUser
else:
    DuplicateUser = "DuplicateUser"


T = TypeVar("T", bound="DuplicateUserCluster")


@attr.s(auto_attribs=True)
class DuplicateUserCluster:
    """ """

    login: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    jabber: Union[Unset, str] = UNSET
    banned: Union[Unset, bool] = UNSET
    users: Union[Unset, List[DuplicateUser]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login = self.login
        name = self.name
        email = self.email
        jabber = self.jabber
        banned = self.banned
        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()

                users.append(users_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if login is not UNSET:
            field_dict["login"] = login
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if jabber is not UNSET:
            field_dict["jabber"] = jabber
        if banned is not UNSET:
            field_dict["banned"] = banned
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        login = d.pop("login", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        jabber = d.pop("jabber", UNSET)

        banned = d.pop("banned", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = DuplicateUser.from_dict(users_item_data)

            users.append(users_item)

        duplicate_user_cluster = cls(
            login=login,
            name=name,
            email=email,
            jabber=jabber,
            banned=banned,
            users=users,
        )

        duplicate_user_cluster.additional_properties = d
        return duplicate_user_cluster

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
