from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyStoreData")


@attr.s(auto_attribs=True)
class KeyStoreData:
    """ """

    bytes_: "Union[Unset, str]" = UNSET
    password: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        bytes_ = self.bytes_
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        bytes_ = d.pop("bytes", UNSET)

        password = d.pop("password", UNSET)

        key_store_data = cls(
            bytes_=bytes_,
            password=password,
        )

        return key_store_data
