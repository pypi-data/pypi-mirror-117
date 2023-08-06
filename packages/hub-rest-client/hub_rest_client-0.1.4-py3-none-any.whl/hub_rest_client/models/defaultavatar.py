from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="Defaultavatar")


try:
    from ..models import avatar
except ImportError:
    import sys

    avatar = sys.modules[__package__ + "avatar"]


@attr.s(auto_attribs=True)
class Defaultavatar(avatar.Avatar):
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _Avatar_dict = super().to_dict()
        field_dict.update(_Avatar_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        defaultavatar = cls()

        return defaultavatar
