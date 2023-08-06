from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Counters")


@attr.s(auto_attribs=True)
class Counters:
    """ """

    users: Union[Unset, int] = UNSET
    groups: Union[Unset, int] = UNSET
    roles: Union[Unset, int] = UNSET
    projects: Union[Unset, int] = UNSET
    services: Union[Unset, int] = UNSET
    auth_modules: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        users = self.users
        groups = self.groups
        roles = self.roles
        projects = self.projects
        services = self.services
        auth_modules = self.auth_modules

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users
        if groups is not UNSET:
            field_dict["groups"] = groups
        if roles is not UNSET:
            field_dict["roles"] = roles
        if projects is not UNSET:
            field_dict["projects"] = projects
        if services is not UNSET:
            field_dict["services"] = services
        if auth_modules is not UNSET:
            field_dict["authModules"] = auth_modules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        users = d.pop("users", UNSET)

        groups = d.pop("groups", UNSET)

        roles = d.pop("roles", UNSET)

        projects = d.pop("projects", UNSET)

        services = d.pop("services", UNSET)

        auth_modules = d.pop("authModules", UNSET)

        counters = cls(
            users=users,
            groups=groups,
            roles=roles,
            projects=projects,
            services=services,
            auth_modules=auth_modules,
        )

        counters.additional_properties = d
        return counters

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
