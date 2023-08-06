from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_info import LicenseInfo
    from ..models.service import Service
    from ..models.user import User
    from ..models.user_group import UserGroup
else:
    Service = "Service"
    User = "User"
    UserGroup = "UserGroup"
    LicenseInfo = "LicenseInfo"

from ..models.settings import Settings

T = TypeVar("T", bound="License")


@attr.s(auto_attribs=True)
class License(Settings):
    """ """

    license_key: Union[Unset, str] = UNSET
    license_name: Union[Unset, str] = UNSET
    service: Union[Unset, Service] = UNSET
    users: Union[Unset, List[User]] = UNSET
    auto_join_groups: Union[Unset, List[UserGroup]] = UNSET
    license_info: Union[Unset, LicenseInfo] = UNSET
    available_licenses: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        license_key = self.license_key
        license_name = self.license_name
        service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.to_dict()

        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()

                users.append(users_item)

        auto_join_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.auto_join_groups, Unset):
            auto_join_groups = []
            for auto_join_groups_item_data in self.auto_join_groups:
                auto_join_groups_item = auto_join_groups_item_data.to_dict()

                auto_join_groups.append(auto_join_groups_item)

        license_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.license_info, Unset):
            license_info = self.license_info.to_dict()

        available_licenses = self.available_licenses

        field_dict: Dict[str, Any] = {}
        _Settings_dict = super(Settings).to_dict()
        field_dict.update(_Settings_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if license_key is not UNSET:
            field_dict["licenseKey"] = license_key
        if license_name is not UNSET:
            field_dict["licenseName"] = license_name
        if service is not UNSET:
            field_dict["service"] = service
        if users is not UNSET:
            field_dict["users"] = users
        if auto_join_groups is not UNSET:
            field_dict["autoJoinGroups"] = auto_join_groups
        if license_info is not UNSET:
            field_dict["licenseInfo"] = license_info
        if available_licenses is not UNSET:
            field_dict["availableLicenses"] = available_licenses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Settings_kwargs = super(Settings).from_dict(src_dict=d).to_dict()

        license_key = d.pop("licenseKey", UNSET)

        license_name = d.pop("licenseName", UNSET)

        _service = d.pop("service", UNSET)
        service: Union[Unset, Service]
        if isinstance(_service, Unset):
            service = UNSET
        else:
            service = Service.from_dict(_service)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = User.from_dict(users_item_data)

            users.append(users_item)

        auto_join_groups = []
        _auto_join_groups = d.pop("autoJoinGroups", UNSET)
        for auto_join_groups_item_data in _auto_join_groups or []:
            auto_join_groups_item = UserGroup.from_dict(auto_join_groups_item_data)

            auto_join_groups.append(auto_join_groups_item)

        _license_info = d.pop("licenseInfo", UNSET)
        license_info: Union[Unset, LicenseInfo]
        if isinstance(_license_info, Unset):
            license_info = UNSET
        else:
            license_info = LicenseInfo.from_dict(_license_info)

        available_licenses = d.pop("availableLicenses", UNSET)

        license_ = cls(
            license_key=license_key,
            license_name=license_name,
            service=service,
            users=users,
            auto_join_groups=auto_join_groups,
            license_info=license_info,
            available_licenses=available_licenses,
            **_Settings_kwargs,
        )

        license_.additional_properties = d
        return license_

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
