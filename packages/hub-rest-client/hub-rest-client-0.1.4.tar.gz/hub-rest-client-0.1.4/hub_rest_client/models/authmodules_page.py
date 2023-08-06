from typing import Any, Dict, Type, TypeVar, Union

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

        return authmodules_page
