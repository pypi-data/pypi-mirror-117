from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserdetailsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class UserdetailsPage(base_page.BasePage):
    """ """

    userdetails: "Union[Unset, List[details_m.Details]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        userdetails: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.userdetails, Unset):
            userdetails = []
            for userdetails_item_data in self.userdetails:
                userdetails_item = userdetails_item_data.to_dict()

                userdetails.append(userdetails_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if userdetails is not UNSET:
            field_dict["userdetails"] = userdetails

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import details as details_m
        except ImportError:
            import sys

            details_m = sys.modules[__package__ + "details"]

        d = src_dict.copy()

        userdetails = []
        _userdetails = d.pop("userdetails", UNSET)
        for userdetails_item_data in _userdetails or []:
            userdetails_item = details_m.Details.from_dict(userdetails_item_data)

            userdetails.append(userdetails_item)

        userdetails_page = cls(
            userdetails=userdetails,
        )

        return userdetails_page
