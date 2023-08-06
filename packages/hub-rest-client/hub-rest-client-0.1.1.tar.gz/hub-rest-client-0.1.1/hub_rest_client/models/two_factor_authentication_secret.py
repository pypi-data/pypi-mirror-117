from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TwoFactorAuthenticationSecret")


@attr.s(auto_attribs=True)
class TwoFactorAuthenticationSecret:
    """ """

    type: str
    secret_key: Union[Unset, str] = UNSET
    qr_code_uri: Union[Unset, str] = UNSET
    scratch_codes: Union[Unset, List[int]] = UNSET
    failed_attempts_counter: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        secret_key = self.secret_key
        qr_code_uri = self.qr_code_uri
        scratch_codes: Union[Unset, List[int]] = UNSET
        if not isinstance(self.scratch_codes, Unset):
            scratch_codes = self.scratch_codes

        failed_attempts_counter = self.failed_attempts_counter

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key
        if qr_code_uri is not UNSET:
            field_dict["qrCodeUri"] = qr_code_uri
        if scratch_codes is not UNSET:
            field_dict["scratchCodes"] = scratch_codes
        if failed_attempts_counter is not UNSET:
            field_dict["failedAttemptsCounter"] = failed_attempts_counter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        type = d.pop("type")

        secret_key = d.pop("secretKey", UNSET)

        qr_code_uri = d.pop("qrCodeUri", UNSET)

        scratch_codes = cast(List[int], d.pop("scratchCodes", UNSET))

        failed_attempts_counter = d.pop("failedAttemptsCounter", UNSET)

        two_factor_authentication_secret = cls(
            type=type,
            secret_key=secret_key,
            qr_code_uri=qr_code_uri,
            scratch_codes=scratch_codes,
            failed_attempts_counter=failed_attempts_counter,
        )

        two_factor_authentication_secret.additional_properties = d
        return two_factor_authentication_secret

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
