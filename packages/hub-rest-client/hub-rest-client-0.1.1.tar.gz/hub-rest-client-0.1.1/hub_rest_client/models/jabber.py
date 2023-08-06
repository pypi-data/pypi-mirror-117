from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.contact import Contact
from ..types import UNSET, Unset

T = TypeVar("T", bound="Jabber")


@attr.s(auto_attribs=True)
class Jabber(Contact):
    """ """

    jabber: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        jabber = self.jabber

        field_dict: Dict[str, Any] = {}
        _Contact_dict = super(Contact).to_dict()
        field_dict.update(_Contact_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jabber is not UNSET:
            field_dict["jabber"] = jabber

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Contact_kwargs = super(Contact).from_dict(src_dict=d).to_dict()

        jabber = d.pop("jabber", UNSET)

        jabber = cls(
            jabber=jabber,
            **_Contact_kwargs,
        )

        jabber.additional_properties = d
        return jabber

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
