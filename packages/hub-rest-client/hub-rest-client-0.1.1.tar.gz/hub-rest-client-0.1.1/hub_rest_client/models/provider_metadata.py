from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.uuid import Uuid
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderMetadata")


@attr.s(auto_attribs=True)
class ProviderMetadata(Uuid):
    """ """

    entity_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_id = self.entity_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        _Uuid_dict = super(Uuid).to_dict()
        field_dict.update(_Uuid_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Uuid_kwargs = super(Uuid).from_dict(src_dict=d).to_dict()

        entity_id = d.pop("entityId", UNSET)

        name = d.pop("name", UNSET)

        provider_metadata = cls(
            entity_id=entity_id,
            name=name,
            **_Uuid_kwargs,
        )

        provider_metadata.additional_properties = d
        return provider_metadata

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
