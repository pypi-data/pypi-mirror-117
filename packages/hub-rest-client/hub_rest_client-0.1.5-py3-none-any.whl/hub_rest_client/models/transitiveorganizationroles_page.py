from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransitiveorganizationrolesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class TransitiveorganizationrolesPage(base_page.BasePage):
    """ """

    transitiveorganizationroles: "Union[Unset, List[organization_role_m.OrganizationRole]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        transitiveorganizationroles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transitiveorganizationroles, Unset):
            transitiveorganizationroles = []
            for transitiveorganizationroles_item_data in self.transitiveorganizationroles:
                transitiveorganizationroles_item = transitiveorganizationroles_item_data.to_dict()

                transitiveorganizationroles.append(transitiveorganizationroles_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if transitiveorganizationroles is not UNSET:
            field_dict["transitiveorganizationroles"] = transitiveorganizationroles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import organization_role as organization_role_m
        except ImportError:
            import sys

            organization_role_m = sys.modules[__package__ + "organization_role"]

        d = src_dict.copy()

        _BasePage_kwargs = super().from_dict(src_dict=d).to_dict()
        _BasePage_kwargs.pop("$type")

        transitiveorganizationroles = []
        _transitiveorganizationroles = d.pop("transitiveorganizationroles", UNSET)
        for transitiveorganizationroles_item_data in _transitiveorganizationroles or []:
            transitiveorganizationroles_item = organization_role_m.OrganizationRole.from_dict(
                transitiveorganizationroles_item_data
            )

            transitiveorganizationroles.append(transitiveorganizationroles_item)

        transitiveorganizationroles_page = cls(
            transitiveorganizationroles=transitiveorganizationroles,
            **_BasePage_kwargs,
        )

        return transitiveorganizationroles_page
