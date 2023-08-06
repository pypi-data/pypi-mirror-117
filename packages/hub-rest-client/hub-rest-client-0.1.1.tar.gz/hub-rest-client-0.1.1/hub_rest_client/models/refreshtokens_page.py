from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.refresh_token import RefreshToken
else:
    RefreshToken = "RefreshToken"

from ..models.base_page import BasePage

T = TypeVar("T", bound="RefreshtokensPage")


@attr.s(auto_attribs=True)
class RefreshtokensPage(BasePage):
    """ """

    refreshtokens: Union[Unset, List[RefreshToken]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refreshtokens: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.refreshtokens, Unset):
            refreshtokens = []
            for refreshtokens_item_data in self.refreshtokens:
                refreshtokens_item = refreshtokens_item_data.to_dict()

                refreshtokens.append(refreshtokens_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if refreshtokens is not UNSET:
            field_dict["refreshtokens"] = refreshtokens

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        refreshtokens = []
        _refreshtokens = d.pop("refreshtokens", UNSET)
        for refreshtokens_item_data in _refreshtokens or []:
            refreshtokens_item = RefreshToken.from_dict(refreshtokens_item_data)

            refreshtokens.append(refreshtokens_item)

        refreshtokens_page = cls(
            refreshtokens=refreshtokens,
            **_BasePage_kwargs,
        )

        refreshtokens_page.additional_properties = d
        return refreshtokens_page

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
