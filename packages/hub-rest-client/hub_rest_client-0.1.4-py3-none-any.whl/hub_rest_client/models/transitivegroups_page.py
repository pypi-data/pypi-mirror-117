from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransitivegroupsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class TransitivegroupsPage(base_page.BasePage):
    """ """

    transitivegroups: "Union[Unset, List[user_group_m.UserGroup]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        transitivegroups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transitivegroups, Unset):
            transitivegroups = []
            for transitivegroups_item_data in self.transitivegroups:
                transitivegroups_item = transitivegroups_item_data.to_dict()

                transitivegroups.append(transitivegroups_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if transitivegroups is not UNSET:
            field_dict["transitivegroups"] = transitivegroups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            user_group_m = sys.modules[__package__ + "user_group"]

        d = src_dict.copy()

        transitivegroups = []
        _transitivegroups = d.pop("transitivegroups", UNSET)
        for transitivegroups_item_data in _transitivegroups or []:
            transitivegroups_item = user_group_m.UserGroup.from_dict(transitivegroups_item_data)

            transitivegroups.append(transitivegroups_item)

        transitivegroups_page = cls(
            transitivegroups=transitivegroups,
        )

        return transitivegroups_page
