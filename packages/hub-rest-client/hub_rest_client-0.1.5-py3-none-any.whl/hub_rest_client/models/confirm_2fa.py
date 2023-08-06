from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Confirm2FA")


@attr.s(auto_attribs=True)
class Confirm2FA:
    """ """

    code: "Union[Unset, int]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        code = d.pop("code", UNSET)

        confirm_2fa = cls(
            code=code,
        )

        return confirm_2fa
