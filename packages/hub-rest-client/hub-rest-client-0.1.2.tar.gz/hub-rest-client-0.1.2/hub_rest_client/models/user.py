from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


try:
    from ..models import authority_holder
except ImportError:
    import sys

    authority_holder = sys.modules[__package__ + "authority_holder"]


@attr.s(auto_attribs=True)
class User(authority_holder.AuthorityHolder):
    """ """

    login: "Union[Unset, str]" = UNSET
    banned: "Union[Unset, bool]" = UNSET
    ban_reason: "Union[Unset, str]" = UNSET
    ban_badge: "Union[Unset, str]" = UNSET
    guest: "Union[Unset, bool]" = UNSET
    avatar: "Union[Unset, avatar_m.Avatar]" = UNSET
    profile: "Union[Unset, profile_m.Profile]" = UNSET
    groups: "Union[Unset, List[user_group_m.UserGroup]]" = UNSET
    organizations: "Union[Unset, List[organization_m.Organization]]" = UNSET
    transitive_organizations: "Union[Unset, List[organization_m.Organization]]" = UNSET
    transitive_groups: "Union[Unset, List[user_group_m.UserGroup]]" = UNSET
    teams: "Union[Unset, List[project_team_m.ProjectTeam]]" = UNSET
    transitive_teams: "Union[Unset, List[project_team_m.ProjectTeam]]" = UNSET
    details: "Union[Unset, List[details_m.Details]]" = UNSET
    vcs_user_names: "Union[Unset, List[vcs_user_name_m.VcsUserName]]" = UNSET
    ssh_public_keys: "Union[Unset, List[ssh_public_key_m.SshPublicKey]]" = UNSET
    licenses: "Union[Unset, List[license__m.License]]" = UNSET
    creation_time: "Union[Unset, int]" = UNSET
    last_access_time: "Union[Unset, int]" = UNSET
    refresh_tokens: "Union[Unset, List[refresh_token_m.RefreshToken]]" = UNSET
    permanent_tokens: "Union[Unset, List[permanent_token_m.PermanentToken]]" = UNSET
    approved_scopes: "Union[Unset, List[approved_scope_m.ApprovedScope]]" = UNSET
    application_passwords: "Union[Unset, List[application_password_m.ApplicationPassword]]" = UNSET
    favorite_projects: "Union[Unset, List[project_m.Project]]" = UNSET
    end_user_agreement_consent: "Union[Unset, end_user_agreement_consent_m.EndUserAgreementConsent]" = UNSET
    erase_timestamp: "Union[Unset, int]" = UNSET
    two_factor_authentication: "Union[Unset, two_factor_authentication_m.TwoFactorAuthentication]" = UNSET
    required_two_factor_authentication: "Union[Unset, bool]" = UNSET
    pending_two_factor_authentication: "Union[Unset, two_factor_authentication_secret_m.TwoFactorAuthenticationSecret]" = (
        UNSET
    )
    webauthn_device: "Union[Unset, webauthn_device_m.WebauthnDevice]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login = self.login
        banned = self.banned
        ban_reason = self.ban_reason
        ban_badge = self.ban_badge
        guest = self.guest
        avatar: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()

                groups.append(groups_item)

        organizations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()

                organizations.append(organizations_item)

        transitive_organizations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transitive_organizations, Unset):
            transitive_organizations = []
            for transitive_organizations_item_data in self.transitive_organizations:
                transitive_organizations_item = transitive_organizations_item_data.to_dict()

                transitive_organizations.append(transitive_organizations_item)

        transitive_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transitive_groups, Unset):
            transitive_groups = []
            for transitive_groups_item_data in self.transitive_groups:
                transitive_groups_item = transitive_groups_item_data.to_dict()

                transitive_groups.append(transitive_groups_item)

        teams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()

                teams.append(teams_item)

        transitive_teams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transitive_teams, Unset):
            transitive_teams = []
            for transitive_teams_item_data in self.transitive_teams:
                transitive_teams_item = transitive_teams_item_data.to_dict()

                transitive_teams.append(transitive_teams_item)

        details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()

                details.append(details_item)

        vcs_user_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vcs_user_names, Unset):
            vcs_user_names = []
            for vcs_user_names_item_data in self.vcs_user_names:
                vcs_user_names_item = vcs_user_names_item_data.to_dict()

                vcs_user_names.append(vcs_user_names_item)

        ssh_public_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ssh_public_keys, Unset):
            ssh_public_keys = []
            for ssh_public_keys_item_data in self.ssh_public_keys:
                ssh_public_keys_item = ssh_public_keys_item_data.to_dict()

                ssh_public_keys.append(ssh_public_keys_item)

        licenses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.licenses, Unset):
            licenses = []
            for licenses_item_data in self.licenses:
                licenses_item = licenses_item_data.to_dict()

                licenses.append(licenses_item)

        creation_time = self.creation_time
        last_access_time = self.last_access_time
        refresh_tokens: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.refresh_tokens, Unset):
            refresh_tokens = []
            for refresh_tokens_item_data in self.refresh_tokens:
                refresh_tokens_item = refresh_tokens_item_data.to_dict()

                refresh_tokens.append(refresh_tokens_item)

        permanent_tokens: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.permanent_tokens, Unset):
            permanent_tokens = []
            for permanent_tokens_item_data in self.permanent_tokens:
                permanent_tokens_item = permanent_tokens_item_data.to_dict()

                permanent_tokens.append(permanent_tokens_item)

        approved_scopes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.approved_scopes, Unset):
            approved_scopes = []
            for approved_scopes_item_data in self.approved_scopes:
                approved_scopes_item = approved_scopes_item_data.to_dict()

                approved_scopes.append(approved_scopes_item)

        application_passwords: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.application_passwords, Unset):
            application_passwords = []
            for application_passwords_item_data in self.application_passwords:
                application_passwords_item = application_passwords_item_data.to_dict()

                application_passwords.append(application_passwords_item)

        favorite_projects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.favorite_projects, Unset):
            favorite_projects = []
            for favorite_projects_item_data in self.favorite_projects:
                favorite_projects_item = favorite_projects_item_data.to_dict()

                favorite_projects.append(favorite_projects_item)

        end_user_agreement_consent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.end_user_agreement_consent, Unset):
            end_user_agreement_consent = self.end_user_agreement_consent.to_dict()

        erase_timestamp = self.erase_timestamp
        two_factor_authentication: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.two_factor_authentication, Unset):
            two_factor_authentication = self.two_factor_authentication.to_dict()

        required_two_factor_authentication = self.required_two_factor_authentication
        pending_two_factor_authentication: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pending_two_factor_authentication, Unset):
            pending_two_factor_authentication = self.pending_two_factor_authentication.to_dict()

        webauthn_device: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.webauthn_device, Unset):
            webauthn_device = self.webauthn_device.to_dict()

        field_dict: Dict[str, Any] = {}
        _AuthorityHolder_dict = super().to_dict()
        field_dict.update(_AuthorityHolder_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if login is not UNSET:
            field_dict["login"] = login
        if banned is not UNSET:
            field_dict["banned"] = banned
        if ban_reason is not UNSET:
            field_dict["banReason"] = ban_reason
        if ban_badge is not UNSET:
            field_dict["banBadge"] = ban_badge
        if guest is not UNSET:
            field_dict["guest"] = guest
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if profile is not UNSET:
            field_dict["profile"] = profile
        if groups is not UNSET:
            field_dict["groups"] = groups
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if transitive_organizations is not UNSET:
            field_dict["transitiveOrganizations"] = transitive_organizations
        if transitive_groups is not UNSET:
            field_dict["transitiveGroups"] = transitive_groups
        if teams is not UNSET:
            field_dict["teams"] = teams
        if transitive_teams is not UNSET:
            field_dict["transitiveTeams"] = transitive_teams
        if details is not UNSET:
            field_dict["details"] = details
        if vcs_user_names is not UNSET:
            field_dict["VCSUserNames"] = vcs_user_names
        if ssh_public_keys is not UNSET:
            field_dict["sshPublicKeys"] = ssh_public_keys
        if licenses is not UNSET:
            field_dict["licenses"] = licenses
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if last_access_time is not UNSET:
            field_dict["lastAccessTime"] = last_access_time
        if refresh_tokens is not UNSET:
            field_dict["refreshTokens"] = refresh_tokens
        if permanent_tokens is not UNSET:
            field_dict["permanentTokens"] = permanent_tokens
        if approved_scopes is not UNSET:
            field_dict["approvedScopes"] = approved_scopes
        if application_passwords is not UNSET:
            field_dict["applicationPasswords"] = application_passwords
        if favorite_projects is not UNSET:
            field_dict["favoriteProjects"] = favorite_projects
        if end_user_agreement_consent is not UNSET:
            field_dict["endUserAgreementConsent"] = end_user_agreement_consent
        if erase_timestamp is not UNSET:
            field_dict["eraseTimestamp"] = erase_timestamp
        if two_factor_authentication is not UNSET:
            field_dict["twoFactorAuthentication"] = two_factor_authentication
        if required_two_factor_authentication is not UNSET:
            field_dict["requiredTwoFactorAuthentication"] = required_two_factor_authentication
        if pending_two_factor_authentication is not UNSET:
            field_dict["pendingTwoFactorAuthentication"] = pending_two_factor_authentication
        if webauthn_device is not UNSET:
            field_dict["webauthnDevice"] = webauthn_device

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import application_password as application_password_m
            from ..models import approved_scope as approved_scope_m
            from ..models import avatar as avatar_m
            from ..models import details as details_m
            from ..models import end_user_agreement_consent as end_user_agreement_consent_m
            from ..models import license_ as license__m
            from ..models import organization as organization_m
            from ..models import permanent_token as permanent_token_m
            from ..models import profile as profile_m
            from ..models import project as project_m
            from ..models import project_team as project_team_m
            from ..models import refresh_token as refresh_token_m
            from ..models import ssh_public_key as ssh_public_key_m
            from ..models import two_factor_authentication as two_factor_authentication_m
            from ..models import two_factor_authentication_secret as two_factor_authentication_secret_m
            from ..models import user_group as user_group_m
            from ..models import vcs_user_name as vcs_user_name_m
            from ..models import webauthn_device as webauthn_device_m
        except ImportError:
            import sys

            project_m = sys.modules[__package__ + "project"]
            license__m = sys.modules[__package__ + "license_"]
            webauthn_device_m = sys.modules[__package__ + "webauthn_device"]
            permanent_token_m = sys.modules[__package__ + "permanent_token"]
            two_factor_authentication_m = sys.modules[__package__ + "two_factor_authentication"]
            organization_m = sys.modules[__package__ + "organization"]
            project_team_m = sys.modules[__package__ + "project_team"]
            application_password_m = sys.modules[__package__ + "application_password"]
            approved_scope_m = sys.modules[__package__ + "approved_scope"]
            profile_m = sys.modules[__package__ + "profile"]
            ssh_public_key_m = sys.modules[__package__ + "ssh_public_key"]
            user_group_m = sys.modules[__package__ + "user_group"]
            avatar_m = sys.modules[__package__ + "avatar"]
            refresh_token_m = sys.modules[__package__ + "refresh_token"]
            end_user_agreement_consent_m = sys.modules[__package__ + "end_user_agreement_consent"]
            details_m = sys.modules[__package__ + "details"]
            two_factor_authentication_secret_m = sys.modules[__package__ + "two_factor_authentication_secret"]
            vcs_user_name_m = sys.modules[__package__ + "vcs_user_name"]

        d = src_dict.copy()

        _AuthorityHolder_kwargs = super().from_dict(src_dict=d).to_dict()

        login = d.pop("login", UNSET)

        banned = d.pop("banned", UNSET)

        ban_reason = d.pop("banReason", UNSET)

        ban_badge = d.pop("banBadge", UNSET)

        guest = d.pop("guest", UNSET)

        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, avatar_m.Avatar]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = avatar_m.Avatar.from_dict(_avatar)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, profile_m.Profile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = profile_m.Profile.from_dict(_profile)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = user_group_m.UserGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        organizations = []
        _organizations = d.pop("organizations", UNSET)
        for organizations_item_data in _organizations or []:
            organizations_item = organization_m.Organization.from_dict(organizations_item_data)

            organizations.append(organizations_item)

        transitive_organizations = []
        _transitive_organizations = d.pop("transitiveOrganizations", UNSET)
        for transitive_organizations_item_data in _transitive_organizations or []:
            transitive_organizations_item = organization_m.Organization.from_dict(transitive_organizations_item_data)

            transitive_organizations.append(transitive_organizations_item)

        transitive_groups = []
        _transitive_groups = d.pop("transitiveGroups", UNSET)
        for transitive_groups_item_data in _transitive_groups or []:
            transitive_groups_item = user_group_m.UserGroup.from_dict(transitive_groups_item_data)

            transitive_groups.append(transitive_groups_item)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = project_team_m.ProjectTeam.from_dict(teams_item_data)

            teams.append(teams_item)

        transitive_teams = []
        _transitive_teams = d.pop("transitiveTeams", UNSET)
        for transitive_teams_item_data in _transitive_teams or []:
            transitive_teams_item = project_team_m.ProjectTeam.from_dict(transitive_teams_item_data)

            transitive_teams.append(transitive_teams_item)

        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = details_m.Details.from_dict(details_item_data)

            details.append(details_item)

        vcs_user_names = []
        _vcs_user_names = d.pop("VCSUserNames", UNSET)
        for vcs_user_names_item_data in _vcs_user_names or []:
            vcs_user_names_item = vcs_user_name_m.VcsUserName.from_dict(vcs_user_names_item_data)

            vcs_user_names.append(vcs_user_names_item)

        ssh_public_keys = []
        _ssh_public_keys = d.pop("sshPublicKeys", UNSET)
        for ssh_public_keys_item_data in _ssh_public_keys or []:
            ssh_public_keys_item = ssh_public_key_m.SshPublicKey.from_dict(ssh_public_keys_item_data)

            ssh_public_keys.append(ssh_public_keys_item)

        licenses = []
        _licenses = d.pop("licenses", UNSET)
        for licenses_item_data in _licenses or []:
            licenses_item = license__m.License.from_dict(licenses_item_data)

            licenses.append(licenses_item)

        creation_time = d.pop("creationTime", UNSET)

        last_access_time = d.pop("lastAccessTime", UNSET)

        refresh_tokens = []
        _refresh_tokens = d.pop("refreshTokens", UNSET)
        for refresh_tokens_item_data in _refresh_tokens or []:
            refresh_tokens_item = refresh_token_m.RefreshToken.from_dict(refresh_tokens_item_data)

            refresh_tokens.append(refresh_tokens_item)

        permanent_tokens = []
        _permanent_tokens = d.pop("permanentTokens", UNSET)
        for permanent_tokens_item_data in _permanent_tokens or []:
            permanent_tokens_item = permanent_token_m.PermanentToken.from_dict(permanent_tokens_item_data)

            permanent_tokens.append(permanent_tokens_item)

        approved_scopes = []
        _approved_scopes = d.pop("approvedScopes", UNSET)
        for approved_scopes_item_data in _approved_scopes or []:
            approved_scopes_item = approved_scope_m.ApprovedScope.from_dict(approved_scopes_item_data)

            approved_scopes.append(approved_scopes_item)

        application_passwords = []
        _application_passwords = d.pop("applicationPasswords", UNSET)
        for application_passwords_item_data in _application_passwords or []:
            application_passwords_item = application_password_m.ApplicationPassword.from_dict(
                application_passwords_item_data
            )

            application_passwords.append(application_passwords_item)

        favorite_projects = []
        _favorite_projects = d.pop("favoriteProjects", UNSET)
        for favorite_projects_item_data in _favorite_projects or []:
            favorite_projects_item = project_m.Project.from_dict(favorite_projects_item_data)

            favorite_projects.append(favorite_projects_item)

        _end_user_agreement_consent = d.pop("endUserAgreementConsent", UNSET)
        end_user_agreement_consent: Union[Unset, end_user_agreement_consent_m.EndUserAgreementConsent]
        if isinstance(_end_user_agreement_consent, Unset):
            end_user_agreement_consent = UNSET
        else:
            end_user_agreement_consent = end_user_agreement_consent_m.EndUserAgreementConsent.from_dict(
                _end_user_agreement_consent
            )

        erase_timestamp = d.pop("eraseTimestamp", UNSET)

        _two_factor_authentication = d.pop("twoFactorAuthentication", UNSET)
        two_factor_authentication: Union[Unset, two_factor_authentication_m.TwoFactorAuthentication]
        if isinstance(_two_factor_authentication, Unset):
            two_factor_authentication = UNSET
        else:
            two_factor_authentication = two_factor_authentication_m.TwoFactorAuthentication.from_dict(
                _two_factor_authentication
            )

        required_two_factor_authentication = d.pop("requiredTwoFactorAuthentication", UNSET)

        _pending_two_factor_authentication = d.pop("pendingTwoFactorAuthentication", UNSET)
        pending_two_factor_authentication: Union[
            Unset, two_factor_authentication_secret_m.TwoFactorAuthenticationSecret
        ]
        if isinstance(_pending_two_factor_authentication, Unset):
            pending_two_factor_authentication = UNSET
        else:
            pending_two_factor_authentication = (
                two_factor_authentication_secret_m.TwoFactorAuthenticationSecret.from_dict(
                    _pending_two_factor_authentication
                )
            )

        _webauthn_device = d.pop("webauthnDevice", UNSET)
        webauthn_device: Union[Unset, webauthn_device_m.WebauthnDevice]
        if isinstance(_webauthn_device, Unset):
            webauthn_device = UNSET
        else:
            webauthn_device = webauthn_device_m.WebauthnDevice.from_dict(_webauthn_device)

        user = cls(
            login=login,
            banned=banned,
            ban_reason=ban_reason,
            ban_badge=ban_badge,
            guest=guest,
            avatar=avatar,
            profile=profile,
            groups=groups,
            organizations=organizations,
            transitive_organizations=transitive_organizations,
            transitive_groups=transitive_groups,
            teams=teams,
            transitive_teams=transitive_teams,
            details=details,
            vcs_user_names=vcs_user_names,
            ssh_public_keys=ssh_public_keys,
            licenses=licenses,
            creation_time=creation_time,
            last_access_time=last_access_time,
            refresh_tokens=refresh_tokens,
            permanent_tokens=permanent_tokens,
            approved_scopes=approved_scopes,
            application_passwords=application_passwords,
            favorite_projects=favorite_projects,
            end_user_agreement_consent=end_user_agreement_consent,
            erase_timestamp=erase_timestamp,
            two_factor_authentication=two_factor_authentication,
            required_two_factor_authentication=required_two_factor_authentication,
            pending_two_factor_authentication=pending_two_factor_authentication,
            webauthn_device=webauthn_device,
            **_AuthorityHolder_kwargs,
        )

        user.additional_properties = d
        return user

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
