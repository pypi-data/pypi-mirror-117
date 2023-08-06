from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.change import Change
from ..types import UNSET, Unset

T = TypeVar("T", bound="PrimitiveChange")


@attr.s(auto_attribs=True)
class PrimitiveChange(Change):
    """ """

    old_value: Union[Unset, str] = UNSET
    new_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        old_value = self.old_value
        new_value = self.new_value

        field_dict: Dict[str, Any] = {}
        _Change_dict = super(Change).to_dict()
        field_dict.update(_Change_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if old_value is not UNSET:
            field_dict["oldValue"] = old_value
        if new_value is not UNSET:
            field_dict["newValue"] = new_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Change_kwargs = super(Change).from_dict(src_dict=d).to_dict()

        old_value = d.pop("oldValue", UNSET)

        new_value = d.pop("newValue", UNSET)

        primitive_change = cls(
            old_value=old_value,
            new_value=new_value,
            **_Change_kwargs,
        )

        primitive_change.additional_properties = d
        return primitive_change

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
