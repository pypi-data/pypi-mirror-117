from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrimitiveChange")


try:
    from ..models import change
except ImportError:
    import sys

    change = sys.modules[__package__ + "change"]


@attr.s(auto_attribs=True)
class PrimitiveChange(change.Change):
    """ """

    old_value: "Union[Unset, str]" = UNSET
    new_value: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        old_value = self.old_value
        new_value = self.new_value

        field_dict: Dict[str, Any] = {}
        _Change_dict = super().to_dict()
        field_dict.update(_Change_dict)
        field_dict.update({})
        if old_value is not UNSET:
            field_dict["oldValue"] = old_value
        if new_value is not UNSET:
            field_dict["newValue"] = new_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        old_value = d.pop("oldValue", UNSET)

        new_value = d.pop("newValue", UNSET)

        primitive_change = cls(
            old_value=old_value,
            new_value=new_value,
        )

        return primitive_change
