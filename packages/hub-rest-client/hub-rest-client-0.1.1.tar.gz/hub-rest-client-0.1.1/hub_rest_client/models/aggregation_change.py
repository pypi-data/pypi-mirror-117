from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.change import Change
else:
    Change = "Change"

from ..models.change import Change

T = TypeVar("T", bound="AggregationChange")


@attr.s(auto_attribs=True)
class AggregationChange(Change):
    """ """

    child_changes: Union[Unset, List[Change]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        child_changes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.child_changes, Unset):
            child_changes = []
            for child_changes_item_data in self.child_changes:
                child_changes_item = child_changes_item_data.to_dict()

                child_changes.append(child_changes_item)

        field_dict: Dict[str, Any] = {}
        _Change_dict = super(Change).to_dict()
        field_dict.update(_Change_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if child_changes is not UNSET:
            field_dict["childChanges"] = child_changes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Change_kwargs = super(Change).from_dict(src_dict=d).to_dict()

        child_changes = []
        _child_changes = d.pop("childChanges", UNSET)
        for child_changes_item_data in _child_changes or []:
            child_changes_item = Change.from_dict(child_changes_item_data)

            child_changes.append(child_changes_item)

        aggregation_change = cls(
            child_changes=child_changes,
            **_Change_kwargs,
        )

        aggregation_change.additional_properties = d
        return aggregation_change

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
