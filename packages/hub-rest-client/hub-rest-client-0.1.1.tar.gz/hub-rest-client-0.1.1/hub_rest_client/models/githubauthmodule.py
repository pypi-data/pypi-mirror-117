from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.externaloauth_2_module import Externaloauth2module
from ..types import UNSET, Unset

T = TypeVar("T", bound="Githubauthmodule")


@attr.s(auto_attribs=True)
class Githubauthmodule(Externaloauth2module):
    """ """

    scope: Union[Unset, str] = UNSET
    allowed_organizations: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scope = self.scope
        allowed_organizations = self.allowed_organizations

        field_dict: Dict[str, Any] = {}
        _Externaloauth2module_dict = super(Externaloauth2module).to_dict()
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

        _Externaloauth2module_kwargs = super(Externaloauth2module).from_dict(src_dict=d).to_dict()

        scope = d.pop("scope", UNSET)

        allowed_organizations = d.pop("allowedOrganizations", UNSET)

        githubauthmodule = cls(
            scope=scope,
            allowed_organizations=allowed_organizations,
            **_Externaloauth2module_kwargs,
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
