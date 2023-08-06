from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_module_custom_attribute_mapping import AuthModuleCustomAttributeMapping
else:
    AuthModuleCustomAttributeMapping = "AuthModuleCustomAttributeMapping"

from ..models.base_page import BasePage

T = TypeVar("T", bound="CustomattributemappingsPage")


@attr.s(auto_attribs=True)
class CustomattributemappingsPage(BasePage):
    """ """

    customattributemappings: Union[Unset, List[AuthModuleCustomAttributeMapping]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customattributemappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.customattributemappings, Unset):
            customattributemappings = []
            for customattributemappings_item_data in self.customattributemappings:
                customattributemappings_item = customattributemappings_item_data.to_dict()

                customattributemappings.append(customattributemappings_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customattributemappings is not UNSET:
            field_dict["customattributemappings"] = customattributemappings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        customattributemappings = []
        _customattributemappings = d.pop("customattributemappings", UNSET)
        for customattributemappings_item_data in _customattributemappings or []:
            customattributemappings_item = AuthModuleCustomAttributeMapping.from_dict(customattributemappings_item_data)

            customattributemappings.append(customattributemappings_item)

        customattributemappings_page = cls(
            customattributemappings=customattributemappings,
            **_BasePage_kwargs,
        )

        customattributemappings_page.additional_properties = d
        return customattributemappings_page

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
