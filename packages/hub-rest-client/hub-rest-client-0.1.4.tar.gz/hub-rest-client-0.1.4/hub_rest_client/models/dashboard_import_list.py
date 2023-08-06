from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardImportList")


@attr.s(auto_attribs=True)
class DashboardImportList:
    """ """

    items: "Union[Unset, List[dashboard_import_m.DashboardImport]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import dashboard_import as dashboard_import_m
        except ImportError:
            import sys

            dashboard_import_m = sys.modules[__package__ + "dashboard_import"]

        d = src_dict.copy()

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = dashboard_import_m.DashboardImport.from_dict(items_item_data)

            items.append(items_item)

        dashboard_import_list = cls(
            items=items,
        )

        return dashboard_import_list
