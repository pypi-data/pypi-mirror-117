from typing import Any, Dict, List, Type, TypeVar, Union

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
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_user_restrict_domain = self.new_user_restrict_domain

        field_dict: Dict[str, Any] = {}
        _Externaloauth2module_dict = super().to_dict()
        field_dict.update(_Externaloauth2module_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_user_restrict_domain is not UNSET:
            field_dict["newUserRestrictDomain"] = new_user_restrict_domain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        new_user_restrict_domain = d.pop("newUserRestrictDomain", UNSET)

        googleauthmodule = cls(
            new_user_restrict_domain=new_user_restrict_domain,
        )

        googleauthmodule.additional_properties = d
        return googleauthmodule

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
