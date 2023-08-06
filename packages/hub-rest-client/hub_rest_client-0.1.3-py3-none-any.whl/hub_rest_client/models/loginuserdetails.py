from typing import Any, Dict, List, Type, TypeVar, Union

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
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login = self.login

        field_dict: Dict[str, Any] = {}
        _Coreuserdetails_dict = super().to_dict()
        field_dict.update(_Coreuserdetails_dict)
        field_dict.update(self.additional_properties)
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

        loginuserdetails.additional_properties = d
        return loginuserdetails

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
