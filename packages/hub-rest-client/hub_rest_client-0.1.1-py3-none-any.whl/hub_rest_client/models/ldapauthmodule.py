from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.externalpasswordauthmodule import Externalpasswordauthmodule
from ..types import UNSET, Unset

T = TypeVar("T", bound="Ldapauthmodule")


@attr.s(auto_attribs=True)
class Ldapauthmodule(Externalpasswordauthmodule):
    """ """

    filter_: Union[Unset, str] = UNSET
    format_dn: Union[Unset, str] = UNSET
    email_attribute_name: Union[Unset, str] = UNSET
    full_name_attribute_name: Union[Unset, str] = UNSET
    jabber_attribute_name: Union[Unset, str] = UNSET
    user_id_attribute_name: Union[Unset, str] = UNSET
    vcs_name_attribute_name: Union[Unset, str] = UNSET
    groups_attribute_name: Union[Unset, str] = UNSET
    account_expires_attribute_name: Union[Unset, str] = UNSET
    user_account_control_attribute_name: Union[Unset, str] = UNSET
    lockout_threshold_attribute_name: Union[Unset, str] = UNSET
    lockout_time_attribute_name: Union[Unset, str] = UNSET
    lockout_duration_attribute_name: Union[Unset, str] = UNSET
    bind_user_login: Union[Unset, str] = UNSET
    bind_user_password: Union[Unset, str] = UNSET
    use_bind_user: Union[Unset, bool] = UNSET
    referral_ignored: Union[Unset, bool] = UNSET
    user_status_ignored: Union[Unset, bool] = UNSET
    sync_interval: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_ = self.filter_
        format_dn = self.format_dn
        email_attribute_name = self.email_attribute_name
        full_name_attribute_name = self.full_name_attribute_name
        jabber_attribute_name = self.jabber_attribute_name
        user_id_attribute_name = self.user_id_attribute_name
        vcs_name_attribute_name = self.vcs_name_attribute_name
        groups_attribute_name = self.groups_attribute_name
        account_expires_attribute_name = self.account_expires_attribute_name
        user_account_control_attribute_name = self.user_account_control_attribute_name
        lockout_threshold_attribute_name = self.lockout_threshold_attribute_name
        lockout_time_attribute_name = self.lockout_time_attribute_name
        lockout_duration_attribute_name = self.lockout_duration_attribute_name
        bind_user_login = self.bind_user_login
        bind_user_password = self.bind_user_password
        use_bind_user = self.use_bind_user
        referral_ignored = self.referral_ignored
        user_status_ignored = self.user_status_ignored
        sync_interval = self.sync_interval

        field_dict: Dict[str, Any] = {}
        _Externalpasswordauthmodule_dict = super(Externalpasswordauthmodule).to_dict()
        field_dict.update(_Externalpasswordauthmodule_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if format_dn is not UNSET:
            field_dict["formatDN"] = format_dn
        if email_attribute_name is not UNSET:
            field_dict["emailAttributeName"] = email_attribute_name
        if full_name_attribute_name is not UNSET:
            field_dict["fullNameAttributeName"] = full_name_attribute_name
        if jabber_attribute_name is not UNSET:
            field_dict["jabberAttributeName"] = jabber_attribute_name
        if user_id_attribute_name is not UNSET:
            field_dict["userIdAttributeName"] = user_id_attribute_name
        if vcs_name_attribute_name is not UNSET:
            field_dict["VCSNameAttributeName"] = vcs_name_attribute_name
        if groups_attribute_name is not UNSET:
            field_dict["groupsAttributeName"] = groups_attribute_name
        if account_expires_attribute_name is not UNSET:
            field_dict["accountExpiresAttributeName"] = account_expires_attribute_name
        if user_account_control_attribute_name is not UNSET:
            field_dict["userAccountControlAttributeName"] = user_account_control_attribute_name
        if lockout_threshold_attribute_name is not UNSET:
            field_dict["lockoutThresholdAttributeName"] = lockout_threshold_attribute_name
        if lockout_time_attribute_name is not UNSET:
            field_dict["lockoutTimeAttributeName"] = lockout_time_attribute_name
        if lockout_duration_attribute_name is not UNSET:
            field_dict["lockoutDurationAttributeName"] = lockout_duration_attribute_name
        if bind_user_login is not UNSET:
            field_dict["bindUserLogin"] = bind_user_login
        if bind_user_password is not UNSET:
            field_dict["bindUserPassword"] = bind_user_password
        if use_bind_user is not UNSET:
            field_dict["useBindUser"] = use_bind_user
        if referral_ignored is not UNSET:
            field_dict["referralIgnored"] = referral_ignored
        if user_status_ignored is not UNSET:
            field_dict["userStatusIgnored"] = user_status_ignored
        if sync_interval is not UNSET:
            field_dict["syncInterval"] = sync_interval

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Externalpasswordauthmodule_kwargs = super(Externalpasswordauthmodule).from_dict(src_dict=d).to_dict()

        filter_ = d.pop("filter", UNSET)

        format_dn = d.pop("formatDN", UNSET)

        email_attribute_name = d.pop("emailAttributeName", UNSET)

        full_name_attribute_name = d.pop("fullNameAttributeName", UNSET)

        jabber_attribute_name = d.pop("jabberAttributeName", UNSET)

        user_id_attribute_name = d.pop("userIdAttributeName", UNSET)

        vcs_name_attribute_name = d.pop("VCSNameAttributeName", UNSET)

        groups_attribute_name = d.pop("groupsAttributeName", UNSET)

        account_expires_attribute_name = d.pop("accountExpiresAttributeName", UNSET)

        user_account_control_attribute_name = d.pop("userAccountControlAttributeName", UNSET)

        lockout_threshold_attribute_name = d.pop("lockoutThresholdAttributeName", UNSET)

        lockout_time_attribute_name = d.pop("lockoutTimeAttributeName", UNSET)

        lockout_duration_attribute_name = d.pop("lockoutDurationAttributeName", UNSET)

        bind_user_login = d.pop("bindUserLogin", UNSET)

        bind_user_password = d.pop("bindUserPassword", UNSET)

        use_bind_user = d.pop("useBindUser", UNSET)

        referral_ignored = d.pop("referralIgnored", UNSET)

        user_status_ignored = d.pop("userStatusIgnored", UNSET)

        sync_interval = d.pop("syncInterval", UNSET)

        ldapauthmodule = cls(
            filter_=filter_,
            format_dn=format_dn,
            email_attribute_name=email_attribute_name,
            full_name_attribute_name=full_name_attribute_name,
            jabber_attribute_name=jabber_attribute_name,
            user_id_attribute_name=user_id_attribute_name,
            vcs_name_attribute_name=vcs_name_attribute_name,
            groups_attribute_name=groups_attribute_name,
            account_expires_attribute_name=account_expires_attribute_name,
            user_account_control_attribute_name=user_account_control_attribute_name,
            lockout_threshold_attribute_name=lockout_threshold_attribute_name,
            lockout_time_attribute_name=lockout_time_attribute_name,
            lockout_duration_attribute_name=lockout_duration_attribute_name,
            bind_user_login=bind_user_login,
            bind_user_password=bind_user_password,
            use_bind_user=use_bind_user,
            referral_ignored=referral_ignored,
            user_status_ignored=user_status_ignored,
            sync_interval=sync_interval,
            **_Externalpasswordauthmodule_kwargs,
        )

        ldapauthmodule.additional_properties = d
        return ldapauthmodule

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
