from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkChange")


try:
    from ..models import change
except ImportError:
    import sys

    change = sys.modules[__package__ + "change"]


@attr.s(auto_attribs=True)
class LinkChange(change.Change):
    """ """

    removed: "Union[Unset, List[link_data_m.LinkData]]" = UNSET
    added: "Union[Unset, List[link_data_m.LinkData]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        removed: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.removed, Unset):
            removed = []
            for removed_item_data in self.removed:
                removed_item = removed_item_data.to_dict()

                removed.append(removed_item)

        added: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.added, Unset):
            added = []
            for added_item_data in self.added:
                added_item = added_item_data.to_dict()

                added.append(added_item)

        field_dict: Dict[str, Any] = {}
        _Change_dict = super().to_dict()
        field_dict.update(_Change_dict)
        field_dict.update({})
        if removed is not UNSET:
            field_dict["removed"] = removed
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import link_data as link_data_m
        except ImportError:
            import sys

            link_data_m = sys.modules[__package__ + "link_data"]

        d = src_dict.copy()

        removed = []
        _removed = d.pop("removed", UNSET)
        for removed_item_data in _removed or []:
            removed_item = link_data_m.LinkData.from_dict(removed_item_data)

            removed.append(removed_item)

        added = []
        _added = d.pop("added", UNSET)
        for added_item_data in _added or []:
            added_item = link_data_m.LinkData.from_dict(added_item_data)

            added.append(added_item)

        link_change = cls(
            removed=removed,
            added=added,
        )

        return link_change
