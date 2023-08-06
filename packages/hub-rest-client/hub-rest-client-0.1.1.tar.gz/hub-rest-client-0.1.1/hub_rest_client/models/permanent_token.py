from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authority_holder import AuthorityHolder
    from ..models.service import Service
    from ..models.user import User
else:
    AuthorityHolder = "AuthorityHolder"
    Service = "Service"
    User = "User"


T = TypeVar("T", bound="PermanentToken")


@attr.s(auto_attribs=True)
class PermanentToken:
    """ """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    scope: Union[Unset, List[Service]] = UNSET
    user: Union[Unset, User] = UNSET
    author: Union[Unset, AuthorityHolder] = UNSET
    creation_time: Union[Unset, int] = UNSET
    last_access_time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        token = self.token
        scope: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.scope, Unset):
            scope = []
            for scope_item_data in self.scope:
                scope_item = scope_item_data.to_dict()

                scope.append(scope_item)

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        creation_time = self.creation_time
        last_access_time = self.last_access_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if token is not UNSET:
            field_dict["token"] = token
        if scope is not UNSET:
            field_dict["scope"] = scope
        if user is not UNSET:
            field_dict["user"] = user
        if author is not UNSET:
            field_dict["author"] = author
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if last_access_time is not UNSET:
            field_dict["lastAccessTime"] = last_access_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        token = d.pop("token", UNSET)

        scope = []
        _scope = d.pop("scope", UNSET)
        for scope_item_data in _scope or []:
            scope_item = Service.from_dict(scope_item_data)

            scope.append(scope_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        _author = d.pop("author", UNSET)
        author: Union[Unset, AuthorityHolder]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = AuthorityHolder.from_dict(_author)

        creation_time = d.pop("creationTime", UNSET)

        last_access_time = d.pop("lastAccessTime", UNSET)

        permanent_token = cls(
            id=id,
            name=name,
            token=token,
            scope=scope,
            user=user,
            author=author,
            creation_time=creation_time,
            last_access_time=last_access_time,
        )

        permanent_token.additional_properties = d
        return permanent_token

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
