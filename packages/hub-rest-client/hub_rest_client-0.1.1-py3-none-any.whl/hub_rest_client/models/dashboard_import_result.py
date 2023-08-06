from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_import_event import DashboardImportEvent
    from ..models.dashboard_import_missing_entity import DashboardImportMissingEntity
else:
    DashboardImportMissingEntity = "DashboardImportMissingEntity"
    DashboardImportEvent = "DashboardImportEvent"


T = TypeVar("T", bound="DashboardImportResult")


@attr.s(auto_attribs=True)
class DashboardImportResult:
    """ """

    success: Union[Unset, bool] = UNSET
    events: Union[Unset, List[DashboardImportEvent]] = UNSET
    missing: Union[Unset, List[DashboardImportMissingEntity]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success
        events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()

                events.append(events_item)

        missing: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.missing, Unset):
            missing = []
            for missing_item_data in self.missing:
                missing_item = missing_item_data.to_dict()

                missing.append(missing_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if events is not UNSET:
            field_dict["events"] = events
        if missing is not UNSET:
            field_dict["missing"] = missing

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        success = d.pop("success", UNSET)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = DashboardImportEvent.from_dict(events_item_data)

            events.append(events_item)

        missing = []
        _missing = d.pop("missing", UNSET)
        for missing_item_data in _missing or []:
            missing_item = DashboardImportMissingEntity.from_dict(missing_item_data)

            missing.append(missing_item)

        dashboard_import_result = cls(
            success=success,
            events=events,
            missing=missing,
        )

        dashboard_import_result.additional_properties = d
        return dashboard_import_result

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
