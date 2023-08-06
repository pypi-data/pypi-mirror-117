from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Googleauthmodule")


try:
    from ..models import externaloauth_2_module
except ImportError:
    import sys

    externaloauth_2_module = sys.modules[__package__ + "externaloauth_2_module"]


@attr.s(auto_attribs=True)
class Googleauthmodule(externaloauth_2_module.Externaloauth2module):
    """ """

    new_user_restrict_domain: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        new_user_restrict_domain = self.new_user_restrict_domain

        field_dict: Dict[str, Any] = {}
        _Externaloauth2module_dict = super().to_dict()
        field_dict.update(_Externaloauth2module_dict)
        field_dict.update({})
        if new_user_restrict_domain is not UNSET:
            field_dict["newUserRestrictDomain"] = new_user_restrict_domain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _Externaloauth2module_kwargs = super().from_dict(src_dict=d).to_dict()
        _Externaloauth2module_kwargs.pop("$type")

        new_user_restrict_domain = d.pop("newUserRestrictDomain", UNSET)

        googleauthmodule = cls(
            new_user_restrict_domain=new_user_restrict_domain,
            **_Externaloauth2module_kwargs,
        )

        return googleauthmodule
