from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndUserAgreementConsent")


@attr.s(auto_attribs=True)
class EndUserAgreementConsent:
    """ """

    accepted: Union[Unset, bool] = UNSET
    major_version: Union[Unset, int] = UNSET
    minor_version: Union[Unset, int] = UNSET
    time: Union[Unset, int] = UNSET
    revocation_time: Union[Unset, int] = UNSET
    address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accepted = self.accepted
        major_version = self.major_version
        minor_version = self.minor_version
        time = self.time
        revocation_time = self.revocation_time
        address = self.address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepted is not UNSET:
            field_dict["accepted"] = accepted
        if major_version is not UNSET:
            field_dict["majorVersion"] = major_version
        if minor_version is not UNSET:
            field_dict["minorVersion"] = minor_version
        if time is not UNSET:
            field_dict["time"] = time
        if revocation_time is not UNSET:
            field_dict["revocationTime"] = revocation_time
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        accepted = d.pop("accepted", UNSET)

        major_version = d.pop("majorVersion", UNSET)

        minor_version = d.pop("minorVersion", UNSET)

        time = d.pop("time", UNSET)

        revocation_time = d.pop("revocationTime", UNSET)

        address = d.pop("address", UNSET)

        end_user_agreement_consent = cls(
            accepted=accepted,
            major_version=major_version,
            minor_version=minor_version,
            time=time,
            revocation_time=revocation_time,
            address=address,
        )

        end_user_agreement_consent.additional_properties = d
        return end_user_agreement_consent

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
