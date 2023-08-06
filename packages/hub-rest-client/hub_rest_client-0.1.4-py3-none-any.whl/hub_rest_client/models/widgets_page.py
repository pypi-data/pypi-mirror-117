from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WidgetsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class WidgetsPage(base_page.BasePage):
    """ """

    widgets: "Union[Unset, List[widget_m.Widget]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        widgets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.widgets, Unset):
            widgets = []
            for widgets_item_data in self.widgets:
                widgets_item = widgets_item_data.to_dict()

                widgets.append(widgets_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if widgets is not UNSET:
            field_dict["widgets"] = widgets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import widget as widget_m
        except ImportError:
            import sys

            widget_m = sys.modules[__package__ + "widget"]

        d = src_dict.copy()

        widgets = []
        _widgets = d.pop("widgets", UNSET)
        for widgets_item_data in _widgets or []:
            widgets_item = widget_m.Widget.from_dict(widgets_item_data)

            widgets.append(widgets_item)

        widgets_page = cls(
            widgets=widgets,
        )

        return widgets_page
