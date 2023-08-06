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

        d = src_dict.copy()

        _Externalpasswordauthmodule_kwargs = super().from_dict(src_dict=d).to_dict()
        _Externalpasswordauthmodule_kwargs.pop("$type")

        jiraauthmodule = cls(
            **_Externalpasswordauthmodule_kwargs,
        )

        return jiraauthmodule
