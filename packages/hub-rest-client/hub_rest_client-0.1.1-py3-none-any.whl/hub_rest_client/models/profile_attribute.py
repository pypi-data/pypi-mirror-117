from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alias import Alias
    from ..models.profile_attribute_prototype import ProfileAttributePrototype
else:
    ProfileAttributePrototype = "ProfileAttributePrototype"
    Alias = "Alias"


T = TypeVar("T", bound="ProfileAttribute")


@attr.s(auto_attribs=True)
class ProfileAttribute:
    """ """

    id: Union[Unset, str] = UNSET
    aliases: Union[Unset, List[Alias]] = UNSET
    value: Union[Unset, str] = UNSET
    prototype: Union[Unset, ProfileAttributePrototype] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()

                aliases.append(aliases_item)

        value = self.value
        prototype: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prototype, Unset):
            prototype = self.prototype.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if value is not UNSET:
            field_dict["value"] = value
        if prototype is not UNSET:
            field_dict["prototype"] = prototype

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        value = d.pop("value", UNSET)

        _prototype = d.pop("prototype", UNSET)
        prototype: Union[Unset, ProfileAttributePrototype]
        if isinstance(_prototype, Unset):
            prototype = UNSET
        else:
            prototype = ProfileAttributePrototype.from_dict(_prototype)

        profile_attribute = cls(
            id=id,
            aliases=aliases,
            value=value,
            prototype=prototype,
        )

        profile_attribute.additional_properties = d
        return profile_attribute

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
