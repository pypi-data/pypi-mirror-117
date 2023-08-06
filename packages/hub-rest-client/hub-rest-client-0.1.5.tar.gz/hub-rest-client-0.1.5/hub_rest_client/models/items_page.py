from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class ItemsPage(base_page.BasePage):
    """ """

    items: "Union[Unset, List[dashboard_m.Dashboard]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import dashboard as dashboard_m
        except ImportError:
            import sys

            dashboard_m = sys.modules[__package__ + "dashboard"]

        d = src_dict.copy()

        _BasePage_kwargs = super().from_dict(src_dict=d).to_dict()
        _BasePage_kwargs.pop("$type")

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = dashboard_m.Dashboard.from_dict(items_item_data)

            items.append(items_item)

        items_page = cls(
            items=items,
            **_BasePage_kwargs,
        )

        return items_page
