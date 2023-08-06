from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuerySuggestItem")


@attr.s(auto_attribs=True)
class QuerySuggestItem:
    """ """

    prefix: "Union[Unset, str]" = UNSET
    option: "Union[Unset, str]" = UNSET
    suffix: "Union[Unset, str]" = UNSET
    description: "Union[Unset, str]" = UNSET
    matching_start: "Union[Unset, int]" = UNSET
    matching_end: "Union[Unset, int]" = UNSET
    caret: "Union[Unset, int]" = UNSET
    completion_start: "Union[Unset, int]" = UNSET
    completion_end: "Union[Unset, int]" = UNSET
    group: "Union[Unset, str]" = UNSET
    icon: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        prefix = self.prefix
        option = self.option
        suffix = self.suffix
        description = self.description
        matching_start = self.matching_start
        matching_end = self.matching_end
        caret = self.caret
        completion_start = self.completion_start
        completion_end = self.completion_end
        group = self.group
        icon = self.icon

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if option is not UNSET:
            field_dict["option"] = option
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if description is not UNSET:
            field_dict["description"] = description
        if matching_start is not UNSET:
            field_dict["matchingStart"] = matching_start
        if matching_end is not UNSET:
            field_dict["matchingEnd"] = matching_end
        if caret is not UNSET:
            field_dict["caret"] = caret
        if completion_start is not UNSET:
            field_dict["completionStart"] = completion_start
        if completion_end is not UNSET:
            field_dict["completionEnd"] = completion_end
        if group is not UNSET:
            field_dict["group"] = group
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        prefix = d.pop("prefix", UNSET)

        option = d.pop("option", UNSET)

        suffix = d.pop("suffix", UNSET)

        description = d.pop("description", UNSET)

        matching_start = d.pop("matchingStart", UNSET)

        matching_end = d.pop("matchingEnd", UNSET)

        caret = d.pop("caret", UNSET)

        completion_start = d.pop("completionStart", UNSET)

        completion_end = d.pop("completionEnd", UNSET)

        group = d.pop("group", UNSET)

        icon = d.pop("icon", UNSET)

        query_suggest_item = cls(
            prefix=prefix,
            option=option,
            suffix=suffix,
            description=description,
            matching_start=matching_start,
            matching_end=matching_end,
            caret=caret,
            completion_start=completion_start,
            completion_end=completion_end,
            group=group,
            icon=icon,
        )

        return query_suggest_item
