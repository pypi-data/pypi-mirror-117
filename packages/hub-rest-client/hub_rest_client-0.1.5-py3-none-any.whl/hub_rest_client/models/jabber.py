from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Jabber")


try:
    from ..models import contact
except ImportError:
    import sys

    contact = sys.modules[__package__ + "contact"]


@attr.s(auto_attribs=True)
class Jabber(contact.Contact):
    """ """

    jabber: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        jabber = self.jabber

        field_dict: Dict[str, Any] = {}
        _Contact_dict = super().to_dict()
        field_dict.update(_Contact_dict)
        field_dict.update({})
        if jabber is not UNSET:
            field_dict["jabber"] = jabber

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _Contact_kwargs = super().from_dict(src_dict=d).to_dict()
        _Contact_kwargs.pop("$type")

        jabber = d.pop("jabber", UNSET)

        jabber = cls(
            jabber=jabber,
            **_Contact_kwargs,
        )

        return jabber
