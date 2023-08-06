from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OwnUsersPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class OwnUsersPage(base_page.BasePage):
    """ """

    own_users: "Union[Unset, List[user_m.User]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        own_users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.own_users, Unset):
            own_users = []
            for own_users_item_data in self.own_users:
                own_users_item = own_users_item_data.to_dict()

                own_users.append(own_users_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if own_users is not UNSET:
            field_dict["ownUsers"] = own_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import user as user_m
        except ImportError:
            import sys

            user_m = sys.modules[__package__ + "user"]

        d = src_dict.copy()

        _BasePage_kwargs = super().from_dict(src_dict=d).to_dict()
        _BasePage_kwargs.pop("$type")

        own_users = []
        _own_users = d.pop("ownUsers", UNSET)
        for own_users_item_data in _own_users or []:
            own_users_item = user_m.User.from_dict(own_users_item_data)

            own_users.append(own_users_item)

        own_users_page = cls(
            own_users=own_users,
            **_BasePage_kwargs,
        )

        return own_users_page
