from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Resource")


@attr.s(auto_attribs=True)
class Resource:
    """ """

    id: "Union[Unset, str]" = UNSET
    aliases: "Union[Unset, List[alias_m.Alias]]" = UNSET
    key: "Union[Unset, str]" = UNSET
    name: "Union[Unset, str]" = UNSET
    home_url: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET
    service: "Union[Unset, service_m.Service]" = UNSET
    project: "Union[Unset, project_m.Project]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()

                aliases.append(aliases_item)

        key = self.key
        name = self.name
        home_url = self.home_url
        type = self.type
        service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if home_url is not UNSET:
            field_dict["homeUrl"] = home_url
        if type is not UNSET:
            field_dict["type"] = type
        if service is not UNSET:
            field_dict["service"] = service
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import alias as alias_m
            from ..models import project as project_m
            from ..models import service as service_m
        except ImportError:
            import sys

            service_m = sys.modules[__package__ + "service"]
            alias_m = sys.modules[__package__ + "alias"]
            project_m = sys.modules[__package__ + "project"]

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = alias_m.Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        home_url = d.pop("homeUrl", UNSET)

        type = d.pop("type", UNSET)

        _service = d.pop("service", UNSET)
        service: Union[Unset, service_m.Service]
        if isinstance(_service, Unset):
            service = UNSET
        else:
            service = service_m.Service.from_dict(_service)

        _project = d.pop("project", UNSET)
        project: Union[Unset, project_m.Project]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = project_m.Project.from_dict(_project)

        resource = cls(
            id=id,
            aliases=aliases,
            key=key,
            name=name,
            home_url=home_url,
            type=type,
            service=service,
            project=project,
        )

        resource.additional_properties = d
        return resource

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
