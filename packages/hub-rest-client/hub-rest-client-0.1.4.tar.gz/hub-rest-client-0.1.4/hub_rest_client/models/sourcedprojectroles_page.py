from typing import Any, Dict, Type, TypeVar, Union

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

        return sourcedprojectroles_page
