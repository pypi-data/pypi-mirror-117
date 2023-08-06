from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_group import UserGroup
else:
    UserGroup = "UserGroup"

from ..models.base_page import BasePage

T = TypeVar("T", bound="SubgroupsPage")


@attr.s(auto_attribs=True)
class SubgroupsPage(BasePage):
    """ """

    subgroups: Union[Unset, List[UserGroup]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subgroups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subgroups, Unset):
            subgroups = []
            for subgroups_item_data in self.subgroups:
                subgroups_item = subgroups_item_data.to_dict()

                subgroups.append(subgroups_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subgroups is not UNSET:
            field_dict["subgroups"] = subgroups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        subgroups = []
        _subgroups = d.pop("subgroups", UNSET)
        for subgroups_item_data in _subgroups or []:
            subgroups_item = UserGroup.from_dict(subgroups_item_data)

            subgroups.append(subgroups_item)

        subgroups_page = cls(
            subgroups=subgroups,
            **_BasePage_kwargs,
        )

        subgroups_page.additional_properties = d
        return subgroups_page

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
