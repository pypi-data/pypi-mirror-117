from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Resolution")


@attr.s(auto_attribs=True)
class Resolution:
    """ """

    type: "Union[Unset, str]" = UNSET
    property_overrides: "Union[Unset, info_m.Info]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        property_overrides: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.property_overrides, Unset):
            property_overrides = self.property_overrides.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if property_overrides is not UNSET:
            field_dict["propertyOverrides"] = property_overrides

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import info as info_m
        except ImportError:
            import sys

            info_m = sys.modules[__package__ + "info"]

        d = src_dict.copy()

        type = d.pop("type", UNSET)

        _property_overrides = d.pop("propertyOverrides", UNSET)
        property_overrides: Union[Unset, info_m.Info]
        if isinstance(_property_overrides, Unset):
            property_overrides = UNSET
        else:
            property_overrides = info_m.Info.from_dict(_property_overrides)

        resolution = cls(
            type=type,
            property_overrides=property_overrides,
        )

        return resolution
