from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.provider_metadata import ProviderMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceProviderMetadata")


@attr.s(auto_attribs=True)
class ServiceProviderMetadata(ProviderMetadata):
    """ """

    description: Union[Unset, str] = UNSET
    assertion_consumer_url: Union[Unset, str] = UNSET
    logout_response_supported: Union[Unset, bool] = UNSET
    login_attribute_name: Union[Unset, str] = UNSET
    full_name_attribute_name: Union[Unset, str] = UNSET
    email_attribute_name: Union[Unset, str] = UNSET
    groups_attribute_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        assertion_consumer_url = self.assertion_consumer_url
        logout_response_supported = self.logout_response_supported
        login_attribute_name = self.login_attribute_name
        full_name_attribute_name = self.full_name_attribute_name
        email_attribute_name = self.email_attribute_name
        groups_attribute_name = self.groups_attribute_name

        field_dict: Dict[str, Any] = {}
        _ProviderMetadata_dict = super(ProviderMetadata).to_dict()
        field_dict.update(_ProviderMetadata_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if assertion_consumer_url is not UNSET:
            field_dict["assertionConsumerUrl"] = assertion_consumer_url
        if logout_response_supported is not UNSET:
            field_dict["logoutResponseSupported"] = logout_response_supported
        if login_attribute_name is not UNSET:
            field_dict["loginAttributeName"] = login_attribute_name
        if full_name_attribute_name is not UNSET:
            field_dict["fullNameAttributeName"] = full_name_attribute_name
        if email_attribute_name is not UNSET:
            field_dict["emailAttributeName"] = email_attribute_name
        if groups_attribute_name is not UNSET:
            field_dict["groupsAttributeName"] = groups_attribute_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _ProviderMetadata_kwargs = super(ProviderMetadata).from_dict(src_dict=d).to_dict()

        description = d.pop("description", UNSET)

        assertion_consumer_url = d.pop("assertionConsumerUrl", UNSET)

        logout_response_supported = d.pop("logoutResponseSupported", UNSET)

        login_attribute_name = d.pop("loginAttributeName", UNSET)

        full_name_attribute_name = d.pop("fullNameAttributeName", UNSET)

        email_attribute_name = d.pop("emailAttributeName", UNSET)

        groups_attribute_name = d.pop("groupsAttributeName", UNSET)

        service_provider_metadata = cls(
            description=description,
            assertion_consumer_url=assertion_consumer_url,
            logout_response_supported=logout_response_supported,
            login_attribute_name=login_attribute_name,
            full_name_attribute_name=full_name_attribute_name,
            email_attribute_name=email_attribute_name,
            groups_attribute_name=groups_attribute_name,
            **_ProviderMetadata_kwargs,
        )

        service_provider_metadata.additional_properties = d
        return service_provider_metadata

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
