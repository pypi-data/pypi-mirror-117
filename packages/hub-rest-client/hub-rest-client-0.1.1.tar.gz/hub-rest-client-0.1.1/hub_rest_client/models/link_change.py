from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_data import LinkData
else:
    LinkData = "LinkData"

from ..models.change import Change

T = TypeVar("T", bound="LinkChange")


@attr.s(auto_attribs=True)
class LinkChange(Change):
    """ """

    removed: Union[Unset, List[LinkData]] = UNSET
    added: Union[Unset, List[LinkData]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        _Change_dict = super(Change).to_dict()
        field_dict.update(_Change_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if removed is not UNSET:
            field_dict["removed"] = removed
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Change_kwargs = super(Change).from_dict(src_dict=d).to_dict()

        removed = []
        _removed = d.pop("removed", UNSET)
        for removed_item_data in _removed or []:
            removed_item = LinkData.from_dict(removed_item_data)

            removed.append(removed_item)

        added = []
        _added = d.pop("added", UNSET)
        for added_item_data in _added or []:
            added_item = LinkData.from_dict(added_item_data)

            added.append(added_item)

        link_change = cls(
            removed=removed,
            added=added,
            **_Change_kwargs,
        )

        link_change.additional_properties = d
        return link_change

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
