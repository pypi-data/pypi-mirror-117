from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authority_holder import AuthorityHolder
else:
    AuthorityHolder = "AuthorityHolder"

from ..models.base_page import BasePage

T = TypeVar("T", bound="ViewersPage")


@attr.s(auto_attribs=True)
class ViewersPage(BasePage):
    """ """

    viewers: Union[Unset, List[AuthorityHolder]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        viewers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.viewers, Unset):
            viewers = []
            for viewers_item_data in self.viewers:
                viewers_item = viewers_item_data.to_dict()

                viewers.append(viewers_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if viewers is not UNSET:
            field_dict["viewers"] = viewers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        viewers = []
        _viewers = d.pop("viewers", UNSET)
        for viewers_item_data in _viewers or []:
            viewers_item = AuthorityHolder.from_dict(viewers_item_data)

            viewers.append(viewers_item)

        viewers_page = cls(
            viewers=viewers,
            **_BasePage_kwargs,
        )

        viewers_page.additional_properties = d
        return viewers_page

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
