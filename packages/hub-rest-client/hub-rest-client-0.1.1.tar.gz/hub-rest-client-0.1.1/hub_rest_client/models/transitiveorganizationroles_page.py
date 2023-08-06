from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_role import OrganizationRole
else:
    OrganizationRole = "OrganizationRole"

from ..models.base_page import BasePage

T = TypeVar("T", bound="TransitiveorganizationrolesPage")


@attr.s(auto_attribs=True)
class TransitiveorganizationrolesPage(BasePage):
    """ """

    transitiveorganizationroles: Union[Unset, List[OrganizationRole]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transitiveorganizationroles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transitiveorganizationroles, Unset):
            transitiveorganizationroles = []
            for transitiveorganizationroles_item_data in self.transitiveorganizationroles:
                transitiveorganizationroles_item = transitiveorganizationroles_item_data.to_dict()

                transitiveorganizationroles.append(transitiveorganizationroles_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transitiveorganizationroles is not UNSET:
            field_dict["transitiveorganizationroles"] = transitiveorganizationroles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        transitiveorganizationroles = []
        _transitiveorganizationroles = d.pop("transitiveorganizationroles", UNSET)
        for transitiveorganizationroles_item_data in _transitiveorganizationroles or []:
            transitiveorganizationroles_item = OrganizationRole.from_dict(transitiveorganizationroles_item_data)

            transitiveorganizationroles.append(transitiveorganizationroles_item)

        transitiveorganizationroles_page = cls(
            transitiveorganizationroles=transitiveorganizationroles,
            **_BasePage_kwargs,
        )

        transitiveorganizationroles_page.additional_properties = d
        return transitiveorganizationroles_page

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
