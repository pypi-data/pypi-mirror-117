from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutojoingroupsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class AutojoingroupsPage(base_page.BasePage):
    """ """

    autojoingroups: "Union[Unset, List[user_group_m.UserGroup]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        autojoingroups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.autojoingroups, Unset):
            autojoingroups = []
            for autojoingroups_item_data in self.autojoingroups:
                autojoingroups_item = autojoingroups_item_data.to_dict()

                autojoingroups.append(autojoingroups_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if autojoingroups is not UNSET:
            field_dict["autojoingroups"] = autojoingroups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            user_group_m = sys.modules[__package__ + "user_group"]

        d = src_dict.copy()

        _BasePage_kwargs = super().from_dict(src_dict=d).to_dict()
        _BasePage_kwargs.pop("$type")

        autojoingroups = []
        _autojoingroups = d.pop("autojoingroups", UNSET)
        for autojoingroups_item_data in _autojoingroups or []:
            autojoingroups_item = user_group_m.UserGroup.from_dict(autojoingroups_item_data)

            autojoingroups.append(autojoingroups_item)

        autojoingroups_page = cls(
            autojoingroups=autojoingroups,
            **_BasePage_kwargs,
        )

        return autojoingroups_page
