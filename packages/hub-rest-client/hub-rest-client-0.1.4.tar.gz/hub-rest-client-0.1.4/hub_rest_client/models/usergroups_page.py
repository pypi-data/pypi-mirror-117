from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsergroupsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class UsergroupsPage(base_page.BasePage):
    """ """

    usergroups: "Union[Unset, List[user_group_m.UserGroup]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        usergroups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.usergroups, Unset):
            usergroups = []
            for usergroups_item_data in self.usergroups:
                usergroups_item = usergroups_item_data.to_dict()

                usergroups.append(usergroups_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if usergroups is not UNSET:
            field_dict["usergroups"] = usergroups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            user_group_m = sys.modules[__package__ + "user_group"]

        d = src_dict.copy()

        usergroups = []
        _usergroups = d.pop("usergroups", UNSET)
        for usergroups_item_data in _usergroups or []:
            usergroups_item = user_group_m.UserGroup.from_dict(usergroups_item_data)

            usergroups.append(usergroups_item)

        usergroups_page = cls(
            usergroups=usergroups,
        )

        return usergroups_page
