from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.uuid import Uuid
from ..types import UNSET, Unset

T = TypeVar("T", bound="HubFeature")


@attr.s(auto_attribs=True)
class HubFeature(Uuid):
    """ """

    key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    restart_required: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        name = self.name
        description = self.description
        restart_required = self.restart_required
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        _Uuid_dict = super(Uuid).to_dict()
        field_dict.update(_Uuid_dict)
        field_dict.update(self.additional_properties)
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

        _Uuid_kwargs = super(Uuid).from_dict(src_dict=d).to_dict()

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
            **_Uuid_kwargs,
        )

        hub_feature.additional_properties = d
        return hub_feature

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
