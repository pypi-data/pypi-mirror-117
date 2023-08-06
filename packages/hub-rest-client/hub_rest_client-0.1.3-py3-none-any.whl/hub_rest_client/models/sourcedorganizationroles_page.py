from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcedorganizationrolesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class SourcedorganizationrolesPage(base_page.BasePage):
    """ """

    sourcedorganizationroles: "Union[Unset, List[sourced_organization_role_m.SourcedOrganizationRole]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sourcedorganizationroles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sourcedorganizationroles, Unset):
            sourcedorganizationroles = []
            for sourcedorganizationroles_item_data in self.sourcedorganizationroles:
                sourcedorganizationroles_item = sourcedorganizationroles_item_data.to_dict()

                sourcedorganizationroles.append(sourcedorganizationroles_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sourcedorganizationroles is not UNSET:
            field_dict["sourcedorganizationroles"] = sourcedorganizationroles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import sourced_organization_role as sourced_organization_role_m
        except ImportError:
            import sys

            sourced_organization_role_m = sys.modules[__package__ + "sourced_organization_role"]

        d = src_dict.copy()

        sourcedorganizationroles = []
        _sourcedorganizationroles = d.pop("sourcedorganizationroles", UNSET)
        for sourcedorganizationroles_item_data in _sourcedorganizationroles or []:
            sourcedorganizationroles_item = sourced_organization_role_m.SourcedOrganizationRole.from_dict(
                sourcedorganizationroles_item_data
            )

            sourcedorganizationroles.append(sourcedorganizationroles_item)

        sourcedorganizationroles_page = cls(
            sourcedorganizationroles=sourcedorganizationroles,
        )

        sourcedorganizationroles_page.additional_properties = d
        return sourcedorganizationroles_page

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
