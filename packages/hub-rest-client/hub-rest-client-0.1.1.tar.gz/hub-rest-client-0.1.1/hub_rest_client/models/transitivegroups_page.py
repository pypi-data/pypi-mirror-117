from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_group import UserGroup
else:
    UserGroup = "UserGroup"

from ..models.base_page import BasePage

T = TypeVar("T", bound="TransitivegroupsPage")


@attr.s(auto_attribs=True)
class TransitivegroupsPage(BasePage):
    """ """

    transitivegroups: Union[Unset, List[UserGroup]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transitivegroups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transitivegroups, Unset):
            transitivegroups = []
            for transitivegroups_item_data in self.transitivegroups:
                transitivegroups_item = transitivegroups_item_data.to_dict()

                transitivegroups.append(transitivegroups_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transitivegroups is not UNSET:
            field_dict["transitivegroups"] = transitivegroups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        transitivegroups = []
        _transitivegroups = d.pop("transitivegroups", UNSET)
        for transitivegroups_item_data in _transitivegroups or []:
            transitivegroups_item = UserGroup.from_dict(transitivegroups_item_data)

            transitivegroups.append(transitivegroups_item)

        transitivegroups_page = cls(
            transitivegroups=transitivegroups,
            **_BasePage_kwargs,
        )

        transitivegroups_page.additional_properties = d
        return transitivegroups_page

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
