from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthmodulesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class AuthmodulesPage(base_page.BasePage):
    """ """

    authmodules: "Union[Unset, List[authmodule_m.Authmodule]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authmodules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.authmodules, Unset):
            authmodules = []
            for authmodules_item_data in self.authmodules:
                authmodules_item = authmodules_item_data.to_dict()

                authmodules.append(authmodules_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authmodules is not UNSET:
            field_dict["authmodules"] = authmodules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import authmodule as authmodule_m
        except ImportError:
            import sys

            authmodule_m = sys.modules[__package__ + "authmodule"]

        d = src_dict.copy()

        authmodules = []
        _authmodules = d.pop("authmodules", UNSET)
        for authmodules_item_data in _authmodules or []:
            authmodules_item = authmodule_m.Authmodule.from_dict(authmodules_item_data)

            authmodules.append(authmodules_item)

        authmodules_page = cls(
            authmodules=authmodules,
        )

        authmodules_page.additional_properties = d
        return authmodules_page

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
