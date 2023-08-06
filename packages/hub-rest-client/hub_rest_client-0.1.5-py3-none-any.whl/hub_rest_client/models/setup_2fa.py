from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Setup2FA")


@attr.s(auto_attribs=True)
class Setup2FA:
    """ """

    confirm: "Union[Unset, bool]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        confirm = self.confirm

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if confirm is not UNSET:
            field_dict["confirm"] = confirm

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        confirm = d.pop("confirm", UNSET)

        setup_2fa = cls(
            confirm=confirm,
        )

        return setup_2fa
