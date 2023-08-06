from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authority_holder import AuthorityHolder
    from ..models.license_ import License
    from ..models.permission import Permission
    from ..models.resource import Resource
    from ..models.role import Role
    from ..models.untrusted_redirect_uri import UntrustedRedirectURI
else:
    UntrustedRedirectURI = "UntrustedRedirectURI"
    AuthorityHolder = "AuthorityHolder"
    Role = "Role"
    Resource = "Resource"
    License = "License"
    Permission = "Permission"

from ..models.authority_holder import AuthorityHolder

T = TypeVar("T", bound="Service")


@attr.s(auto_attribs=True)
class Service(AuthorityHolder):
    """ """

    key: Union[Unset, str] = UNSET
    home_url: Union[Unset, str] = UNSET
    base_urls: Union[Unset, List[str]] = UNSET
    user_uri_pattern: Union[Unset, str] = UNSET
    group_uri_pattern: Union[Unset, str] = UNSET
    redirect_uris: Union[Unset, List[str]] = UNSET
    untrusted_redirect_uris: Union[Unset, List[UntrustedRedirectURI]] = UNSET
    application_name: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    release_date: Union[Unset, int] = UNSET
    version: Union[Unset, str] = UNSET
    icon_url: Union[Unset, str] = UNSET
    resources: Union[Unset, List[Resource]] = UNSET
    permissions: Union[Unset, List[Permission]] = UNSET
    default_roles: Union[Unset, List[Role]] = UNSET
    viewers: Union[Unset, List[AuthorityHolder]] = UNSET
    license_settings: Union[Unset, License] = UNSET
    trusted: Union[Unset, bool] = UNSET
    secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        home_url = self.home_url
        base_urls: Union[Unset, List[str]] = UNSET
        if not isinstance(self.base_urls, Unset):
            base_urls = self.base_urls

        user_uri_pattern = self.user_uri_pattern
        group_uri_pattern = self.group_uri_pattern
        redirect_uris: Union[Unset, List[str]] = UNSET
        if not isinstance(self.redirect_uris, Unset):
            redirect_uris = self.redirect_uris

        untrusted_redirect_uris: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.untrusted_redirect_uris, Unset):
            untrusted_redirect_uris = []
            for untrusted_redirect_uris_item_data in self.untrusted_redirect_uris:
                untrusted_redirect_uris_item = untrusted_redirect_uris_item_data.to_dict()

                untrusted_redirect_uris.append(untrusted_redirect_uris_item)

        application_name = self.application_name
        vendor = self.vendor
        release_date = self.release_date
        version = self.version
        icon_url = self.icon_url
        resources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()

                resources.append(resources_item)

        permissions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()

                permissions.append(permissions_item)

        default_roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.default_roles, Unset):
            default_roles = []
            for default_roles_item_data in self.default_roles:
                default_roles_item = default_roles_item_data.to_dict()

                default_roles.append(default_roles_item)

        viewers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.viewers, Unset):
            viewers = []
            for viewers_item_data in self.viewers:
                viewers_item = viewers_item_data.to_dict()

                viewers.append(viewers_item)

        license_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.license_settings, Unset):
            license_settings = self.license_settings.to_dict()

        trusted = self.trusted
        secret = self.secret

        field_dict: Dict[str, Any] = {}
        _AuthorityHolder_dict = super(AuthorityHolder).to_dict()
        field_dict.update(_AuthorityHolder_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if home_url is not UNSET:
            field_dict["homeUrl"] = home_url
        if base_urls is not UNSET:
            field_dict["baseUrls"] = base_urls
        if user_uri_pattern is not UNSET:
            field_dict["userUriPattern"] = user_uri_pattern
        if group_uri_pattern is not UNSET:
            field_dict["groupUriPattern"] = group_uri_pattern
        if redirect_uris is not UNSET:
            field_dict["redirectUris"] = redirect_uris
        if untrusted_redirect_uris is not UNSET:
            field_dict["untrustedRedirectUris"] = untrusted_redirect_uris
        if application_name is not UNSET:
            field_dict["applicationName"] = application_name
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if version is not UNSET:
            field_dict["version"] = version
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if resources is not UNSET:
            field_dict["resources"] = resources
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if default_roles is not UNSET:
            field_dict["defaultRoles"] = default_roles
        if viewers is not UNSET:
            field_dict["viewers"] = viewers
        if license_settings is not UNSET:
            field_dict["licenseSettings"] = license_settings
        if trusted is not UNSET:
            field_dict["trusted"] = trusted
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _AuthorityHolder_kwargs = super(AuthorityHolder).from_dict(src_dict=d).to_dict()

        key = d.pop("key", UNSET)

        home_url = d.pop("homeUrl", UNSET)

        base_urls = cast(List[str], d.pop("baseUrls", UNSET))

        user_uri_pattern = d.pop("userUriPattern", UNSET)

        group_uri_pattern = d.pop("groupUriPattern", UNSET)

        redirect_uris = cast(List[str], d.pop("redirectUris", UNSET))

        untrusted_redirect_uris = []
        _untrusted_redirect_uris = d.pop("untrustedRedirectUris", UNSET)
        for untrusted_redirect_uris_item_data in _untrusted_redirect_uris or []:
            untrusted_redirect_uris_item = UntrustedRedirectURI.from_dict(untrusted_redirect_uris_item_data)

            untrusted_redirect_uris.append(untrusted_redirect_uris_item)

        application_name = d.pop("applicationName", UNSET)

        vendor = d.pop("vendor", UNSET)

        release_date = d.pop("releaseDate", UNSET)

        version = d.pop("version", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        resources = []
        _resources = d.pop("resources", UNSET)
        for resources_item_data in _resources or []:
            resources_item = Resource.from_dict(resources_item_data)

            resources.append(resources_item)

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = Permission.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        default_roles = []
        _default_roles = d.pop("defaultRoles", UNSET)
        for default_roles_item_data in _default_roles or []:
            default_roles_item = Role.from_dict(default_roles_item_data)

            default_roles.append(default_roles_item)

        viewers = []
        _viewers = d.pop("viewers", UNSET)
        for viewers_item_data in _viewers or []:
            viewers_item = AuthorityHolder.from_dict(viewers_item_data)

            viewers.append(viewers_item)

        _license_settings = d.pop("licenseSettings", UNSET)
        license_settings: Union[Unset, License]
        if isinstance(_license_settings, Unset):
            license_settings = UNSET
        else:
            license_settings = License.from_dict(_license_settings)

        trusted = d.pop("trusted", UNSET)

        secret = d.pop("secret", UNSET)

        service = cls(
            key=key,
            home_url=home_url,
            base_urls=base_urls,
            user_uri_pattern=user_uri_pattern,
            group_uri_pattern=group_uri_pattern,
            redirect_uris=redirect_uris,
            untrusted_redirect_uris=untrusted_redirect_uris,
            application_name=application_name,
            vendor=vendor,
            release_date=release_date,
            version=version,
            icon_url=icon_url,
            resources=resources,
            permissions=permissions,
            default_roles=default_roles,
            viewers=viewers,
            license_settings=license_settings,
            trusted=trusted,
            secret=secret,
            **_AuthorityHolder_kwargs,
        )

        service.additional_properties = d
        return service

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
