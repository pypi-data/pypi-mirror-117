from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.externalauthmodule import Externalauthmodule
from ..types import UNSET, Unset

T = TypeVar("T", bound="Openidauthmodule")


@attr.s(auto_attribs=True)
class Openidauthmodule(Externalauthmodule):
    """ """

    email_schema: Union[Unset, str] = UNSET
    first_name_schema: Union[Unset, str] = UNSET
    last_name_schema: Union[Unset, str] = UNSET
    full_name_schema: Union[Unset, str] = UNSET
    avatar_schema: Union[Unset, str] = UNSET
    url_pattern: Union[Unset, str] = UNSET
    icon_url: Union[Unset, str] = UNSET
    email_verified: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email_schema = self.email_schema
        first_name_schema = self.first_name_schema
        last_name_schema = self.last_name_schema
        full_name_schema = self.full_name_schema
        avatar_schema = self.avatar_schema
        url_pattern = self.url_pattern
        icon_url = self.icon_url
        email_verified = self.email_verified

        field_dict: Dict[str, Any] = {}
        _Externalauthmodule_dict = super(Externalauthmodule).to_dict()
        field_dict.update(_Externalauthmodule_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email_schema is not UNSET:
            field_dict["emailSchema"] = email_schema
        if first_name_schema is not UNSET:
            field_dict["firstNameSchema"] = first_name_schema
        if last_name_schema is not UNSET:
            field_dict["lastNameSchema"] = last_name_schema
        if full_name_schema is not UNSET:
            field_dict["fullNameSchema"] = full_name_schema
        if avatar_schema is not UNSET:
            field_dict["avatarSchema"] = avatar_schema
        if url_pattern is not UNSET:
            field_dict["urlPattern"] = url_pattern
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if email_verified is not UNSET:
            field_dict["emailVerified"] = email_verified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Externalauthmodule_kwargs = super(Externalauthmodule).from_dict(src_dict=d).to_dict()

        email_schema = d.pop("emailSchema", UNSET)

        first_name_schema = d.pop("firstNameSchema", UNSET)

        last_name_schema = d.pop("lastNameSchema", UNSET)

        full_name_schema = d.pop("fullNameSchema", UNSET)

        avatar_schema = d.pop("avatarSchema", UNSET)

        url_pattern = d.pop("urlPattern", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        email_verified = d.pop("emailVerified", UNSET)

        openidauthmodule = cls(
            email_schema=email_schema,
            first_name_schema=first_name_schema,
            last_name_schema=last_name_schema,
            full_name_schema=full_name_schema,
            avatar_schema=avatar_schema,
            url_pattern=url_pattern,
            icon_url=icon_url,
            email_verified=email_verified,
            **_Externalauthmodule_kwargs,
        )

        openidauthmodule.additional_properties = d
        return openidauthmodule

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
