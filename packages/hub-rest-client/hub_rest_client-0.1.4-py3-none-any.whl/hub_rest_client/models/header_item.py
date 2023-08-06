from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeaderItem")


@attr.s(auto_attribs=True)
class HeaderItem:
    """ """

    id: "Union[Unset, str]" = UNSET
    aliases: "Union[Unset, List[alias_m.Alias]]" = UNSET
    name: "Union[Unset, str]" = UNSET
    home_url: "Union[Unset, str]" = UNSET
    icon_url: "Union[Unset, str]" = UNSET
    application_name: "Union[Unset, str]" = UNSET
    vendor: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()

                aliases.append(aliases_item)

        name = self.name
        home_url = self.home_url
        icon_url = self.icon_url
        application_name = self.application_name
        vendor = self.vendor

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if name is not UNSET:
            field_dict["name"] = name
        if home_url is not UNSET:
            field_dict["homeUrl"] = home_url
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if application_name is not UNSET:
            field_dict["applicationName"] = application_name
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

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

        home_url = d.pop("homeUrl", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        application_name = d.pop("applicationName", UNSET)

        vendor = d.pop("vendor", UNSET)

        header_item = cls(
            id=id,
            aliases=aliases,
            name=name,
            home_url=home_url,
            icon_url=icon_url,
            application_name=application_name,
            vendor=vendor,
        )

        return header_item
