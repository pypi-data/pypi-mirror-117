from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Permission")


@attr.s(auto_attribs=True)
class Permission:
    """ """

    id: "Union[Unset, str]" = UNSET
    aliases: "Union[Unset, List[alias_m.Alias]]" = UNSET
    key: "Union[Unset, str]" = UNSET
    name: "Union[Unset, str]" = UNSET
    service: "Union[Unset, service_m.Service]" = UNSET
    description: "Union[Unset, str]" = UNSET
    global_: "Union[Unset, bool]" = UNSET
    entity_type: "Union[Unset, str]" = UNSET
    operation: "Union[Unset, str]" = UNSET
    implied_permissions: "Union[Unset, List[permission_m.Permission]]" = UNSET
    dependent_permissions: "Union[Unset, List[permission_m.Permission]]" = UNSET

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
        service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.to_dict()

        description = self.description
        global_ = self.global_
        entity_type = self.entity_type
        operation = self.operation
        implied_permissions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.implied_permissions, Unset):
            implied_permissions = []
            for implied_permissions_item_data in self.implied_permissions:
                implied_permissions_item = implied_permissions_item_data.to_dict()

                implied_permissions.append(implied_permissions_item)

        dependent_permissions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dependent_permissions, Unset):
            dependent_permissions = []
            for dependent_permissions_item_data in self.dependent_permissions:
                dependent_permissions_item = dependent_permissions_item_data.to_dict()

                dependent_permissions.append(dependent_permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if service is not UNSET:
            field_dict["service"] = service
        if description is not UNSET:
            field_dict["description"] = description
        if global_ is not UNSET:
            field_dict["global"] = global_
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if operation is not UNSET:
            field_dict["operation"] = operation
        if implied_permissions is not UNSET:
            field_dict["impliedPermissions"] = implied_permissions
        if dependent_permissions is not UNSET:
            field_dict["dependentPermissions"] = dependent_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import alias as alias_m
            from ..models import permission as permission_m
            from ..models import service as service_m
        except ImportError:
            import sys

            alias_m = sys.modules[__package__ + "alias"]
            service_m = sys.modules[__package__ + "service"]
            permission_m = sys.modules[__package__ + "permission"]

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = alias_m.Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        _service = d.pop("service", UNSET)
        service: Union[Unset, service_m.Service]
        if isinstance(_service, Unset):
            service = UNSET
        else:
            service = service_m.Service.from_dict(_service)

        description = d.pop("description", UNSET)

        global_ = d.pop("global", UNSET)

        entity_type = d.pop("entityType", UNSET)

        operation = d.pop("operation", UNSET)

        implied_permissions = []
        _implied_permissions = d.pop("impliedPermissions", UNSET)
        for implied_permissions_item_data in _implied_permissions or []:
            implied_permissions_item = permission_m.Permission.from_dict(implied_permissions_item_data)

            implied_permissions.append(implied_permissions_item)

        dependent_permissions = []
        _dependent_permissions = d.pop("dependentPermissions", UNSET)
        for dependent_permissions_item_data in _dependent_permissions or []:
            dependent_permissions_item = permission_m.Permission.from_dict(dependent_permissions_item_data)

            dependent_permissions.append(dependent_permissions_item)

        permission = cls(
            id=id,
            aliases=aliases,
            key=key,
            name=name,
            service=service,
            description=description,
            global_=global_,
            entity_type=entity_type,
            operation=operation,
            implied_permissions=implied_permissions,
            dependent_permissions=dependent_permissions,
        )

        return permission
