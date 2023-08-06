from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndUserAgreement")


@attr.s(auto_attribs=True)
class EndUserAgreement:
    """ """

    enabled: Union[Unset, bool] = UNSET
    text: Union[Unset, str] = UNSET
    major_version: Union[Unset, int] = UNSET
    minor_version: Union[Unset, int] = UNSET
    update_time: Union[Unset, int] = UNSET
    required_for_rest: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        text = self.text
        major_version = self.major_version
        minor_version = self.minor_version
        update_time = self.update_time
        required_for_rest = self.required_for_rest

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if text is not UNSET:
            field_dict["text"] = text
        if major_version is not UNSET:
            field_dict["majorVersion"] = major_version
        if minor_version is not UNSET:
            field_dict["minorVersion"] = minor_version
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time
        if required_for_rest is not UNSET:
            field_dict["requiredForREST"] = required_for_rest

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        enabled = d.pop("enabled", UNSET)

        text = d.pop("text", UNSET)

        major_version = d.pop("majorVersion", UNSET)

        minor_version = d.pop("minorVersion", UNSET)

        update_time = d.pop("updateTime", UNSET)

        required_for_rest = d.pop("requiredForREST", UNSET)

        end_user_agreement = cls(
            enabled=enabled,
            text=text,
            major_version=major_version,
            minor_version=minor_version,
            update_time=update_time,
            required_for_rest=required_for_rest,
        )

        end_user_agreement.additional_properties = d
        return end_user_agreement

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
