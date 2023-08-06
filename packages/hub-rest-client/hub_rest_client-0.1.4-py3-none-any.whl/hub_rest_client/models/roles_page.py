from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RolesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class RolesPage(base_page.BasePage):
    """ """

    roles: "Union[Unset, List[role_m.Role]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()

                roles.append(roles_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import role as role_m
        except ImportError:
            import sys

            role_m = sys.modules[__package__ + "role"]

        d = src_dict.copy()

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = role_m.Role.from_dict(roles_item_data)

            roles.append(roles_item)

        roles_page = cls(
            roles=roles,
        )

        return roles_page
