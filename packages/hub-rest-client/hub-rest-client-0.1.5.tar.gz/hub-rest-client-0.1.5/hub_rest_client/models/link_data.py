from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkData")


@attr.s(auto_attribs=True)
class LinkData:
    """ """

    id: "Union[Unset, str]" = UNSET
    presentation: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        presentation = self.presentation

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if presentation is not UNSET:
            field_dict["presentation"] = presentation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        presentation = d.pop("presentation", UNSET)

        link_data = cls(
            id=id,
            presentation=presentation,
        )

        return link_data
