from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BasePage")


@attr.s(auto_attribs=True)
class BasePage:
    """ """

    type: str
    skip: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    top: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        skip = self.skip
        total = self.total
        top = self.top

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        base_page.additional_properties = d
        return base_page

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
