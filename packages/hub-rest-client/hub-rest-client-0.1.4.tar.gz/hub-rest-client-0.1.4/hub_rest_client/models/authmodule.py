from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Authmodule")


@attr.s(auto_attribs=True)
class Authmodule:
    """ """

    type: "str"
    id: "Union[Unset, str]" = UNSET
    aliases: "Union[Unset, List[alias_m.Alias]]" = UNSET
    name: "Union[Unset, str]" = UNSET
    ordinal: "Union[Unset, int]" = UNSET
    accounts_size: "Union[Unset, int]" = UNSET
    disabled: "Union[Unset, bool]" = UNSET
    auto_join_groups: "Union[Unset, List[user_group_m.UserGroup]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        id = self.id
        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()

                aliases.append(aliases_item)

        name = self.name
        ordinal = self.ordinal
        accounts_size = self.accounts_size
        disabled = self.disabled
        auto_join_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.auto_join_groups, Unset):
            auto_join_groups = []
            for auto_join_groups_item_data in self.auto_join_groups:
                auto_join_groups_item = auto_join_groups_item_data.to_dict()

                auto_join_groups.append(auto_join_groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if name is not UNSET:
            field_dict["name"] = name
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if accounts_size is not UNSET:
            field_dict["accountsSize"] = accounts_size
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if auto_join_groups is not UNSET:
            field_dict["autoJoinGroups"] = auto_join_groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import alias as alias_m
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            user_group_m = sys.modules[__package__ + "user_group"]
            alias_m = sys.modules[__package__ + "alias"]

        d = src_dict.copy()

        type = d.pop("type")

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = alias_m.Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        name = d.pop("name", UNSET)

        ordinal = d.pop("ordinal", UNSET)

        accounts_size = d.pop("accountsSize", UNSET)

        disabled = d.pop("disabled", UNSET)

        auto_join_groups = []
        _auto_join_groups = d.pop("autoJoinGroups", UNSET)
        for auto_join_groups_item_data in _auto_join_groups or []:
            auto_join_groups_item = user_group_m.UserGroup.from_dict(auto_join_groups_item_data)

            auto_join_groups.append(auto_join_groups_item)

        authmodule = cls(
            type=type,
            id=id,
            aliases=aliases,
            name=name,
            ordinal=ordinal,
            accounts_size=accounts_size,
            disabled=disabled,
            auto_join_groups=auto_join_groups,
        )

        return authmodule
