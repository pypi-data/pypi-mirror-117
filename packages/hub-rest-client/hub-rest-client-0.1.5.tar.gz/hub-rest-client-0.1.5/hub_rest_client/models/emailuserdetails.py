from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="Emailuserdetails")


try:
    from ..models import coreuserdetails
except ImportError:
    import sys

    coreuserdetails = sys.modules[__package__ + "coreuserdetails"]


@attr.s(auto_attribs=True)
class Emailuserdetails(coreuserdetails.Coreuserdetails):
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _Coreuserdetails_dict = super().to_dict()
        field_dict.update(_Coreuserdetails_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _Coreuserdetails_kwargs = super().from_dict(src_dict=d).to_dict()
        _Coreuserdetails_kwargs.pop("$type")

        emailuserdetails = cls(
            **_Coreuserdetails_kwargs,
        )

        return emailuserdetails
