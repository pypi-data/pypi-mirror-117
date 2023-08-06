from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User
else:
    User = "User"

from ..models.base_page import BasePage

T = TypeVar("T", bound="OwnUsersPage")


@attr.s(auto_attribs=True)
class OwnUsersPage(BasePage):
    """ """

    own_users: Union[Unset, List[User]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        own_users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.own_users, Unset):
            own_users = []
            for own_users_item_data in self.own_users:
                own_users_item = own_users_item_data.to_dict()

                own_users.append(own_users_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if own_users is not UNSET:
            field_dict["ownUsers"] = own_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        own_users = []
        _own_users = d.pop("ownUsers", UNSET)
        for own_users_item_data in _own_users or []:
            own_users_item = User.from_dict(own_users_item_data)

            own_users.append(own_users_item)

        own_users_page = cls(
            own_users=own_users,
            **_BasePage_kwargs,
        )

        own_users_page.additional_properties = d
        return own_users_page

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
