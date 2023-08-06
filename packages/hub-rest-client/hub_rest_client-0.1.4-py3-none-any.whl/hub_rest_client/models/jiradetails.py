from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Jiradetails")


try:
    from ..models import details
except ImportError:
    import sys

    details = sys.modules[__package__ + "details"]


@attr.s(auto_attribs=True)
class Jiradetails(details.Details):
    """ """

    login: "Union[Unset, str]" = UNSET
    full_name: "Union[Unset, str]" = UNSET
    change_password_url: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        login = self.login
        full_name = self.full_name
        change_password_url = self.change_password_url

        field_dict: Dict[str, Any] = {}
        _Details_dict = super().to_dict()
        field_dict.update(_Details_dict)
        field_dict.update({})
        if login is not UNSET:
            field_dict["login"] = login
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if change_password_url is not UNSET:
            field_dict["changePasswordUrl"] = change_password_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        login = d.pop("login", UNSET)

        full_name = d.pop("fullName", UNSET)

        change_password_url = d.pop("changePasswordUrl", UNSET)

        jiradetails = cls(
            login=login,
            full_name=full_name,
            change_password_url=change_password_url,
        )

        return jiradetails
