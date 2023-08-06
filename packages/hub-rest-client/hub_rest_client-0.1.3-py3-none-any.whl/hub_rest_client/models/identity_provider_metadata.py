from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentityProviderMetadata")


try:
    from ..models import provider_metadata
except ImportError:
    import sys

    provider_metadata = sys.modules[__package__ + "provider_metadata"]


@attr.s(auto_attribs=True)
class IdentityProviderMetadata(provider_metadata.ProviderMetadata):
    """ """

    default_name_id_type: "Union[Unset, str]" = UNSET
    service: "Union[Unset, service_m.Service]" = UNSET
    key_store: "Union[Unset, key_store_m.KeyStore]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_name_id_type = self.default_name_id_type
        service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.to_dict()

        key_store: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_store, Unset):
            key_store = self.key_store.to_dict()

        field_dict: Dict[str, Any] = {}
        _ProviderMetadata_dict = super().to_dict()
        field_dict.update(_ProviderMetadata_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_name_id_type is not UNSET:
            field_dict["defaultNameIdType"] = default_name_id_type
        if service is not UNSET:
            field_dict["service"] = service
        if key_store is not UNSET:
            field_dict["keyStore"] = key_store

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import key_store as key_store_m
            from ..models import service as service_m
        except ImportError:
            import sys

            service_m = sys.modules[__package__ + "service"]
            key_store_m = sys.modules[__package__ + "key_store"]

        d = src_dict.copy()

        default_name_id_type = d.pop("defaultNameIdType", UNSET)

        _service = d.pop("service", UNSET)
        service: Union[Unset, service_m.Service]
        if isinstance(_service, Unset):
            service = UNSET
        else:
            service = service_m.Service.from_dict(_service)

        _key_store = d.pop("keyStore", UNSET)
        key_store: Union[Unset, key_store_m.KeyStore]
        if isinstance(_key_store, Unset):
            key_store = UNSET
        else:
            key_store = key_store_m.KeyStore.from_dict(_key_store)

        identity_provider_metadata = cls(
            default_name_id_type=default_name_id_type,
            service=service,
            key_store=key_store,
        )

        identity_provider_metadata.additional_properties = d
        return identity_provider_metadata

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
