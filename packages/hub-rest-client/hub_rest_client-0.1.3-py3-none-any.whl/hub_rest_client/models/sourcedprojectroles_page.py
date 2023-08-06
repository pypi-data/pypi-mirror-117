from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcedprojectrolesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class SourcedprojectrolesPage(base_page.BasePage):
    """ """

    sourcedprojectroles: "Union[Unset, List[sourced_project_role_m.SourcedProjectRole]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sourcedprojectroles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sourcedprojectroles, Unset):
            sourcedprojectroles = []
            for sourcedprojectroles_item_data in self.sourcedprojectroles:
                sourcedprojectroles_item = sourcedprojectroles_item_data.to_dict()

                sourcedprojectroles.append(sourcedprojectroles_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sourcedprojectroles is not UNSET:
            field_dict["sourcedprojectroles"] = sourcedprojectroles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import sourced_project_role as sourced_project_role_m
        except ImportError:
            import sys

            sourced_project_role_m = sys.modules[__package__ + "sourced_project_role"]

        d = src_dict.copy()

        sourcedprojectroles = []
        _sourcedprojectroles = d.pop("sourcedprojectroles", UNSET)
        for sourcedprojectroles_item_data in _sourcedprojectroles or []:
            sourcedprojectroles_item = sourced_project_role_m.SourcedProjectRole.from_dict(
                sourcedprojectroles_item_data
            )

            sourcedprojectroles.append(sourcedprojectroles_item)

        sourcedprojectroles_page = cls(
            sourcedprojectroles=sourcedprojectroles,
        )

        sourcedprojectroles_page.additional_properties = d
        return sourcedprojectroles_page

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
