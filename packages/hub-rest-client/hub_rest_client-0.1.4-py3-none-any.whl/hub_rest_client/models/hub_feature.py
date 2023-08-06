from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HubFeature")


try:
    from ..models import uuid
except ImportError:
    import sys

    uuid = sys.modules[__package__ + "uuid"]


@attr.s(auto_attribs=True)
class HubFeature(uuid.Uuid):
    """ """

    key: "Union[Unset, str]" = UNSET
    name: "Union[Unset, str]" = UNSET
    description: "Union[Unset, str]" = UNSET
    restart_required: "Union[Unset, bool]" = UNSET
    enabled: "Union[Unset, bool]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        name = self.name
        description = self.description
        restart_required = self.restart_required
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        _Uuid_dict = super().to_dict()
        field_dict.update(_Uuid_dict)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if restart_required is not UNSET:
            field_dict["restartRequired"] = restart_required
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        restart_required = d.pop("restartRequired", UNSET)

        enabled = d.pop("enabled", UNSET)

        hub_feature = cls(
            key=key,
            name=name,
            description=description,
            restart_required=restart_required,
            enabled=enabled,
        )

        return hub_feature
