from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class OrganizationsPage(base_page.BasePage):
    """ """

    organizations: "Union[Unset, List[organization_m.Organization]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organizations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()

                organizations.append(organizations_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organizations is not UNSET:
            field_dict["organizations"] = organizations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import organization as organization_m
        except ImportError:
            import sys

            organization_m = sys.modules[__package__ + "organization"]

        d = src_dict.copy()

        organizations = []
        _organizations = d.pop("organizations", UNSET)
        for organizations_item_data in _organizations or []:
            organizations_item = organization_m.Organization.from_dict(organizations_item_data)

            organizations.append(organizations_item)

        organizations_page = cls(
            organizations=organizations,
        )

        organizations_page.additional_properties = d
        return organizations_page

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
