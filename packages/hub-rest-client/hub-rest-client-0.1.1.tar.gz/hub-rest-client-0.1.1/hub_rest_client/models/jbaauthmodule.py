from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.externalpasswordauthmodule import Externalpasswordauthmodule
from ..types import UNSET, Unset

T = TypeVar("T", bound="Jbaauthmodule")


@attr.s(auto_attribs=True)
class Jbaauthmodule(Externalpasswordauthmodule):
    """ """

    registration_enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        registration_enabled = self.registration_enabled

        field_dict: Dict[str, Any] = {}
        _Externalpasswordauthmodule_dict = super(Externalpasswordauthmodule).to_dict()
        field_dict.update(_Externalpasswordauthmodule_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if registration_enabled is not UNSET:
            field_dict["registrationEnabled"] = registration_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Externalpasswordauthmodule_kwargs = super(Externalpasswordauthmodule).from_dict(src_dict=d).to_dict()

        registration_enabled = d.pop("registrationEnabled", UNSET)

        jbaauthmodule = cls(
            registration_enabled=registration_enabled,
            **_Externalpasswordauthmodule_kwargs,
        )

        jbaauthmodule.additional_properties = d
        return jbaauthmodule

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
