from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Profile")


@attr.s(auto_attribs=True)
class Profile:
    """ """

    avatar: "Union[Unset, avatar_m.Avatar]" = UNSET
    email: "Union[Unset, email_m.Email]" = UNSET
    unverified_email: "Union[Unset, email_m.Email]" = UNSET
    jabber: "Union[Unset, jabber_m.Jabber]" = UNSET
    locale: "Union[Unset, locale_m.Locale]" = UNSET
    attributes: "Union[Unset, List[profile_attribute_m.ProfileAttribute]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        avatar: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        email: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        unverified_email: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unverified_email, Unset):
            unverified_email = self.unverified_email.to_dict()

        jabber: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.jabber, Unset):
            jabber = self.jabber.to_dict()

        locale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.to_dict()

        attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()

                attributes.append(attributes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if email is not UNSET:
            field_dict["email"] = email
        if unverified_email is not UNSET:
            field_dict["unverifiedEmail"] = unverified_email
        if jabber is not UNSET:
            field_dict["jabber"] = jabber
        if locale is not UNSET:
            field_dict["locale"] = locale
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import avatar as avatar_m
            from ..models import email as email_m
            from ..models import jabber as jabber_m
            from ..models import locale as locale_m
            from ..models import profile_attribute as profile_attribute_m
        except ImportError:
            import sys

            locale_m = sys.modules[__package__ + "locale"]
            email_m = sys.modules[__package__ + "email"]
            profile_attribute_m = sys.modules[__package__ + "profile_attribute"]
            avatar_m = sys.modules[__package__ + "avatar"]
            jabber_m = sys.modules[__package__ + "jabber"]

        d = src_dict.copy()

        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, avatar_m.Avatar]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = avatar_m.Avatar.from_dict(_avatar)

        _email = d.pop("email", UNSET)
        email: Union[Unset, email_m.Email]
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = email_m.Email.from_dict(_email)

        _unverified_email = d.pop("unverifiedEmail", UNSET)
        unverified_email: Union[Unset, email_m.Email]
        if isinstance(_unverified_email, Unset):
            unverified_email = UNSET
        else:
            unverified_email = email_m.Email.from_dict(_unverified_email)

        _jabber = d.pop("jabber", UNSET)
        jabber: Union[Unset, jabber_m.Jabber]
        if isinstance(_jabber, Unset):
            jabber = UNSET
        else:
            jabber = jabber_m.Jabber.from_dict(_jabber)

        _locale = d.pop("locale", UNSET)
        locale: Union[Unset, locale_m.Locale]
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = locale_m.Locale.from_dict(_locale)

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = profile_attribute_m.ProfileAttribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        profile = cls(
            avatar=avatar,
            email=email,
            unverified_email=unverified_email,
            jabber=jabber,
            locale=locale,
            attributes=attributes,
        )

        return profile
