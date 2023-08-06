from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseInfo")


@attr.s(auto_attribs=True)
class LicenseInfo:
    """ """

    product: Union[Unset, int] = UNSET
    license_type: Union[Unset, int] = UNSET
    major_version: Union[Unset, int] = UNSET
    minor_version: Union[Unset, int] = UNSET
    build_number: Union[Unset, int] = UNSET
    user_count: Union[Unset, int] = UNSET
    expiration_date: Union[Unset, int] = UNSET
    free_update_end: Union[Unset, int] = UNSET
    hosted: Union[Unset, bool] = UNSET
    change_you_track_logo_forbidden: Union[Unset, bool] = UNSET
    guest_ban_forbidden: Union[Unset, bool] = UNSET
    invalidity_reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product = self.product
        license_type = self.license_type
        major_version = self.major_version
        minor_version = self.minor_version
        build_number = self.build_number
        user_count = self.user_count
        expiration_date = self.expiration_date
        free_update_end = self.free_update_end
        hosted = self.hosted
        change_you_track_logo_forbidden = self.change_you_track_logo_forbidden
        guest_ban_forbidden = self.guest_ban_forbidden
        invalidity_reason = self.invalidity_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product is not UNSET:
            field_dict["product"] = product
        if license_type is not UNSET:
            field_dict["licenseType"] = license_type
        if major_version is not UNSET:
            field_dict["majorVersion"] = major_version
        if minor_version is not UNSET:
            field_dict["minorVersion"] = minor_version
        if build_number is not UNSET:
            field_dict["buildNumber"] = build_number
        if user_count is not UNSET:
            field_dict["userCount"] = user_count
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if free_update_end is not UNSET:
            field_dict["freeUpdateEnd"] = free_update_end
        if hosted is not UNSET:
            field_dict["hosted"] = hosted
        if change_you_track_logo_forbidden is not UNSET:
            field_dict["changeYouTrackLogoForbidden"] = change_you_track_logo_forbidden
        if guest_ban_forbidden is not UNSET:
            field_dict["guestBanForbidden"] = guest_ban_forbidden
        if invalidity_reason is not UNSET:
            field_dict["invalidityReason"] = invalidity_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        product = d.pop("product", UNSET)

        license_type = d.pop("licenseType", UNSET)

        major_version = d.pop("majorVersion", UNSET)

        minor_version = d.pop("minorVersion", UNSET)

        build_number = d.pop("buildNumber", UNSET)

        user_count = d.pop("userCount", UNSET)

        expiration_date = d.pop("expirationDate", UNSET)

        free_update_end = d.pop("freeUpdateEnd", UNSET)

        hosted = d.pop("hosted", UNSET)

        change_you_track_logo_forbidden = d.pop("changeYouTrackLogoForbidden", UNSET)

        guest_ban_forbidden = d.pop("guestBanForbidden", UNSET)

        invalidity_reason = d.pop("invalidityReason", UNSET)

        license_info = cls(
            product=product,
            license_type=license_type,
            major_version=major_version,
            minor_version=minor_version,
            build_number=build_number,
            user_count=user_count,
            expiration_date=expiration_date,
            free_update_end=free_update_end,
            hosted=hosted,
            change_you_track_logo_forbidden=change_you_track_logo_forbidden,
            guest_ban_forbidden=guest_ban_forbidden,
            invalidity_reason=invalidity_reason,
        )

        license_info.additional_properties = d
        return license_info

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
