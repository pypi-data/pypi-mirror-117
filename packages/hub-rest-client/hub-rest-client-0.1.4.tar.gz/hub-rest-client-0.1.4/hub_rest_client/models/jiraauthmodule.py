from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="Jiraauthmodule")


try:
    from ..models import externalpasswordauthmodule
except ImportError:
    import sys

    externalpasswordauthmodule = sys.modules[__package__ + "externalpasswordauthmodule"]


@attr.s(auto_attribs=True)
class Jiraauthmodule(externalpasswordauthmodule.Externalpasswordauthmodule):
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _Externalpasswordauthmodule_dict = super().to_dict()
        field_dict.update(_Externalpasswordauthmodule_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        jiraauthmodule = cls()

        return jiraauthmodule
