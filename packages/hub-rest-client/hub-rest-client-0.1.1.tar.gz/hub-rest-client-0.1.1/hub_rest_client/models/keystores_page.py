from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_store import KeyStore
else:
    KeyStore = "KeyStore"

from ..models.base_page import BasePage

T = TypeVar("T", bound="KeystoresPage")


@attr.s(auto_attribs=True)
class KeystoresPage(BasePage):
    """ """

    keystores: Union[Unset, List[KeyStore]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keystores: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.keystores, Unset):
            keystores = []
            for keystores_item_data in self.keystores:
                keystores_item = keystores_item_data.to_dict()

                keystores.append(keystores_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keystores is not UNSET:
            field_dict["keystores"] = keystores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        keystores = []
        _keystores = d.pop("keystores", UNSET)
        for keystores_item_data in _keystores or []:
            keystores_item = KeyStore.from_dict(keystores_item_data)

            keystores.append(keystores_item)

        keystores_page = cls(
            keystores=keystores,
            **_BasePage_kwargs,
        )

        keystores_page.additional_properties = d
        return keystores_page

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
