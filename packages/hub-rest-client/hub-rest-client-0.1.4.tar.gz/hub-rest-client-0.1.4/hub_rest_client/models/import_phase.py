from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportPhase")


@attr.s(auto_attribs=True)
class ImportPhase:
    """ """

    name: "Union[Unset, str]" = UNSET
    progress: "Union[Unset, int]" = UNSET
    message: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        progress = self.progress
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if progress is not UNSET:
            field_dict["progress"] = progress
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        name = d.pop("name", UNSET)

        progress = d.pop("progress", UNSET)

        message = d.pop("message", UNSET)

        import_phase = cls(
            name=name,
            progress=progress,
            message=message,
        )

        return import_phase
