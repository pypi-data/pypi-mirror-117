from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupData")


@attr.s(auto_attribs=True)
class BackupData:
    """ """

    name: "Union[Unset, str]" = UNSET
    timestamp: "Union[Unset, int]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        name = d.pop("name", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        backup_data = cls(
            name=name,
            timestamp=timestamp,
        )

        return backup_data
