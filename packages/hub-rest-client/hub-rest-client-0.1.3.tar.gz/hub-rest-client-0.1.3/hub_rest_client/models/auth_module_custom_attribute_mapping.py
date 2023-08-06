from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthModuleCustomAttributeMapping")


@attr.s(auto_attribs=True)
class AuthModuleCustomAttributeMapping:
    """ """

    mapping: "Union[Unset, str]" = UNSET
    attribute_prototype: "Union[Unset, profile_attribute_prototype_m.ProfileAttributePrototype]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mapping = self.mapping
        attribute_prototype: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attribute_prototype, Unset):
            attribute_prototype = self.attribute_prototype.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mapping is not UNSET:
            field_dict["mapping"] = mapping
        if attribute_prototype is not UNSET:
            field_dict["attributePrototype"] = attribute_prototype

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import profile_attribute_prototype as profile_attribute_prototype_m
        except ImportError:
            import sys

            profile_attribute_prototype_m = sys.modules[__package__ + "profile_attribute_prototype"]

        d = src_dict.copy()

        mapping = d.pop("mapping", UNSET)

        _attribute_prototype = d.pop("attributePrototype", UNSET)
        attribute_prototype: Union[Unset, profile_attribute_prototype_m.ProfileAttributePrototype]
        if isinstance(_attribute_prototype, Unset):
            attribute_prototype = UNSET
        else:
            attribute_prototype = profile_attribute_prototype_m.ProfileAttributePrototype.from_dict(
                _attribute_prototype
            )

        auth_module_custom_attribute_mapping = cls(
            mapping=mapping,
            attribute_prototype=attribute_prototype,
        )

        auth_module_custom_attribute_mapping.additional_properties = d
        return auth_module_custom_attribute_mapping

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
