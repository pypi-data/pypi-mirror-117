from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessGrantOptionList")


@attr.s(auto_attribs=True)
class AccessGrantOptionList:
    """ """

    has_already: "Union[Unset, bool]" = UNSET
    options: "Union[Unset, List[access_grant_option_m.AccessGrantOption]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        has_already = self.has_already
        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()

                options.append(options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if has_already is not UNSET:
            field_dict["hasAlready"] = has_already
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import access_grant_option as access_grant_option_m
        except ImportError:
            import sys

            access_grant_option_m = sys.modules[__package__ + "access_grant_option"]

        d = src_dict.copy()

        has_already = d.pop("hasAlready", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = access_grant_option_m.AccessGrantOption.from_dict(options_item_data)

            options.append(options_item)

        access_grant_option_list = cls(
            has_already=has_already,
            options=options,
        )

        return access_grant_option_list
