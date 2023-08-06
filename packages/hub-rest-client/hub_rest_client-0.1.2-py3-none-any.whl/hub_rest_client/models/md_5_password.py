from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Md5password")


try:
    from ..models import password
except ImportError:
    import sys

    password = sys.modules[__package__ + "password"]


@attr.s(auto_attribs=True)
class Md5password(password.Password):
    """ """

    hashed_value: "Union[Unset, str]" = UNSET
    salt: "Union[Unset, str]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hashed_value = self.hashed_value
        salt = self.salt

        field_dict: Dict[str, Any] = {}
        _Password_dict = super().to_dict()
        field_dict.update(_Password_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hashed_value is not UNSET:
            field_dict["hashedValue"] = hashed_value
        if salt is not UNSET:
            field_dict["salt"] = salt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _Password_kwargs = super().from_dict(src_dict=d).to_dict()

        hashed_value = d.pop("hashedValue", UNSET)

        salt = d.pop("salt", UNSET)

        md_5_password = cls(
            hashed_value=hashed_value,
            salt=salt,
            **_Password_kwargs,
        )

        md_5_password.additional_properties = d
        return md_5_password

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
