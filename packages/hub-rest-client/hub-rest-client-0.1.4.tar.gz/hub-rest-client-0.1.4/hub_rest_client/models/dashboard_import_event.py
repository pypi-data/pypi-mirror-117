from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardImportEvent")


@attr.s(auto_attribs=True)
class DashboardImportEvent:
    """ """

    message: "Union[Unset, str]" = UNSET
    path: "Union[Unset, str]" = UNSET
    severity: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        path = self.path
        severity = self.severity

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if path is not UNSET:
            field_dict["path"] = path
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        message = d.pop("message", UNSET)

        path = d.pop("path", UNSET)

        severity = d.pop("severity", UNSET)

        dashboard_import_event = cls(
            message=message,
            path=path,
            severity=severity,
        )

        return dashboard_import_event
