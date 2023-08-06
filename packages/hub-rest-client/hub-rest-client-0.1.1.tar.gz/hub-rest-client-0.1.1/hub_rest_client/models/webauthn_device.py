from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebauthnDevice")


@attr.s(auto_attribs=True)
class WebauthnDevice:
    """ """

    enabled: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    icon_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        name = self.name
        vendor = self.vendor
        url = self.url
        icon_url = self.icon_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if url is not UNSET:
            field_dict["url"] = url
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        enabled = d.pop("enabled", UNSET)

        name = d.pop("name", UNSET)

        vendor = d.pop("vendor", UNSET)

        url = d.pop("url", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        webauthn_device = cls(
            enabled=enabled,
            name=name,
            vendor=vendor,
            url=url,
            icon_url=icon_url,
        )

        webauthn_device.additional_properties = d
        return webauthn_device

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
