from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Change")


@attr.s(auto_attribs=True)
class Change:
    """ """

    type: "str"
    field_name: "Union[Unset, str]" = UNSET
    field_type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        field_name = self.field_name
        field_type = self.field_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        type = d.pop("type")

        field_name = d.pop("fieldName", UNSET)

        field_type = d.pop("fieldType", UNSET)

        change = cls(
            type=type,
            field_name=field_name,
            field_type=field_type,
        )

        return change
