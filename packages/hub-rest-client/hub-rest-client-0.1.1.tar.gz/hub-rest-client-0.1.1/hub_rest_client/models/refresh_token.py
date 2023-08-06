from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service import Service
    from ..models.user import User
else:
    Service = "Service"
    User = "User"


T = TypeVar("T", bound="RefreshToken")


@attr.s(auto_attribs=True)
class RefreshToken:
    """ """

    id: Union[Unset, str] = UNSET
    client: Union[Unset, Service] = UNSET
    scope: Union[Unset, List[Service]] = UNSET
    user: Union[Unset, User] = UNSET
    creation_time: Union[Unset, int] = UNSET
    last_access_time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        scope: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.scope, Unset):
            scope = []
            for scope_item_data in self.scope:
                scope_item = scope_item_data.to_dict()

                scope.append(scope_item)

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        creation_time = self.creation_time
        last_access_time = self.last_access_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if client is not UNSET:
            field_dict["client"] = client
        if scope is not UNSET:
            field_dict["scope"] = scope
        if user is not UNSET:
            field_dict["user"] = user
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if last_access_time is not UNSET:
            field_dict["lastAccessTime"] = last_access_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        id = d.pop("id", UNSET)

        _client = d.pop("client", UNSET)
        client: Union[Unset, Service]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = Service.from_dict(_client)

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

        creation_time = d.pop("creationTime", UNSET)

        last_access_time = d.pop("lastAccessTime", UNSET)

        refresh_token = cls(
            id=id,
            client=client,
            scope=scope,
            user=user,
            creation_time=creation_time,
            last_access_time=last_access_time,
        )

        refresh_token.additional_properties = d
        return refresh_token

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
