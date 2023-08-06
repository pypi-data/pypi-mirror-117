from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.password import Password
from ..types import UNSET, Unset

T = TypeVar("T", bound="Bcryptpassword")


@attr.s(auto_attribs=True)
class Bcryptpassword(Password):
    """ """

    hashed_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hashed_value = self.hashed_value

        field_dict: Dict[str, Any] = {}
        _Password_dict = super(Password).to_dict()
        field_dict.update(_Password_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hashed_value is not UNSET:
            field_dict["hashedValue"] = hashed_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Password_kwargs = super(Password).from_dict(src_dict=d).to_dict()

        hashed_value = d.pop("hashedValue", UNSET)

        bcryptpassword = cls(
            hashed_value=hashed_value,
            **_Password_kwargs,
        )

        bcryptpassword.additional_properties = d
        return bcryptpassword

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
