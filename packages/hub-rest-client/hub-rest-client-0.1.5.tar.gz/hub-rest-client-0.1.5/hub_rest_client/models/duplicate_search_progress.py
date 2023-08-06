from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateSearchProgress")


@attr.s(auto_attribs=True)
class DuplicateSearchProgress:
    """ """

    phase: "Union[Unset, str]" = UNSET
    progress: "Union[Unset, int]" = UNSET
    total: "Union[Unset, int]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        phase = self.phase
        progress = self.progress
        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if phase is not UNSET:
            field_dict["phase"] = phase
        if progress is not UNSET:
            field_dict["progress"] = progress
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        phase = d.pop("phase", UNSET)

        progress = d.pop("progress", UNSET)

        total = d.pop("total", UNSET)

        duplicate_search_progress = cls(
            phase=phase,
            progress=progress,
            total=total,
        )

        return duplicate_search_progress
