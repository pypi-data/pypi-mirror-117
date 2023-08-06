from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AggregationChange")


try:
    from ..models import change
except ImportError:
    import sys

    change = sys.modules[__package__ + "change"]


@attr.s(auto_attribs=True)
class AggregationChange(change.Change):
    """ """

    child_changes: "Union[Unset, List[change_m.Change]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        child_changes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.child_changes, Unset):
            child_changes = []
            for child_changes_item_data in self.child_changes:
                child_changes_item = child_changes_item_data.to_dict()

                child_changes.append(child_changes_item)

        field_dict: Dict[str, Any] = {}
        _Change_dict = super().to_dict()
        field_dict.update(_Change_dict)
        field_dict.update({})
        if child_changes is not UNSET:
            field_dict["childChanges"] = child_changes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import change as change_m
        except ImportError:
            import sys

            change_m = sys.modules[__package__ + "change"]

        d = src_dict.copy()

        child_changes = []
        _child_changes = d.pop("childChanges", UNSET)
        for child_changes_item_data in _child_changes or []:
            child_changes_item = change_m.Change.from_dict(child_changes_item_data)

            child_changes.append(child_changes_item)

        aggregation_change = cls(
            child_changes=child_changes,
        )

        return aggregation_change
