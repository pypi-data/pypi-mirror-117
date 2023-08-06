from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateUser")


@attr.s(auto_attribs=True)
class DuplicateUser:
    """ """

    user: "Union[Unset, user_m.User]" = UNSET
    reason_fields: "Union[Unset, List[str]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        reason_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.reason_fields, Unset):
            reason_fields = self.reason_fields

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if reason_fields is not UNSET:
            field_dict["reasonFields"] = reason_fields

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

        reason_fields = cast(List[str], d.pop("reasonFields", UNSET))

        duplicate_user = cls(
            user=user,
            reason_fields=reason_fields,
        )

        return duplicate_user
