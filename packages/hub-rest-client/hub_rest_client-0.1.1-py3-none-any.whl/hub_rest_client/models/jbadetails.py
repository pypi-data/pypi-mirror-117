from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.details import Details
from ..types import UNSET, Unset

T = TypeVar("T", bound="Jbadetails")


@attr.s(auto_attribs=True)
class Jbadetails(Details):
    """ """

    login: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    change_password_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login = self.login
        full_name = self.full_name
        change_password_url = self.change_password_url

        field_dict: Dict[str, Any] = {}
        _Details_dict = super(Details).to_dict()
        field_dict.update(_Details_dict)
        field_dict.update(self.additional_properties)
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

        _Details_kwargs = super(Details).from_dict(src_dict=d).to_dict()

        login = d.pop("login", UNSET)

        full_name = d.pop("fullName", UNSET)

        change_password_url = d.pop("changePasswordUrl", UNSET)

        jbadetails = cls(
            login=login,
            full_name=full_name,
            change_password_url=change_password_url,
            **_Details_kwargs,
        )

        jbadetails.additional_properties = d
        return jbadetails

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
