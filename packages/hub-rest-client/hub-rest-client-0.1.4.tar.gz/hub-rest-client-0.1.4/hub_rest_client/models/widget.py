from typing import Any, Dict, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Widget")


try:
    from ..models import uuid
except ImportError:
    import sys

    uuid = sys.modules[__package__ + "uuid"]


@attr.s(auto_attribs=True)
class Widget(uuid.Uuid):
    """ """

    key: "Union[Unset, str]" = UNSET
    version: "Union[Unset, str]" = UNSET
    installed_version: "Union[Unset, str]" = UNSET
    latest_version: "Union[Unset, str]" = UNSET
    installed_from_repository: "Union[Unset, bool]" = UNSET
    archive_id: "Union[Unset, str]" = UNSET
    manifest: "Union[Unset, str]" = UNSET
    disabled: "Union[Unset, bool]" = UNSET
    application_names: "Union[Unset, List[str]]" = UNSET
    accessible_services: "Union[Unset, List[service_m.Service]]" = UNSET
    capabilities: "Union[Unset, List[str]]" = UNSET
    repository_url: "Union[Unset, str]" = UNSET
    repository_icon_url: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        version = self.version
        installed_version = self.installed_version
        latest_version = self.latest_version
        installed_from_repository = self.installed_from_repository
        archive_id = self.archive_id
        manifest = self.manifest
        disabled = self.disabled
        application_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.application_names, Unset):
            application_names = self.application_names

        accessible_services: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.accessible_services, Unset):
            accessible_services = []
            for accessible_services_item_data in self.accessible_services:
                accessible_services_item = accessible_services_item_data.to_dict()

                accessible_services.append(accessible_services_item)

        capabilities: Union[Unset, List[str]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities

        repository_url = self.repository_url
        repository_icon_url = self.repository_icon_url

        field_dict: Dict[str, Any] = {}
        _Uuid_dict = super().to_dict()
        field_dict.update(_Uuid_dict)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if version is not UNSET:
            field_dict["version"] = version
        if installed_version is not UNSET:
            field_dict["installedVersion"] = installed_version
        if latest_version is not UNSET:
            field_dict["latestVersion"] = latest_version
        if installed_from_repository is not UNSET:
            field_dict["installedFromRepository"] = installed_from_repository
        if archive_id is not UNSET:
            field_dict["archiveId"] = archive_id
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if application_names is not UNSET:
            field_dict["applicationNames"] = application_names
        if accessible_services is not UNSET:
            field_dict["accessibleServices"] = accessible_services
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if repository_url is not UNSET:
            field_dict["repositoryUrl"] = repository_url
        if repository_icon_url is not UNSET:
            field_dict["repositoryIconUrl"] = repository_icon_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import service as service_m
        except ImportError:
            import sys

            service_m = sys.modules[__package__ + "service"]

        d = src_dict.copy()

        key = d.pop("key", UNSET)

        version = d.pop("version", UNSET)

        installed_version = d.pop("installedVersion", UNSET)

        latest_version = d.pop("latestVersion", UNSET)

        installed_from_repository = d.pop("installedFromRepository", UNSET)

        archive_id = d.pop("archiveId", UNSET)

        manifest = d.pop("manifest", UNSET)

        disabled = d.pop("disabled", UNSET)

        application_names = cast(List[str], d.pop("applicationNames", UNSET))

        accessible_services = []
        _accessible_services = d.pop("accessibleServices", UNSET)
        for accessible_services_item_data in _accessible_services or []:
            accessible_services_item = service_m.Service.from_dict(accessible_services_item_data)

            accessible_services.append(accessible_services_item)

        capabilities = cast(List[str], d.pop("capabilities", UNSET))

        repository_url = d.pop("repositoryUrl", UNSET)

        repository_icon_url = d.pop("repositoryIconUrl", UNSET)

        widget = cls(
            key=key,
            version=version,
            installed_version=installed_version,
            latest_version=latest_version,
            installed_from_repository=installed_from_repository,
            archive_id=archive_id,
            manifest=manifest,
            disabled=disabled,
            application_names=application_names,
            accessible_services=accessible_services,
            capabilities=capabilities,
            repository_url=repository_url,
            repository_icon_url=repository_icon_url,
        )

        return widget
