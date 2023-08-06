from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.info import Info
else:
    Info = "Info"


T = TypeVar("T", bound="Resolution")


@attr.s(auto_attribs=True)
class Resolution:
    """ """

    type: Union[Unset, str] = UNSET
    property_overrides: Union[Unset, Info] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        property_overrides: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.property_overrides, Unset):
            property_overrides = self.property_overrides.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if property_overrides is not UNSET:
            field_dict["propertyOverrides"] = property_overrides

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        type = d.pop("type", UNSET)

        _property_overrides = d.pop("propertyOverrides", UNSET)
        property_overrides: Union[Unset, Info]
        if isinstance(_property_overrides, Unset):
            property_overrides = UNSET
        else:
            property_overrides = Info.from_dict(_property_overrides)

        resolution = cls(
            type=type,
            property_overrides=property_overrides,
        )

        resolution.additional_properties = d
        return resolution

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
