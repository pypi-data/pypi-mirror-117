from typing import Any, Dict, Type, TypeVar, Union

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

    def to_dict(self) -> Dict[str, Any]:
        scope = self.scope
        allowed_organizations = self.allowed_organizations

        field_dict: Dict[str, Any] = {}
        _Externaloauth2module_dict = super().to_dict()
        field_dict.update(_Externaloauth2module_dict)
        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if allowed_organizations is not UNSET:
            field_dict["allowedOrganizations"] = allowed_organizations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _Externaloauth2module_kwargs = super().from_dict(src_dict=d).to_dict()
        _Externaloauth2module_kwargs.pop("$type")

        scope = d.pop("scope", UNSET)

        allowed_organizations = d.pop("allowedOrganizations", UNSET)

        githubauthmodule = cls(
            scope=scope,
            allowed_organizations=allowed_organizations,
            **_Externaloauth2module_kwargs,
        )

        return githubauthmodule
