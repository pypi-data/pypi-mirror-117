from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hub_feature import HubFeature
else:
    HubFeature = "HubFeature"

from ..models.base_page import BasePage

T = TypeVar("T", bound="HubfeaturesPage")


@attr.s(auto_attribs=True)
class HubfeaturesPage(BasePage):
    """ """

    hubfeatures: Union[Unset, List[HubFeature]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hubfeatures: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hubfeatures, Unset):
            hubfeatures = []
            for hubfeatures_item_data in self.hubfeatures:
                hubfeatures_item = hubfeatures_item_data.to_dict()

                hubfeatures.append(hubfeatures_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hubfeatures is not UNSET:
            field_dict["hubfeatures"] = hubfeatures

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        hubfeatures = []
        _hubfeatures = d.pop("hubfeatures", UNSET)
        for hubfeatures_item_data in _hubfeatures or []:
            hubfeatures_item = HubFeature.from_dict(hubfeatures_item_data)

            hubfeatures.append(hubfeatures_item)

        hubfeatures_page = cls(
            hubfeatures=hubfeatures,
            **_BasePage_kwargs,
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
