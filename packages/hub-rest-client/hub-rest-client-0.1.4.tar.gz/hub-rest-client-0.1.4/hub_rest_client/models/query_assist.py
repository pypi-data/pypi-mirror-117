from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryAssist")


@attr.s(auto_attribs=True)
class QueryAssist:
    """ """

    query: "Union[Unset, str]" = UNSET
    caret: "Union[Unset, int]" = UNSET
    style_ranges: "Union[Unset, List[query_style_range_m.QueryStyleRange]]" = UNSET
    suggestions: "Union[Unset, List[query_suggest_item_m.QuerySuggestItem]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        query = self.query
        caret = self.caret
        style_ranges: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.style_ranges, Unset):
            style_ranges = []
            for style_ranges_item_data in self.style_ranges:
                style_ranges_item = style_ranges_item_data.to_dict()

                style_ranges.append(style_ranges_item)

        suggestions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.suggestions, Unset):
            suggestions = []
            for suggestions_item_data in self.suggestions:
                suggestions_item = suggestions_item_data.to_dict()

                suggestions.append(suggestions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if caret is not UNSET:
            field_dict["caret"] = caret
        if style_ranges is not UNSET:
            field_dict["styleRanges"] = style_ranges
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import query_style_range as query_style_range_m
            from ..models import query_suggest_item as query_suggest_item_m
        except ImportError:
            import sys

            query_style_range_m = sys.modules[__package__ + "query_style_range"]
            query_suggest_item_m = sys.modules[__package__ + "query_suggest_item"]

        d = src_dict.copy()

        query = d.pop("query", UNSET)

        caret = d.pop("caret", UNSET)

        style_ranges = []
        _style_ranges = d.pop("styleRanges", UNSET)
        for style_ranges_item_data in _style_ranges or []:
            style_ranges_item = query_style_range_m.QueryStyleRange.from_dict(style_ranges_item_data)

            style_ranges.append(style_ranges_item)

        suggestions = []
        _suggestions = d.pop("suggestions", UNSET)
        for suggestions_item_data in _suggestions or []:
            suggestions_item = query_suggest_item_m.QuerySuggestItem.from_dict(suggestions_item_data)

            suggestions.append(suggestions_item)

        query_assist = cls(
            query=query,
            caret=caret,
            style_ranges=style_ranges,
            suggestions=suggestions,
        )

        return query_assist
