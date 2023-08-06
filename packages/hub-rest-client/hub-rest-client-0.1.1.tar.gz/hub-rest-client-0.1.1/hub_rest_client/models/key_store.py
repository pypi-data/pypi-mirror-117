from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alias import Alias
    from ..models.certificate_info import CertificateInfo
    from ..models.key_store_data import KeyStoreData
else:
    CertificateInfo = "CertificateInfo"
    KeyStoreData = "KeyStoreData"
    Alias = "Alias"


T = TypeVar("T", bound="KeyStore")


@attr.s(auto_attribs=True)
class KeyStore:
    """ """

    id: Union[Unset, str] = UNSET
    aliases: Union[Unset, List[Alias]] = UNSET
    name: Union[Unset, str] = UNSET
    data: Union[Unset, KeyStoreData] = UNSET
    certificate: Union[Unset, CertificateInfo] = UNSET
    certificate_data: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()

                aliases.append(aliases_item)

        name = self.name
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        certificate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.certificate, Unset):
            certificate = self.certificate.to_dict()

        certificate_data = self.certificate_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if name is not UNSET:
            field_dict["name"] = name
        if data is not UNSET:
            field_dict["data"] = data
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if certificate_data is not UNSET:
            field_dict["certificateData"] = certificate_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        name = d.pop("name", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, KeyStoreData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = KeyStoreData.from_dict(_data)

        _certificate = d.pop("certificate", UNSET)
        certificate: Union[Unset, CertificateInfo]
        if isinstance(_certificate, Unset):
            certificate = UNSET
        else:
            certificate = CertificateInfo.from_dict(_certificate)

        certificate_data = d.pop("certificateData", UNSET)

        key_store = cls(
            id=id,
            aliases=aliases,
            name=name,
            data=data,
            certificate=certificate,
            certificate_data=certificate_data,
        )

        key_store.additional_properties = d
        return key_store

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
