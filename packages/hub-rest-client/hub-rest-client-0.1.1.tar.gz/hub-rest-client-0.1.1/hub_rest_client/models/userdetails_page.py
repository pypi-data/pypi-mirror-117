from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.details import Details
else:
    Details = "Details"

from ..models.base_page import BasePage

T = TypeVar("T", bound="UserdetailsPage")


@attr.s(auto_attribs=True)
class UserdetailsPage(BasePage):
    """ """

    userdetails: Union[Unset, List[Details]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        userdetails: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.userdetails, Unset):
            userdetails = []
            for userdetails_item_data in self.userdetails:
                userdetails_item = userdetails_item_data.to_dict()

                userdetails.append(userdetails_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if userdetails is not UNSET:
            field_dict["userdetails"] = userdetails

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        userdetails = []
        _userdetails = d.pop("userdetails", UNSET)
        for userdetails_item_data in _userdetails or []:
            userdetails_item = Details.from_dict(userdetails_item_data)

            userdetails.append(userdetails_item)

        userdetails_page = cls(
            userdetails=userdetails,
            **_BasePage_kwargs,
        )

        userdetails_page.additional_properties = d
        return userdetails_page

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
