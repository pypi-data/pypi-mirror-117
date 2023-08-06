from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Md5password")


try:
    from ..models import password
except ImportError:
    import sys

    password = sys.modules[__package__ + "password"]


@attr.s(auto_attribs=True)
class Md5password(password.Password):
    """ """

    hashed_value: "Union[Unset, str]" = UNSET
    salt: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        hashed_value = self.hashed_value
        salt = self.salt

        field_dict: Dict[str, Any] = {}
        _Password_dict = super().to_dict()
        field_dict.update(_Password_dict)
        field_dict.update({})
        if hashed_value is not UNSET:
            field_dict["hashedValue"] = hashed_value
        if salt is not UNSET:
            field_dict["salt"] = salt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        hashed_value = d.pop("hashedValue", UNSET)

        salt = d.pop("salt", UNSET)

        md_5_password = cls(
            hashed_value=hashed_value,
            salt=salt,
        )

        return md_5_password
