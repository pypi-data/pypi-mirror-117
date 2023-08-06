from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HubfeaturesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class HubfeaturesPage(base_page.BasePage):
    """ """

    hubfeatures: "Union[Unset, List[hub_feature_m.HubFeature]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hubfeatures: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hubfeatures, Unset):
            hubfeatures = []
            for hubfeatures_item_data in self.hubfeatures:
                hubfeatures_item = hubfeatures_item_data.to_dict()

                hubfeatures.append(hubfeatures_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hubfeatures is not UNSET:
            field_dict["hubfeatures"] = hubfeatures

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import hub_feature as hub_feature_m
        except ImportError:
            import sys

            hub_feature_m = sys.modules[__package__ + "hub_feature"]

        d = src_dict.copy()

        hubfeatures = []
        _hubfeatures = d.pop("hubfeatures", UNSET)
        for hubfeatures_item_data in _hubfeatures or []:
            hubfeatures_item = hub_feature_m.HubFeature.from_dict(hubfeatures_item_data)

            hubfeatures.append(hubfeatures_item)

        hubfeatures_page = cls(
            hubfeatures=hubfeatures,
        )

        hubfeatures_page.additional_properties = d
        return hubfeatures_page

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
