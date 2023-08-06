from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryStyleRange")


@attr.s(auto_attribs=True)
class QueryStyleRange:
    """ """

    start: "Union[Unset, int]" = UNSET
    length: "Union[Unset, int]" = UNSET
    style: "Union[Unset, str]" = UNSET
    title: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        start = self.start
        length = self.length
        style = self.style
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if start is not UNSET:
            field_dict["start"] = start
        if length is not UNSET:
            field_dict["length"] = length
        if style is not UNSET:
            field_dict["style"] = style
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        start = d.pop("start", UNSET)

        length = d.pop("length", UNSET)

        style = d.pop("style", UNSET)

        title = d.pop("title", UNSET)

        query_style_range = cls(
            start=start,
            length=length,
            style=style,
            title=title,
        )

        return query_style_range
