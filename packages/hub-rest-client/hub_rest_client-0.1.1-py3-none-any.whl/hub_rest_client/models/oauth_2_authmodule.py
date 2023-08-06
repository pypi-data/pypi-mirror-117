from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.externaloauth_2_module import Externaloauth2module
from ..types import UNSET, Unset

T = TypeVar("T", bound="Oauth2authmodule")


@attr.s(auto_attribs=True)
class Oauth2authmodule(Externaloauth2module):
    """ """

    scope: Union[Unset, str] = UNSET
    token_url: Union[Unset, str] = UNSET
    form_client_auth: Union[Unset, bool] = UNSET
    user_info_url: Union[Unset, str] = UNSET
    user_id_path: Union[Unset, str] = UNSET
    user_email_url: Union[Unset, str] = UNSET
    user_avatar_url: Union[Unset, str] = UNSET
    user_email_path: Union[Unset, str] = UNSET
    user_email_verified_path: Union[Unset, str] = UNSET
    user_name_path: Union[Unset, str] = UNSET
    user_picture_id_path: Union[Unset, str] = UNSET
    user_picture_url_pattern: Union[Unset, str] = UNSET
    email_verified_by_default: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scope = self.scope
        token_url = self.token_url
        form_client_auth = self.form_client_auth
        user_info_url = self.user_info_url
        user_id_path = self.user_id_path
        user_email_url = self.user_email_url
        user_avatar_url = self.user_avatar_url
        user_email_path = self.user_email_path
        user_email_verified_path = self.user_email_verified_path
        user_name_path = self.user_name_path
        user_picture_id_path = self.user_picture_id_path
        user_picture_url_pattern = self.user_picture_url_pattern
        email_verified_by_default = self.email_verified_by_default

        field_dict: Dict[str, Any] = {}
        _Externaloauth2module_dict = super(Externaloauth2module).to_dict()
        field_dict.update(_Externaloauth2module_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if token_url is not UNSET:
            field_dict["tokenUrl"] = token_url
        if form_client_auth is not UNSET:
            field_dict["formClientAuth"] = form_client_auth
        if user_info_url is not UNSET:
            field_dict["userInfoUrl"] = user_info_url
        if user_id_path is not UNSET:
            field_dict["userIdPath"] = user_id_path
        if user_email_url is not UNSET:
            field_dict["userEmailUrl"] = user_email_url
        if user_avatar_url is not UNSET:
            field_dict["userAvatarUrl"] = user_avatar_url
        if user_email_path is not UNSET:
            field_dict["userEmailPath"] = user_email_path
        if user_email_verified_path is not UNSET:
            field_dict["userEmailVerifiedPath"] = user_email_verified_path
        if user_name_path is not UNSET:
            field_dict["userNamePath"] = user_name_path
        if user_picture_id_path is not UNSET:
            field_dict["userPictureIdPath"] = user_picture_id_path
        if user_picture_url_pattern is not UNSET:
            field_dict["userPictureUrlPattern"] = user_picture_url_pattern
        if email_verified_by_default is not UNSET:
            field_dict["emailVerifiedByDefault"] = email_verified_by_default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Externaloauth2module_kwargs = super(Externaloauth2module).from_dict(src_dict=d).to_dict()

        scope = d.pop("scope", UNSET)

        token_url = d.pop("tokenUrl", UNSET)

        form_client_auth = d.pop("formClientAuth", UNSET)

        user_info_url = d.pop("userInfoUrl", UNSET)

        user_id_path = d.pop("userIdPath", UNSET)

        user_email_url = d.pop("userEmailUrl", UNSET)

        user_avatar_url = d.pop("userAvatarUrl", UNSET)

        user_email_path = d.pop("userEmailPath", UNSET)

        user_email_verified_path = d.pop("userEmailVerifiedPath", UNSET)

        user_name_path = d.pop("userNamePath", UNSET)

        user_picture_id_path = d.pop("userPictureIdPath", UNSET)

        user_picture_url_pattern = d.pop("userPictureUrlPattern", UNSET)

        email_verified_by_default = d.pop("emailVerifiedByDefault", UNSET)

        oauth_2_authmodule = cls(
            scope=scope,
            token_url=token_url,
            form_client_auth=form_client_auth,
            user_info_url=user_info_url,
            user_id_path=user_id_path,
            user_email_url=user_email_url,
            user_avatar_url=user_avatar_url,
            user_email_path=user_email_path,
            user_email_verified_path=user_email_verified_path,
            user_name_path=user_name_path,
            user_picture_id_path=user_picture_id_path,
            user_picture_url_pattern=user_picture_url_pattern,
            email_verified_by_default=email_verified_by_default,
            **_Externaloauth2module_kwargs,
        )

        oauth_2_authmodule.additional_properties = d
        return oauth_2_authmodule

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
