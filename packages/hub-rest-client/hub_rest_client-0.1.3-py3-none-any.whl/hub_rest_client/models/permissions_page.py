from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PermissionsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class PermissionsPage(base_page.BasePage):
    """ """

    permissions: "Union[Unset, List[permission_m.Permission]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permissions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()

                permissions.append(permissions_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import permission as permission_m
        except ImportError:
            import sys

            permission_m = sys.modules[__package__ + "permission"]

        d = src_dict.copy()

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = permission_m.Permission.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        permissions_page = cls(
            permissions=permissions,
        )

        permissions_page.additional_properties = d
        return permissions_page

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
