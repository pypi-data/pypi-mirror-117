from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PermanenttokensPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class PermanenttokensPage(base_page.BasePage):
    """ """

    permanenttokens: "Union[Unset, List[permanent_token_m.PermanentToken]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permanenttokens: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.permanenttokens, Unset):
            permanenttokens = []
            for permanenttokens_item_data in self.permanenttokens:
                permanenttokens_item = permanenttokens_item_data.to_dict()

                permanenttokens.append(permanenttokens_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permanenttokens is not UNSET:
            field_dict["permanenttokens"] = permanenttokens

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import permanent_token as permanent_token_m
        except ImportError:
            import sys

            permanent_token_m = sys.modules[__package__ + "permanent_token"]

        d = src_dict.copy()

        permanenttokens = []
        _permanenttokens = d.pop("permanenttokens", UNSET)
        for permanenttokens_item_data in _permanenttokens or []:
            permanenttokens_item = permanent_token_m.PermanentToken.from_dict(permanenttokens_item_data)

            permanenttokens.append(permanenttokens_item)

        permanenttokens_page = cls(
            permanenttokens=permanenttokens,
        )

        permanenttokens_page.additional_properties = d
        return permanenttokens_page

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
