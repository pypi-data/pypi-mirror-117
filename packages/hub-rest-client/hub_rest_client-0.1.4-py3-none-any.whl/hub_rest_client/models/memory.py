from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Memory")


@attr.s(auto_attribs=True)
class Memory:
    """ """

    available: "Union[Unset, int]" = UNSET
    allocated: "Union[Unset, int]" = UNSET
    used: "Union[Unset, int]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        available = self.available
        allocated = self.allocated
        used = self.used

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if available is not UNSET:
            field_dict["available"] = available
        if allocated is not UNSET:
            field_dict["allocated"] = allocated
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        available = d.pop("available", UNSET)

        allocated = d.pop("allocated", UNSET)

        used = d.pop("used", UNSET)

        memory = cls(
            available=available,
            allocated=allocated,
            used=used,
        )

        return memory
