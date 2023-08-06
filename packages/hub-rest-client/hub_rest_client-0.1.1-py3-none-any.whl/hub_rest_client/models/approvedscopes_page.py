from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approved_scope import ApprovedScope
else:
    ApprovedScope = "ApprovedScope"

from ..models.base_page import BasePage

T = TypeVar("T", bound="ApprovedscopesPage")


@attr.s(auto_attribs=True)
class ApprovedscopesPage(BasePage):
    """ """

    approvedscopes: Union[Unset, List[ApprovedScope]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        approvedscopes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.approvedscopes, Unset):
            approvedscopes = []
            for approvedscopes_item_data in self.approvedscopes:
                approvedscopes_item = approvedscopes_item_data.to_dict()

                approvedscopes.append(approvedscopes_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approvedscopes is not UNSET:
            field_dict["approvedscopes"] = approvedscopes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        approvedscopes = []
        _approvedscopes = d.pop("approvedscopes", UNSET)
        for approvedscopes_item_data in _approvedscopes or []:
            approvedscopes_item = ApprovedScope.from_dict(approvedscopes_item_data)

            approvedscopes.append(approvedscopes_item)

        approvedscopes_page = cls(
            approvedscopes=approvedscopes,
            **_BasePage_kwargs,
        )

        approvedscopes_page.additional_properties = d
        return approvedscopes_page

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
