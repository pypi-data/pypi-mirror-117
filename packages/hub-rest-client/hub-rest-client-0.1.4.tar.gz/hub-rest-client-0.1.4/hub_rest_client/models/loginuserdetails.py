from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Loginuserdetails")


try:
    from ..models import coreuserdetails
except ImportError:
    import sys

    coreuserdetails = sys.modules[__package__ + "coreuserdetails"]


@attr.s(auto_attribs=True)
class Loginuserdetails(coreuserdetails.Coreuserdetails):
    """ """

    login: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        login = self.login

        field_dict: Dict[str, Any] = {}
        _Coreuserdetails_dict = super().to_dict()
        field_dict.update(_Coreuserdetails_dict)
        field_dict.update({})
        if login is not UNSET:
            field_dict["login"] = login

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        login = d.pop("login", UNSET)

        loginuserdetails = cls(
            login=login,
        )

        return loginuserdetails
