from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class EventsPage(base_page.BasePage):
    """ """

    events: "Union[Unset, List[event_m.Event]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()

                events.append(events_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import event as event_m
        except ImportError:
            import sys

            event_m = sys.modules[__package__ + "event"]

        d = src_dict.copy()

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = event_m.Event.from_dict(events_item_data)

            events.append(events_item)

        events_page = cls(
            events=events,
        )

        return events_page
