from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_group import UserGroup
else:
    UserGroup = "UserGroup"

from ..models.base_page import BasePage

T = TypeVar("T", bound="UsergroupsPage")


@attr.s(auto_attribs=True)
class UsergroupsPage(BasePage):
    """ """

    usergroups: Union[Unset, List[UserGroup]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        usergroups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.usergroups, Unset):
            usergroups = []
            for usergroups_item_data in self.usergroups:
                usergroups_item = usergroups_item_data.to_dict()

                usergroups.append(usergroups_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if usergroups is not UNSET:
            field_dict["usergroups"] = usergroups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        usergroups = []
        _usergroups = d.pop("usergroups", UNSET)
        for usergroups_item_data in _usergroups or []:
            usergroups_item = UserGroup.from_dict(usergroups_item_data)

            usergroups.append(usergroups_item)

        usergroups_page = cls(
            usergroups=usergroups,
            **_BasePage_kwargs,
        )

        usergroups_page.additional_properties = d
        return usergroups_page

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
