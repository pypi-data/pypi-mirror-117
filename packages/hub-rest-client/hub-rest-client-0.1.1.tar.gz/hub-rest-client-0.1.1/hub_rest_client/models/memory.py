from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Memory")


@attr.s(auto_attribs=True)
class Memory:
    """ """

    available: Union[Unset, int] = UNSET
    allocated: Union[Unset, int] = UNSET
    used: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available = self.available
        allocated = self.allocated
        used = self.used

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        memory.additional_properties = d
        return memory

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
