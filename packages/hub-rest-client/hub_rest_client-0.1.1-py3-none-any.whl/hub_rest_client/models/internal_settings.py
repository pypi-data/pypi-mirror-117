from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.settings import Settings
from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalSettings")


@attr.s(auto_attribs=True)
class InternalSettings(Settings):
    """ """

    token_interval: Union[Unset, int] = UNSET
    session_interval: Union[Unset, int] = UNSET
    remember_me_interval: Union[Unset, int] = UNSET
    hash_anonymization: Union[Unset, bool] = UNSET
    captcha_public_key: Union[Unset, str] = UNSET
    captcha_private_key: Union[Unset, str] = UNSET
    debug_categories: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token_interval = self.token_interval
        session_interval = self.session_interval
        remember_me_interval = self.remember_me_interval
        hash_anonymization = self.hash_anonymization
        captcha_public_key = self.captcha_public_key
        captcha_private_key = self.captcha_private_key
        debug_categories: Union[Unset, List[str]] = UNSET
        if not isinstance(self.debug_categories, Unset):
            debug_categories = self.debug_categories

        field_dict: Dict[str, Any] = {}
        _Settings_dict = super(Settings).to_dict()
        field_dict.update(_Settings_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token_interval is not UNSET:
            field_dict["tokenInterval"] = token_interval
        if session_interval is not UNSET:
            field_dict["sessionInterval"] = session_interval
        if remember_me_interval is not UNSET:
            field_dict["rememberMeInterval"] = remember_me_interval
        if hash_anonymization is not UNSET:
            field_dict["hashAnonymization"] = hash_anonymization
        if captcha_public_key is not UNSET:
            field_dict["captchaPublicKey"] = captcha_public_key
        if captcha_private_key is not UNSET:
            field_dict["captchaPrivateKey"] = captcha_private_key
        if debug_categories is not UNSET:
            field_dict["debugCategories"] = debug_categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Settings_kwargs = super(Settings).from_dict(src_dict=d).to_dict()

        token_interval = d.pop("tokenInterval", UNSET)

        session_interval = d.pop("sessionInterval", UNSET)

        remember_me_interval = d.pop("rememberMeInterval", UNSET)

        hash_anonymization = d.pop("hashAnonymization", UNSET)

        captcha_public_key = d.pop("captchaPublicKey", UNSET)

        captcha_private_key = d.pop("captchaPrivateKey", UNSET)

        debug_categories = cast(List[str], d.pop("debugCategories", UNSET))

        internal_settings = cls(
            token_interval=token_interval,
            session_interval=session_interval,
            remember_me_interval=remember_me_interval,
            hash_anonymization=hash_anonymization,
            captcha_public_key=captcha_public_key,
            captcha_private_key=captcha_private_key,
            debug_categories=debug_categories,
            **_Settings_kwargs,
        )

        internal_settings.additional_properties = d
        return internal_settings

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
