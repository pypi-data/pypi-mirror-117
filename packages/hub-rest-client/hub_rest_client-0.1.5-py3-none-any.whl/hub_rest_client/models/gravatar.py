from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Gravatar")


try:
    from ..models import avatar
except ImportError:
    import sys

    avatar = sys.modules[__package__ + "avatar"]


@attr.s(auto_attribs=True)
class Gravatar(avatar.Avatar):
    """ """

    email: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        field_dict: Dict[str, Any] = {}
        _Avatar_dict = super().to_dict()
        field_dict.update(_Avatar_dict)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _Avatar_kwargs = super().from_dict(src_dict=d).to_dict()
        _Avatar_kwargs.pop("$type")

        email = d.pop("email", UNSET)

        gravatar = cls(
            email=email,
            **_Avatar_kwargs,
        )

        return gravatar
