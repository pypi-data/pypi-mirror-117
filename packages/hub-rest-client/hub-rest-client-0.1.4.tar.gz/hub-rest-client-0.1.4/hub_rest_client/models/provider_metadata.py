from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderMetadata")


try:
    from ..models import uuid
except ImportError:
    import sys

    uuid = sys.modules[__package__ + "uuid"]


@attr.s(auto_attribs=True)
class ProviderMetadata(uuid.Uuid):
    """ """

    entity_id: "Union[Unset, str]" = UNSET
    name: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        entity_id = self.entity_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        _Uuid_dict = super().to_dict()
        field_dict.update(_Uuid_dict)
        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        entity_id = d.pop("entityId", UNSET)

        name = d.pop("name", UNSET)

        provider_metadata = cls(
            entity_id=entity_id,
            name=name,
        )

        return provider_metadata
