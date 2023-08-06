from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Info")


@attr.s(auto_attribs=True)
class Info:
    """ """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    login: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    jabber: Union[Unset, str] = UNSET
    banned: Union[Unset, bool] = UNSET
    ban_badge: Union[Unset, str] = UNSET
    ban_reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        login = self.login
        key = self.key
        url = self.url
        email = self.email
        jabber = self.jabber
        banned = self.banned
        ban_badge = self.ban_badge
        ban_reason = self.ban_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if login is not UNSET:
            field_dict["login"] = login
        if key is not UNSET:
            field_dict["key"] = key
        if url is not UNSET:
            field_dict["url"] = url
        if email is not UNSET:
            field_dict["email"] = email
        if jabber is not UNSET:
            field_dict["jabber"] = jabber
        if banned is not UNSET:
            field_dict["banned"] = banned
        if ban_badge is not UNSET:
            field_dict["banBadge"] = ban_badge
        if ban_reason is not UNSET:
            field_dict["banReason"] = ban_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        login = d.pop("login", UNSET)

        key = d.pop("key", UNSET)

        url = d.pop("url", UNSET)

        email = d.pop("email", UNSET)

        jabber = d.pop("jabber", UNSET)

        banned = d.pop("banned", UNSET)

        ban_badge = d.pop("banBadge", UNSET)

        ban_reason = d.pop("banReason", UNSET)

        info = cls(
            id=id,
            name=name,
            login=login,
            key=key,
            url=url,
            email=email,
            jabber=jabber,
            banned=banned,
            ban_badge=ban_badge,
            ban_reason=ban_reason,
        )

        info.additional_properties = d
        return info

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
