from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_module_group_mapping import AuthModuleGroupMapping
else:
    AuthModuleGroupMapping = "AuthModuleGroupMapping"

from ..models.base_page import BasePage

T = TypeVar("T", bound="GroupmappingsPage")


@attr.s(auto_attribs=True)
class GroupmappingsPage(BasePage):
    """ """

    groupmappings: Union[Unset, List[AuthModuleGroupMapping]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        groupmappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groupmappings, Unset):
            groupmappings = []
            for groupmappings_item_data in self.groupmappings:
                groupmappings_item = groupmappings_item_data.to_dict()

                groupmappings.append(groupmappings_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groupmappings is not UNSET:
            field_dict["groupmappings"] = groupmappings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        groupmappings = []
        _groupmappings = d.pop("groupmappings", UNSET)
        for groupmappings_item_data in _groupmappings or []:
            groupmappings_item = AuthModuleGroupMapping.from_dict(groupmappings_item_data)

            groupmappings.append(groupmappings_item)

        groupmappings_page = cls(
            groupmappings=groupmappings,
            **_BasePage_kwargs,
        )

        groupmappings_page.additional_properties = d
        return groupmappings_page

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
