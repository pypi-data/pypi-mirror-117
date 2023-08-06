from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Urlavatar")


try:
    from ..models import avatar
except ImportError:
    import sys

    avatar = sys.modules[__package__ + "avatar"]


@attr.s(auto_attribs=True)
class Urlavatar(avatar.Avatar):
    """ """

    avatar_url: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        avatar_url = self.avatar_url

        field_dict: Dict[str, Any] = {}
        _Avatar_dict = super().to_dict()
        field_dict.update(_Avatar_dict)
        field_dict.update({})
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        avatar_url = d.pop("avatarUrl", UNSET)

        urlavatar = cls(
            avatar_url=avatar_url,
        )

        return urlavatar
