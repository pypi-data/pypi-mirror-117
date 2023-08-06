from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.settings import Settings
from ..types import UNSET, Unset

T = TypeVar("T", bound="JabberSettings")


@attr.s(auto_attribs=True)
class JabberSettings(Settings):
    """ """

    enabled: Union[Unset, bool] = UNSET
    host: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    service_name: Union[Unset, str] = UNSET
    sasl_enabled: Union[Unset, bool] = UNSET
    login: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    password_defined: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        host = self.host
        port = self.port
        service_name = self.service_name
        sasl_enabled = self.sasl_enabled
        login = self.login
        password = self.password
        password_defined = self.password_defined

        field_dict: Dict[str, Any] = {}
        _Settings_dict = super(Settings).to_dict()
        field_dict.update(_Settings_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if sasl_enabled is not UNSET:
            field_dict["SASLEnabled"] = sasl_enabled
        if login is not UNSET:
            field_dict["login"] = login
        if password is not UNSET:
            field_dict["password"] = password
        if password_defined is not UNSET:
            field_dict["passwordDefined"] = password_defined

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Settings_kwargs = super(Settings).from_dict(src_dict=d).to_dict()

        enabled = d.pop("enabled", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        service_name = d.pop("serviceName", UNSET)

        sasl_enabled = d.pop("SASLEnabled", UNSET)

        login = d.pop("login", UNSET)

        password = d.pop("password", UNSET)

        password_defined = d.pop("passwordDefined", UNSET)

        jabber_settings = cls(
            enabled=enabled,
            host=host,
            port=port,
            service_name=service_name,
            sasl_enabled=sasl_enabled,
            login=login,
            password=password,
            password_defined=password_defined,
            **_Settings_kwargs,
        )

        jabber_settings.additional_properties = d
        return jabber_settings

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
