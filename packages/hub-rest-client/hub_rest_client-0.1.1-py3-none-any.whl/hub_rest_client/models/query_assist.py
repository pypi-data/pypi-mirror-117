from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_style_range import QueryStyleRange
    from ..models.query_suggest_item import QuerySuggestItem
else:
    QueryStyleRange = "QueryStyleRange"
    QuerySuggestItem = "QuerySuggestItem"


T = TypeVar("T", bound="QueryAssist")


@attr.s(auto_attribs=True)
class QueryAssist:
    """ """

    query: Union[Unset, str] = UNSET
    caret: Union[Unset, int] = UNSET
    style_ranges: Union[Unset, List[QueryStyleRange]] = UNSET
    suggestions: Union[Unset, List[QuerySuggestItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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
        d = src_dict.copy()

        query = d.pop("query", UNSET)

        caret = d.pop("caret", UNSET)

        style_ranges = []
        _style_ranges = d.pop("styleRanges", UNSET)
        for style_ranges_item_data in _style_ranges or []:
            style_ranges_item = QueryStyleRange.from_dict(style_ranges_item_data)

            style_ranges.append(style_ranges_item)

        suggestions = []
        _suggestions = d.pop("suggestions", UNSET)
        for suggestions_item_data in _suggestions or []:
            suggestions_item = QuerySuggestItem.from_dict(suggestions_item_data)

            suggestions.append(suggestions_item)

        query_assist = cls(
            query=query,
            caret=caret,
            style_ranges=style_ranges,
            suggestions=suggestions,
        )

        query_assist.additional_properties = d
        return query_assist

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
