from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Ldapdetails")


try:
    from ..models import details
except ImportError:
    import sys

    details = sys.modules[__package__ + "details"]


@attr.s(auto_attribs=True)
class Ldapdetails(details.Details):
    """ """

    userid: "Union[Unset, str]" = UNSET
    full_name: "Union[Unset, str]" = UNSET
    change_password_url: "Union[Unset, str]" = UNSET
    jabber: "Union[Unset, jabber_m.Jabber]" = UNSET
    vcs_name: "Union[Unset, str]" = UNSET
    ldap_group_names: "Union[Unset, List[str]]" = UNSET
    user_status: "Union[Unset, str]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        userid = self.userid
        full_name = self.full_name
        change_password_url = self.change_password_url
        jabber: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.jabber, Unset):
            jabber = self.jabber.to_dict()

        vcs_name = self.vcs_name
        ldap_group_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ldap_group_names, Unset):
            ldap_group_names = self.ldap_group_names

        user_status = self.user_status

        field_dict: Dict[str, Any] = {}
        _Details_dict = super().to_dict()
        field_dict.update(_Details_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if userid is not UNSET:
            field_dict["userid"] = userid
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if change_password_url is not UNSET:
            field_dict["changePasswordUrl"] = change_password_url
        if jabber is not UNSET:
            field_dict["jabber"] = jabber
        if vcs_name is not UNSET:
            field_dict["VCSName"] = vcs_name
        if ldap_group_names is not UNSET:
            field_dict["ldapGroupNames"] = ldap_group_names
        if user_status is not UNSET:
            field_dict["userStatus"] = user_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import jabber as jabber_m
        except ImportError:
            import sys

            jabber_m = sys.modules[__package__ + "jabber"]

        d = src_dict.copy()

        _Details_kwargs = super().from_dict(src_dict=d).to_dict()

        userid = d.pop("userid", UNSET)

        full_name = d.pop("fullName", UNSET)

        change_password_url = d.pop("changePasswordUrl", UNSET)

        _jabber = d.pop("jabber", UNSET)
        jabber: Union[Unset, jabber_m.Jabber]
        if isinstance(_jabber, Unset):
            jabber = UNSET
        else:
            jabber = jabber_m.Jabber.from_dict(_jabber)

        vcs_name = d.pop("VCSName", UNSET)

        ldap_group_names = cast(List[str], d.pop("ldapGroupNames", UNSET))

        user_status = d.pop("userStatus", UNSET)

        ldapdetails = cls(
            userid=userid,
            full_name=full_name,
            change_password_url=change_password_url,
            jabber=jabber,
            vcs_name=vcs_name,
            ldap_group_names=ldap_group_names,
            user_status=user_status,
            **_Details_kwargs,
        )

        ldapdetails.additional_properties = d
        return ldapdetails

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
