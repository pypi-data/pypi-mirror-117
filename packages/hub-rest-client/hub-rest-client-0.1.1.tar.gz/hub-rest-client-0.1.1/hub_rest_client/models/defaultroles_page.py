from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role import Role
else:
    Role = "Role"

from ..models.base_page import BasePage

T = TypeVar("T", bound="DefaultrolesPage")


@attr.s(auto_attribs=True)
class DefaultrolesPage(BasePage):
    """ """

    defaultroles: Union[Unset, List[Role]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        defaultroles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.defaultroles, Unset):
            defaultroles = []
            for defaultroles_item_data in self.defaultroles:
                defaultroles_item = defaultroles_item_data.to_dict()

                defaultroles.append(defaultroles_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defaultroles is not UNSET:
            field_dict["defaultroles"] = defaultroles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        defaultroles = []
        _defaultroles = d.pop("defaultroles", UNSET)
        for defaultroles_item_data in _defaultroles or []:
            defaultroles_item = Role.from_dict(defaultroles_item_data)

            defaultroles.append(defaultroles_item)

        defaultroles_page = cls(
            defaultroles=defaultroles,
            **_BasePage_kwargs,
        )

        defaultroles_page.additional_properties = d
        return defaultroles_page

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
