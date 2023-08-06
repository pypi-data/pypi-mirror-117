from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewersPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class ViewersPage(base_page.BasePage):
    """ """

    viewers: "Union[Unset, List[authority_holder_m.AuthorityHolder]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        viewers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.viewers, Unset):
            viewers = []
            for viewers_item_data in self.viewers:
                viewers_item = viewers_item_data.to_dict()

                viewers.append(viewers_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if viewers is not UNSET:
            field_dict["viewers"] = viewers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import authority_holder as authority_holder_m
        except ImportError:
            import sys

            authority_holder_m = sys.modules[__package__ + "authority_holder"]

        d = src_dict.copy()

        viewers = []
        _viewers = d.pop("viewers", UNSET)
        for viewers_item_data in _viewers or []:
            viewers_item = authority_holder_m.AuthorityHolder.from_dict(viewers_item_data)

            viewers.append(viewers_item)

        viewers_page = cls(
            viewers=viewers,
        )

        viewers_page.additional_properties = d
        return viewers_page

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
