from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupmappingsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class GroupmappingsPage(base_page.BasePage):
    """ """

    groupmappings: "Union[Unset, List[auth_module_group_mapping_m.AuthModuleGroupMapping]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        groupmappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groupmappings, Unset):
            groupmappings = []
            for groupmappings_item_data in self.groupmappings:
                groupmappings_item = groupmappings_item_data.to_dict()

                groupmappings.append(groupmappings_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if groupmappings is not UNSET:
            field_dict["groupmappings"] = groupmappings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import auth_module_group_mapping as auth_module_group_mapping_m
        except ImportError:
            import sys

            auth_module_group_mapping_m = sys.modules[__package__ + "auth_module_group_mapping"]

        d = src_dict.copy()

        groupmappings = []
        _groupmappings = d.pop("groupmappings", UNSET)
        for groupmappings_item_data in _groupmappings or []:
            groupmappings_item = auth_module_group_mapping_m.AuthModuleGroupMapping.from_dict(groupmappings_item_data)

            groupmappings.append(groupmappings_item)

        groupmappings_page = cls(
            groupmappings=groupmappings,
        )

        return groupmappings_page
