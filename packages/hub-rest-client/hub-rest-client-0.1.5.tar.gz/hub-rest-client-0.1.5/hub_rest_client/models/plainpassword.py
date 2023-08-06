from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Plainpassword")


try:
    from ..models import password
except ImportError:
    import sys

    password = sys.modules[__package__ + "password"]


@attr.s(auto_attribs=True)
class Plainpassword(password.Password):
    """ """

    value: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        field_dict: Dict[str, Any] = {}
        _Password_dict = super().to_dict()
        field_dict.update(_Password_dict)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _Password_kwargs = super().from_dict(src_dict=d).to_dict()
        _Password_kwargs.pop("$type")

        value = d.pop("value", UNSET)

        plainpassword = cls(
            value=value,
            **_Password_kwargs,
        )

        return plainpassword
