from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.avatar import Avatar
    from ..models.email import Email
    from ..models.jabber import Jabber
    from ..models.locale import Locale
    from ..models.profile_attribute import ProfileAttribute
else:
    Jabber = "Jabber"
    ProfileAttribute = "ProfileAttribute"
    Avatar = "Avatar"
    Locale = "Locale"
    Email = "Email"


T = TypeVar("T", bound="Profile")


@attr.s(auto_attribs=True)
class Profile:
    """ """

    avatar: Union[Unset, Avatar] = UNSET
    email: Union[Unset, Email] = UNSET
    unverified_email: Union[Unset, Email] = UNSET
    jabber: Union[Unset, Jabber] = UNSET
    locale: Union[Unset, Locale] = UNSET
    attributes: Union[Unset, List[ProfileAttribute]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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
        d = src_dict.copy()

        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, Avatar]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = Avatar.from_dict(_avatar)

        _email = d.pop("email", UNSET)
        email: Union[Unset, Email]
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = Email.from_dict(_email)

        _unverified_email = d.pop("unverifiedEmail", UNSET)
        unverified_email: Union[Unset, Email]
        if isinstance(_unverified_email, Unset):
            unverified_email = UNSET
        else:
            unverified_email = Email.from_dict(_unverified_email)

        _jabber = d.pop("jabber", UNSET)
        jabber: Union[Unset, Jabber]
        if isinstance(_jabber, Unset):
            jabber = UNSET
        else:
            jabber = Jabber.from_dict(_jabber)

        _locale = d.pop("locale", UNSET)
        locale: Union[Unset, Locale]
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = Locale.from_dict(_locale)

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = ProfileAttribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        profile = cls(
            avatar=avatar,
            email=email,
            unverified_email=unverified_email,
            jabber=jabber,
            locale=locale,
            attributes=attributes,
        )

        profile.additional_properties = d
        return profile

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
