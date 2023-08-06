from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationPasswordsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class ApplicationPasswordsPage(base_page.BasePage):
    """ """

    application_passwords: "Union[Unset, List[application_password_m.ApplicationPassword]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        application_passwords: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.application_passwords, Unset):
            application_passwords = []
            for application_passwords_item_data in self.application_passwords:
                application_passwords_item = application_passwords_item_data.to_dict()

                application_passwords.append(application_passwords_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_passwords is not UNSET:
            field_dict["applicationPasswords"] = application_passwords

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import application_password as application_password_m
        except ImportError:
            import sys

            application_password_m = sys.modules[__package__ + "application_password"]

        d = src_dict.copy()

        application_passwords = []
        _application_passwords = d.pop("applicationPasswords", UNSET)
        for application_passwords_item_data in _application_passwords or []:
            application_passwords_item = application_password_m.ApplicationPassword.from_dict(
                application_passwords_item_data
            )

            application_passwords.append(application_passwords_item)

        application_passwords_page = cls(
            application_passwords=application_passwords,
        )

        application_passwords_page.additional_properties = d
        return application_passwords_page

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
