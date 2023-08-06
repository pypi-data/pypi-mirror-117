from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransitiveprojectrolesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class TransitiveprojectrolesPage(base_page.BasePage):
    """ """

    transitiveprojectroles: "Union[Unset, List[project_role_m.ProjectRole]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        transitiveprojectroles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transitiveprojectroles, Unset):
            transitiveprojectroles = []
            for transitiveprojectroles_item_data in self.transitiveprojectroles:
                transitiveprojectroles_item = transitiveprojectroles_item_data.to_dict()

                transitiveprojectroles.append(transitiveprojectroles_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if transitiveprojectroles is not UNSET:
            field_dict["transitiveprojectroles"] = transitiveprojectroles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import project_role as project_role_m
        except ImportError:
            import sys

            project_role_m = sys.modules[__package__ + "project_role"]

        d = src_dict.copy()

        _BasePage_kwargs = super().from_dict(src_dict=d).to_dict()
        _BasePage_kwargs.pop("$type")

        transitiveprojectroles = []
        _transitiveprojectroles = d.pop("transitiveprojectroles", UNSET)
        for transitiveprojectroles_item_data in _transitiveprojectroles or []:
            transitiveprojectroles_item = project_role_m.ProjectRole.from_dict(transitiveprojectroles_item_data)

            transitiveprojectroles.append(transitiveprojectroles_item)

        transitiveprojectroles_page = cls(
            transitiveprojectroles=transitiveprojectroles,
            **_BasePage_kwargs,
        )

        return transitiveprojectroles_page
