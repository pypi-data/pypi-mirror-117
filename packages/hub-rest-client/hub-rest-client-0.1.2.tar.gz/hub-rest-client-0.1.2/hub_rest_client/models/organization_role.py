from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationRole")


@attr.s(auto_attribs=True)
class OrganizationRole:
    """ """

    type: "str"
    id: "Union[Unset, str]" = UNSET
    aliases: "Union[Unset, List[alias_m.Alias]]" = UNSET
    role: "Union[Unset, role_m.Role]" = UNSET
    organization: "Union[Unset, organization_m.Organization]" = UNSET
    owner: "Union[Unset, authority_holder_m.AuthorityHolder]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        id = self.id
        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()

                aliases.append(aliases_item)

        role: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if role is not UNSET:
            field_dict["role"] = role
        if organization is not UNSET:
            field_dict["organization"] = organization
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import alias as alias_m
            from ..models import authority_holder as authority_holder_m
            from ..models import organization as organization_m
            from ..models import role as role_m
        except ImportError:
            import sys

            role_m = sys.modules[__package__ + "role"]
            authority_holder_m = sys.modules[__package__ + "authority_holder"]
            alias_m = sys.modules[__package__ + "alias"]
            organization_m = sys.modules[__package__ + "organization"]

        d = src_dict.copy()

        type = d.pop("type")

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = alias_m.Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        _role = d.pop("role", UNSET)
        role: Union[Unset, role_m.Role]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = role_m.Role.from_dict(_role)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, organization_m.Organization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = organization_m.Organization.from_dict(_organization)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, authority_holder_m.AuthorityHolder]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = authority_holder_m.AuthorityHolder.from_dict(_owner)

        organization_role = cls(
            type=type,
            id=id,
            aliases=aliases,
            role=role,
            organization=organization,
            owner=owner,
        )

        organization_role.additional_properties = d
        return organization_role

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
