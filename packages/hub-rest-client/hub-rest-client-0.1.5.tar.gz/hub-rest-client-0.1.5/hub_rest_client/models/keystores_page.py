from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeystoresPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class KeystoresPage(base_page.BasePage):
    """ """

    keystores: "Union[Unset, List[key_store_m.KeyStore]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        keystores: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.keystores, Unset):
            keystores = []
            for keystores_item_data in self.keystores:
                keystores_item = keystores_item_data.to_dict()

                keystores.append(keystores_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if keystores is not UNSET:
            field_dict["keystores"] = keystores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import key_store as key_store_m
        except ImportError:
            import sys

            key_store_m = sys.modules[__package__ + "key_store"]

        d = src_dict.copy()

        _BasePage_kwargs = super().from_dict(src_dict=d).to_dict()
        _BasePage_kwargs.pop("$type")

        keystores = []
        _keystores = d.pop("keystores", UNSET)
        for keystores_item_data in _keystores or []:
            keystores_item = key_store_m.KeyStore.from_dict(keystores_item_data)

            keystores.append(keystores_item)

        keystores_page = cls(
            keystores=keystores,
            **_BasePage_kwargs,
        )

        return keystores_page
