from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationrolesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class OrganizationrolesPage(base_page.BasePage):
    """ """

    organizationroles: "Union[Unset, List[organization_role_m.OrganizationRole]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organizationroles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organizationroles, Unset):
            organizationroles = []
            for organizationroles_item_data in self.organizationroles:
                organizationroles_item = organizationroles_item_data.to_dict()

                organizationroles.append(organizationroles_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organizationroles is not UNSET:
            field_dict["organizationroles"] = organizationroles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import organization_role as organization_role_m
        except ImportError:
            import sys

            organization_role_m = sys.modules[__package__ + "organization_role"]

        d = src_dict.copy()

        organizationroles = []
        _organizationroles = d.pop("organizationroles", UNSET)
        for organizationroles_item_data in _organizationroles or []:
            organizationroles_item = organization_role_m.OrganizationRole.from_dict(organizationroles_item_data)

            organizationroles.append(organizationroles_item)

        organizationroles_page = cls(
            organizationroles=organizationroles,
        )

        organizationroles_page.additional_properties = d
        return organizationroles_page

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
