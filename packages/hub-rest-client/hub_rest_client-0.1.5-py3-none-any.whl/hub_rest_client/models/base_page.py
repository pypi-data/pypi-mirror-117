from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BasePage")


@attr.s(auto_attribs=True)
class BasePage:
    """ """

    type: "str"
    skip: "Union[Unset, int]" = UNSET
    total: "Union[Unset, int]" = UNSET
    top: "Union[Unset, int]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        skip = self.skip
        total = self.total
        top = self.top

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if skip is not UNSET:
            field_dict["skip"] = skip
        if total is not UNSET:
            field_dict["total"] = total
        if top is not UNSET:
            field_dict["top"] = top

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        type = d.pop("type")

        skip = d.pop("skip", UNSET)

        total = d.pop("total", UNSET)

        top = d.pop("top", UNSET)

        base_page = cls(
            type=type,
            skip=skip,
            total=total,
            top=top,
        )

        return base_page
