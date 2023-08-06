from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovedScope")


@attr.s(auto_attribs=True)
class ApprovedScope:
    """ """

    id: "Union[Unset, str]" = UNSET
    client: "Union[Unset, service_m.Service]" = UNSET
    scope: "Union[Unset, List[service_m.Service]]" = UNSET
    user: "Union[Unset, user_m.User]" = UNSET
    expires_on: "Union[Unset, int]" = UNSET

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

        expires_on = self.expires_on

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if client is not UNSET:
            field_dict["client"] = client
        if scope is not UNSET:
            field_dict["scope"] = scope
        if user is not UNSET:
            field_dict["user"] = user
        if expires_on is not UNSET:
            field_dict["expiresOn"] = expires_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import service as service_m
            from ..models import user as user_m
        except ImportError:
            import sys

            service_m = sys.modules[__package__ + "service"]
            user_m = sys.modules[__package__ + "user"]

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        _client = d.pop("client", UNSET)
        client: Union[Unset, service_m.Service]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = service_m.Service.from_dict(_client)

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

        expires_on = d.pop("expiresOn", UNSET)

        approved_scope = cls(
            id=id,
            client=client,
            scope=scope,
            user=user,
            expires_on=expires_on,
        )

        return approved_scope
