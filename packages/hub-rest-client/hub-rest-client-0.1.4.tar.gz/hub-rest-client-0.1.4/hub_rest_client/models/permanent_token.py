from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PermanentToken")


@attr.s(auto_attribs=True)
class PermanentToken:
    """ """

    id: "Union[Unset, str]" = UNSET
    name: "Union[Unset, str]" = UNSET
    token: "Union[Unset, str]" = UNSET
    scope: "Union[Unset, List[service_m.Service]]" = UNSET
    user: "Union[Unset, user_m.User]" = UNSET
    author: "Union[Unset, authority_holder_m.AuthorityHolder]" = UNSET
    creation_time: "Union[Unset, int]" = UNSET
    last_access_time: "Union[Unset, int]" = UNSET

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

        try:
            from ..models import authority_holder as authority_holder_m
            from ..models import service as service_m
            from ..models import user as user_m
        except ImportError:
            import sys

            authority_holder_m = sys.modules[__package__ + "authority_holder"]
            service_m = sys.modules[__package__ + "service"]
            user_m = sys.modules[__package__ + "user"]

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        token = d.pop("token", UNSET)

        scope = []
        _scope = d.pop("scope", UNSET)
        for scope_item_data in _scope or []:
            scope_item = service_m.Service.from_dict(scope_item_data)

            scope.append(scope_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, user_m.User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = user_m.User.from_dict(_user)

        _author = d.pop("author", UNSET)
        author: Union[Unset, authority_holder_m.AuthorityHolder]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = authority_holder_m.AuthorityHolder.from_dict(_author)

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

        return permanent_token
