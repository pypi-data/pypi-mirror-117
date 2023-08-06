from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.authmodule import Authmodule
from ..types import UNSET, Unset

T = TypeVar("T", bound="Coreauthmodule")


@attr.s(auto_attribs=True)
class Coreauthmodule(Authmodule):
    """ """

    registration_enabled: Union[Unset, bool] = UNSET
    password_restore_enabled: Union[Unset, bool] = UNSET
    captcha_enabled: Union[Unset, bool] = UNSET
    password_strength_policy: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        registration_enabled = self.registration_enabled
        password_restore_enabled = self.password_restore_enabled
        captcha_enabled = self.captcha_enabled
        password_strength_policy = self.password_strength_policy

        field_dict: Dict[str, Any] = {}
        _Authmodule_dict = super(Authmodule).to_dict()
        field_dict.update(_Authmodule_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if registration_enabled is not UNSET:
            field_dict["registrationEnabled"] = registration_enabled
        if password_restore_enabled is not UNSET:
            field_dict["passwordRestoreEnabled"] = password_restore_enabled
        if captcha_enabled is not UNSET:
            field_dict["captchaEnabled"] = captcha_enabled
        if password_strength_policy is not UNSET:
            field_dict["passwordStrengthPolicy"] = password_strength_policy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Authmodule_kwargs = super(Authmodule).from_dict(src_dict=d).to_dict()

        registration_enabled = d.pop("registrationEnabled", UNSET)

        password_restore_enabled = d.pop("passwordRestoreEnabled", UNSET)

        captcha_enabled = d.pop("captchaEnabled", UNSET)

        password_strength_policy = d.pop("passwordStrengthPolicy", UNSET)

        coreauthmodule = cls(
            registration_enabled=registration_enabled,
            password_restore_enabled=password_restore_enabled,
            captcha_enabled=captcha_enabled,
            password_strength_policy=password_strength_policy,
            **_Authmodule_kwargs,
        )

        coreauthmodule.additional_properties = d
        return coreauthmodule

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
