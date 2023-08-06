from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Bcryptpassword")


try:
    from ..models import password
except ImportError:
    import sys

    password = sys.modules[__package__ + "password"]


@attr.s(auto_attribs=True)
class Bcryptpassword(password.Password):
    """ """

    hashed_value: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        hashed_value = self.hashed_value

        field_dict: Dict[str, Any] = {}
        _Password_dict = super().to_dict()
        field_dict.update(_Password_dict)
        field_dict.update({})
        if hashed_value is not UNSET:
            field_dict["hashedValue"] = hashed_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        hashed_value = d.pop("hashedValue", UNSET)

        bcryptpassword = cls(
            hashed_value=hashed_value,
        )

        return bcryptpassword
