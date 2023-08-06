from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Locale")


@attr.s(auto_attribs=True)
class Locale:
    """ """

    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    community: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        label = self.label
        language = self.language
        region = self.region
        community = self.community

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if language is not UNSET:
            field_dict["language"] = language
        if region is not UNSET:
            field_dict["region"] = region
        if community is not UNSET:
            field_dict["community"] = community

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        language = d.pop("language", UNSET)

        region = d.pop("region", UNSET)

        community = d.pop("community", UNSET)

        locale = cls(
            name=name,
            label=label,
            language=language,
            region=region,
            community=community,
        )

        locale.additional_properties = d
        return locale

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
