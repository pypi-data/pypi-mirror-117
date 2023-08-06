from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authmodule import Authmodule
else:
    Authmodule = "Authmodule"

from ..models.base_page import BasePage

T = TypeVar("T", bound="AuthmodulesPage")


@attr.s(auto_attribs=True)
class AuthmodulesPage(BasePage):
    """ """

    authmodules: Union[Unset, List[Authmodule]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authmodules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.authmodules, Unset):
            authmodules = []
            for authmodules_item_data in self.authmodules:
                authmodules_item = authmodules_item_data.to_dict()

                authmodules.append(authmodules_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authmodules is not UNSET:
            field_dict["authmodules"] = authmodules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        authmodules = []
        _authmodules = d.pop("authmodules", UNSET)
        for authmodules_item_data in _authmodules or []:
            authmodules_item = Authmodule.from_dict(authmodules_item_data)

            authmodules.append(authmodules_item)

        authmodules_page = cls(
            authmodules=authmodules,
            **_BasePage_kwargs,
        )

        authmodules_page.additional_properties = d
        return authmodules_page

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
