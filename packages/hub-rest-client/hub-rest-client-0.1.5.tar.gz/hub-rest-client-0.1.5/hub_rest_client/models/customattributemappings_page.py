from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomattributemappingsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class CustomattributemappingsPage(base_page.BasePage):
    """ """

    customattributemappings: "Union[Unset, List[auth_module_custom_attribute_mapping_m.AuthModuleCustomAttributeMapping]]" = (
        UNSET
    )

    def to_dict(self) -> Dict[str, Any]:
        customattributemappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.customattributemappings, Unset):
            customattributemappings = []
            for customattributemappings_item_data in self.customattributemappings:
                customattributemappings_item = customattributemappings_item_data.to_dict()

                customattributemappings.append(customattributemappings_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if customattributemappings is not UNSET:
            field_dict["customattributemappings"] = customattributemappings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import auth_module_custom_attribute_mapping as auth_module_custom_attribute_mapping_m
        except ImportError:
            import sys

            auth_module_custom_attribute_mapping_m = sys.modules[__package__ + "auth_module_custom_attribute_mapping"]

        d = src_dict.copy()

        _BasePage_kwargs = super().from_dict(src_dict=d).to_dict()
        _BasePage_kwargs.pop("$type")

        customattributemappings = []
        _customattributemappings = d.pop("customattributemappings", UNSET)
        for customattributemappings_item_data in _customattributemappings or []:
            customattributemappings_item = (
                auth_module_custom_attribute_mapping_m.AuthModuleCustomAttributeMapping.from_dict(
                    customattributemappings_item_data
                )
            )

            customattributemappings.append(customattributemappings_item)

        customattributemappings_page = cls(
            customattributemappings=customattributemappings,
            **_BasePage_kwargs,
        )

        return customattributemappings_page
