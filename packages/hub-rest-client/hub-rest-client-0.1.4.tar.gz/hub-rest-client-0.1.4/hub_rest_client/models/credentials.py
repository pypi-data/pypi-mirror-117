from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Credentials")


@attr.s(auto_attribs=True)
class Credentials:
    """ """

    username: "Union[Unset, str]" = UNSET
    password: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        credentials = cls(
            username=username,
            password=password,
        )

        return credentials
