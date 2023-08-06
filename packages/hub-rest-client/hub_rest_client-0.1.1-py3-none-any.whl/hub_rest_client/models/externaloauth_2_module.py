from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.externalauthmodule import Externalauthmodule
from ..types import UNSET, Unset

T = TypeVar("T", bound="Externaloauth2module")


@attr.s(auto_attribs=True)
class Externaloauth2module(Externalauthmodule):
    """ """

    client_id: Union[Unset, str] = UNSET
    client_secret: Union[Unset, str] = UNSET
    redirect_uri: Union[Unset, str] = UNSET
    icon_url: Union[Unset, str] = UNSET
    extension_grant_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id
        client_secret = self.client_secret
        redirect_uri = self.redirect_uri
        icon_url = self.icon_url
        extension_grant_type = self.extension_grant_type

        field_dict: Dict[str, Any] = {}
        _Externalauthmodule_dict = super(Externalauthmodule).to_dict()
        field_dict.update(_Externalauthmodule_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret
        if redirect_uri is not UNSET:
            field_dict["redirectUri"] = redirect_uri
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if extension_grant_type is not UNSET:
            field_dict["extensionGrantType"] = extension_grant_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Externalauthmodule_kwargs = super(Externalauthmodule).from_dict(src_dict=d).to_dict()

        client_id = d.pop("clientId", UNSET)

        client_secret = d.pop("clientSecret", UNSET)

        redirect_uri = d.pop("redirectUri", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        extension_grant_type = d.pop("extensionGrantType", UNSET)

        externaloauth_2_module = cls(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            icon_url=icon_url,
            extension_grant_type=extension_grant_type,
            **_Externalauthmodule_kwargs,
        )

        externaloauth_2_module.additional_properties = d
        return externaloauth_2_module

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
