from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_store import KeyStore
else:
    KeyStore = "KeyStore"

from ..models.settings import Settings

T = TypeVar("T", bound="SmtpSettings")


@attr.s(auto_attribs=True)
class SmtpSettings(Settings):
    """ """

    enabled: Union[Unset, bool] = UNSET
    host: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    protocol: Union[Unset, str] = UNSET
    from_: Union[Unset, str] = UNSET
    envelope_from: Union[Unset, str] = UNSET
    login: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    password_defined: Union[Unset, bool] = UNSET
    key_store: Union[Unset, KeyStore] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        d = src_dict.copy()

        _Settings_kwargs = super(Settings).from_dict(src_dict=d).to_dict()

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
        key_store: Union[Unset, KeyStore]
        if isinstance(_key_store, Unset):
            key_store = UNSET
        else:
            key_store = KeyStore.from_dict(_key_store)

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
            **_Settings_kwargs,
        )

        smtp_settings.additional_properties = d
        return smtp_settings

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
