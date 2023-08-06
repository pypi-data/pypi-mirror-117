from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Githubauthmodule")


try:
    from ..models import externaloauth_2_module
except ImportError:
    import sys

    externaloauth_2_module = sys.modules[__package__ + "externaloauth_2_module"]


@attr.s(auto_attribs=True)
class Githubauthmodule(externaloauth_2_module.Externaloauth2module):
    """ """

    scope: "Union[Unset, str]" = UNSET
    allowed_organizations: "Union[Unset, str]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scope = self.scope
        allowed_organizations = self.allowed_organizations

        field_dict: Dict[str, Any] = {}
        _Externaloauth2module_dict = super().to_dict()
        field_dict.update(_Externaloauth2module_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if allowed_organizations is not UNSET:
            field_dict["allowedOrganizations"] = allowed_organizations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        scope = d.pop("scope", UNSET)

        allowed_organizations = d.pop("allowedOrganizations", UNSET)

        githubauthmodule = cls(
            scope=scope,
            allowed_organizations=allowed_organizations,
        )

        githubauthmodule.additional_properties = d
        return githubauthmodule

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
