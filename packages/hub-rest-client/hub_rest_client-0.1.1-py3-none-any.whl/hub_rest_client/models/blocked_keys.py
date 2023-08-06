from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.blocked_key import BlockedKey
else:
    BlockedKey = "BlockedKey"


T = TypeVar("T", bound="BlockedKeys")


@attr.s(auto_attribs=True)
class BlockedKeys:
    """ """

    items: Union[Unset, List[BlockedKey]] = UNSET
    time_until_next_cooldown: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        time_until_next_cooldown = self.time_until_next_cooldown

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if time_until_next_cooldown is not UNSET:
            field_dict["timeUntilNextCooldown"] = time_until_next_cooldown

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = BlockedKey.from_dict(items_item_data)

            items.append(items_item)

        time_until_next_cooldown = d.pop("timeUntilNextCooldown", UNSET)

        blocked_keys = cls(
            items=items,
            time_until_next_cooldown=time_until_next_cooldown,
        )

        blocked_keys.additional_properties = d
        return blocked_keys

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
