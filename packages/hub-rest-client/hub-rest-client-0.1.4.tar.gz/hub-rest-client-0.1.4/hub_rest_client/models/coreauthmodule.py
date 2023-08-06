from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Coreauthmodule")


try:
    from ..models import authmodule
except ImportError:
    import sys

    authmodule = sys.modules[__package__ + "authmodule"]


@attr.s(auto_attribs=True)
class Coreauthmodule(authmodule.Authmodule):
    """ """

    registration_enabled: "Union[Unset, bool]" = UNSET
    password_restore_enabled: "Union[Unset, bool]" = UNSET
    captcha_enabled: "Union[Unset, bool]" = UNSET
    password_strength_policy: "Union[Unset, int]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        registration_enabled = self.registration_enabled
        password_restore_enabled = self.password_restore_enabled
        captcha_enabled = self.captcha_enabled
        password_strength_policy = self.password_strength_policy

        field_dict: Dict[str, Any] = {}
        _Authmodule_dict = super().to_dict()
        field_dict.update(_Authmodule_dict)
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

        registration_enabled = d.pop("registrationEnabled", UNSET)

        password_restore_enabled = d.pop("passwordRestoreEnabled", UNSET)

        captcha_enabled = d.pop("captchaEnabled", UNSET)

        password_strength_policy = d.pop("passwordStrengthPolicy", UNSET)

        coreauthmodule = cls(
            registration_enabled=registration_enabled,
            password_restore_enabled=password_restore_enabled,
            captcha_enabled=captcha_enabled,
            password_strength_policy=password_strength_policy,
        )

        return coreauthmodule
