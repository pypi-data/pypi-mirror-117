from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.avatar import Avatar
from ..types import UNSET, Unset

T = TypeVar("T", bound="Gravatar")


@attr.s(auto_attribs=True)
class Gravatar(Avatar):
    """ """

    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        field_dict: Dict[str, Any] = {}
        _Avatar_dict = super(Avatar).to_dict()
        field_dict.update(_Avatar_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Avatar_kwargs = super(Avatar).from_dict(src_dict=d).to_dict()

        email = d.pop("email", UNSET)

        gravatar = cls(
            email=email,
            **_Avatar_kwargs,
        )

        gravatar.additional_properties = d
        return gravatar

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
