from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileAttribute")


@attr.s(auto_attribs=True)
class ProfileAttribute:
    """ """

    id: "Union[Unset, str]" = UNSET
    aliases: "Union[Unset, List[alias_m.Alias]]" = UNSET
    value: "Union[Unset, str]" = UNSET
    prototype: "Union[Unset, profile_attribute_prototype_m.ProfileAttributePrototype]" = UNSET

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

        try:
            from ..models import alias as alias_m
            from ..models import profile_attribute_prototype as profile_attribute_prototype_m
        except ImportError:
            import sys

            alias_m = sys.modules[__package__ + "alias"]
            profile_attribute_prototype_m = sys.modules[__package__ + "profile_attribute_prototype"]

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = alias_m.Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        value = d.pop("value", UNSET)

        _prototype = d.pop("prototype", UNSET)
        prototype: Union[Unset, profile_attribute_prototype_m.ProfileAttributePrototype]
        if isinstance(_prototype, Unset):
            prototype = UNSET
        else:
            prototype = profile_attribute_prototype_m.ProfileAttributePrototype.from_dict(_prototype)

        profile_attribute = cls(
            id=id,
            aliases=aliases,
            value=value,
            prototype=prototype,
        )

        return profile_attribute
