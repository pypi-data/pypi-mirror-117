from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileAttributePrototype")


@attr.s(auto_attribs=True)
class ProfileAttributePrototype:
    """ """

    id: "Union[Unset, str]" = UNSET
    aliases: "Union[Unset, List[alias_m.Alias]]" = UNSET
    name: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET
    show_on_user_list: "Union[Unset, bool]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()

                aliases.append(aliases_item)

        name = self.name
        type = self.type
        show_on_user_list = self.show_on_user_list

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if show_on_user_list is not UNSET:
            field_dict["showOnUserList"] = show_on_user_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import alias as alias_m
        except ImportError:
            import sys

            alias_m = sys.modules[__package__ + "alias"]

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = alias_m.Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        show_on_user_list = d.pop("showOnUserList", UNSET)

        profile_attribute_prototype = cls(
            id=id,
            aliases=aliases,
            name=name,
            type=type,
            show_on_user_list=show_on_user_list,
        )

        return profile_attribute_prototype
