from typing import Any, Dict, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenInfo")


@attr.s(auto_attribs=True)
class TokenInfo:
    """ """

    id: "Union[Unset, str]" = UNSET
    client: "Union[Unset, str]" = UNSET
    user: "Union[Unset, str]" = UNSET
    scope: "Union[Unset, List[str]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        client = self.client
        user = self.user
        scope: Union[Unset, List[str]] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if client is not UNSET:
            field_dict["client"] = client
        if user is not UNSET:
            field_dict["user"] = user
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        client = d.pop("client", UNSET)

        user = d.pop("user", UNSET)

        scope = cast(List[str], d.pop("scope", UNSET))

        token_info = cls(
            id=id,
            client=client,
            user=user,
            scope=scope,
        )

        return token_info
