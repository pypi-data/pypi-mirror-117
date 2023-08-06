from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardImportResult")


@attr.s(auto_attribs=True)
class DashboardImportResult:
    """ """

    success: "Union[Unset, bool]" = UNSET
    events: "Union[Unset, List[dashboard_import_event_m.DashboardImportEvent]]" = UNSET
    missing: "Union[Unset, List[dashboard_import_missing_entity_m.DashboardImportMissingEntity]]" = UNSET

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

        try:
            from ..models import dashboard_import_event as dashboard_import_event_m
            from ..models import dashboard_import_missing_entity as dashboard_import_missing_entity_m
        except ImportError:
            import sys

            dashboard_import_missing_entity_m = sys.modules[__package__ + "dashboard_import_missing_entity"]
            dashboard_import_event_m = sys.modules[__package__ + "dashboard_import_event"]

        d = src_dict.copy()

        success = d.pop("success", UNSET)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = dashboard_import_event_m.DashboardImportEvent.from_dict(events_item_data)

            events.append(events_item)

        missing = []
        _missing = d.pop("missing", UNSET)
        for missing_item_data in _missing or []:
            missing_item = dashboard_import_missing_entity_m.DashboardImportMissingEntity.from_dict(missing_item_data)

            missing.append(missing_item)

        dashboard_import_result = cls(
            success=success,
            events=events,
            missing=missing,
        )

        return dashboard_import_result
