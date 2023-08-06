from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.externalpasswordauthmodule import Externalpasswordauthmodule

T = TypeVar("T", bound="Jiraauthmodule")


@attr.s(auto_attribs=True)
class Jiraauthmodule(Externalpasswordauthmodule):
    """ """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _Externalpasswordauthmodule_dict = super(Externalpasswordauthmodule).to_dict()
        field_dict.update(_Externalpasswordauthmodule_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Externalpasswordauthmodule_kwargs = super(Externalpasswordauthmodule).from_dict(src_dict=d).to_dict()

        jiraauthmodule = cls(
            **_Externalpasswordauthmodule_kwargs,
        )

        jiraauthmodule.additional_properties = d
        return jiraauthmodule

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
