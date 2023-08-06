from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Password")


@attr.s(auto_attribs=True)
class Password:
    """ """

    type: "str"
    old_value: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        old_value = self.old_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if old_value is not UNSET:
            field_dict["oldValue"] = old_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        type = d.pop("type")

        old_value = d.pop("oldValue", UNSET)

        password = cls(
            type=type,
            old_value=old_value,
        )

        return password
