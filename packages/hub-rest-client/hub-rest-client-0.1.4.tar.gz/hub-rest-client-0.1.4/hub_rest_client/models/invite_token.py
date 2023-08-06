from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InviteToken")


@attr.s(auto_attribs=True)
class InviteToken:
    """ """

    user: "Union[Unset, user_m.User]" = UNSET
    token: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import user as user_m
        except ImportError:
            import sys

            user_m = sys.modules[__package__ + "user"]

        d = src_dict.copy()

        _user = d.pop("user", UNSET)
        user: Union[Unset, user_m.User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = user_m.User.from_dict(_user)

        token = d.pop("token", UNSET)

        invite_token = cls(
            user=user,
            token=token,
        )

        return invite_token
