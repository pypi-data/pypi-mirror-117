from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Email")


try:
    from ..models import contact
except ImportError:
    import sys

    contact = sys.modules[__package__ + "contact"]


@attr.s(auto_attribs=True)
class Email(contact.Contact):
    """ """

    email: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        field_dict: Dict[str, Any] = {}
        _Contact_dict = super().to_dict()
        field_dict.update(_Contact_dict)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        email = d.pop("email", UNSET)

        email = cls(
            email=email,
        )

        return email
