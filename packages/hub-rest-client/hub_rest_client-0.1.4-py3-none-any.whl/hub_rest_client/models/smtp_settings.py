from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmtpSettings")


try:
    from ..models import settings
except ImportError:
    import sys

    settings = sys.modules[__package__ + "settings"]


@attr.s(auto_attribs=True)
class SmtpSettings(settings.Settings):
    """ """

    enabled: "Union[Unset, bool]" = UNSET
    host: "Union[Unset, str]" = UNSET
    port: "Union[Unset, int]" = UNSET
    protocol: "Union[Unset, str]" = UNSET
    from_: "Union[Unset, str]" = UNSET
    envelope_from: "Union[Unset, str]" = UNSET
    login: "Union[Unset, str]" = UNSET
    password: "Union[Unset, str]" = UNSET
    password_defined: "Union[Unset, bool]" = UNSET
    key_store: "Union[Unset, key_store_m.KeyStore]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        host = self.host
        port = self.port
        protocol = self.protocol
        from_ = self.from_
        envelope_from = self.envelope_from
        login = self.login
        password = self.password
        password_defined = self.password_defined
        key_store: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_store, Unset):
            key_store = self.key_store.to_dict()

        field_dict: Dict[str, Any] = {}
        _Settings_dict = super().to_dict()
        field_dict.update(_Settings_dict)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if from_ is not UNSET:
            field_dict["from"] = from_
        if envelope_from is not UNSET:
            field_dict["envelopeFrom"] = envelope_from
        if login is not UNSET:
            field_dict["login"] = login
        if password is not UNSET:
            field_dict["password"] = password
        if password_defined is not UNSET:
            field_dict["passwordDefined"] = password_defined
        if key_store is not UNSET:
            field_dict["keyStore"] = key_store

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import key_store as key_store_m
        except ImportError:
            import sys

            key_store_m = sys.modules[__package__ + "key_store"]

        d = src_dict.copy()

        enabled = d.pop("enabled", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        protocol = d.pop("protocol", UNSET)

        from_ = d.pop("from", UNSET)

        envelope_from = d.pop("envelopeFrom", UNSET)

        login = d.pop("login", UNSET)

        password = d.pop("password", UNSET)

        password_defined = d.pop("passwordDefined", UNSET)

        _key_store = d.pop("keyStore", UNSET)
        key_store: Union[Unset, key_store_m.KeyStore]
        if isinstance(_key_store, Unset):
            key_store = UNSET
        else:
            key_store = key_store_m.KeyStore.from_dict(_key_store)

        smtp_settings = cls(
            enabled=enabled,
            host=host,
            port=port,
            protocol=protocol,
            from_=from_,
            envelope_from=envelope_from,
            login=login,
            password=password,
            password_defined=password_defined,
            key_store=key_store,
        )

        return smtp_settings
