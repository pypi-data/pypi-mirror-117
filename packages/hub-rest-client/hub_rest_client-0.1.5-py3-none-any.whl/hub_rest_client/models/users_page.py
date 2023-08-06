from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsersPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class UsersPage(base_page.BasePage):
    """ """

    users: "Union[Unset, List[user_m.User]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()

                users.append(users_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users

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

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = user_m.User.from_dict(users_item_data)

            users.append(users_item)

        users_page = cls(
            users=users,
            **_BasePage_kwargs,
        )

        return users_page
