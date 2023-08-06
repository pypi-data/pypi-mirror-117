from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TwoFactorAuthentication")


try:
    from ..models import two_factor_authentication_secret
except ImportError:
    import sys

    two_factor_authentication_secret = sys.modules[__package__ + "two_factor_authentication_secret"]


@attr.s(auto_attribs=True)
class TwoFactorAuthentication(two_factor_authentication_secret.TwoFactorAuthenticationSecret):
    """ """

    enabled: "Union[Unset, bool]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        _TwoFactorAuthenticationSecret_dict = super().to_dict()
        field_dict.update(_TwoFactorAuthenticationSecret_dict)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _TwoFactorAuthenticationSecret_kwargs = super().from_dict(src_dict=d).to_dict()
        _TwoFactorAuthenticationSecret_kwargs.pop("$type")

        enabled = d.pop("enabled", UNSET)

        two_factor_authentication = cls(
            enabled=enabled,
            **_TwoFactorAuthenticationSecret_kwargs,
        )

        return two_factor_authentication
