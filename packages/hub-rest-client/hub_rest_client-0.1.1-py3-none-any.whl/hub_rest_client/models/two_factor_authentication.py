from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.two_factor_authentication_secret import TwoFactorAuthenticationSecret
from ..types import UNSET, Unset

T = TypeVar("T", bound="TwoFactorAuthentication")


@attr.s(auto_attribs=True)
class TwoFactorAuthentication(TwoFactorAuthenticationSecret):
    """ """

    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        _TwoFactorAuthenticationSecret_dict = super(TwoFactorAuthenticationSecret).to_dict()
        field_dict.update(_TwoFactorAuthenticationSecret_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _TwoFactorAuthenticationSecret_kwargs = super(TwoFactorAuthenticationSecret).from_dict(src_dict=d).to_dict()

        enabled = d.pop("enabled", UNSET)

        two_factor_authentication = cls(
            enabled=enabled,
            **_TwoFactorAuthenticationSecret_kwargs,
        )

        two_factor_authentication.additional_properties = d
        return two_factor_authentication

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
