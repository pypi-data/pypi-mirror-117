from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UntrustedredirecturisPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class UntrustedredirecturisPage(base_page.BasePage):
    """ """

    untrustedredirecturis: "Union[Unset, List[untrusted_redirect_uri_m.UntrustedRedirectURI]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        untrustedredirecturis: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.untrustedredirecturis, Unset):
            untrustedredirecturis = []
            for untrustedredirecturis_item_data in self.untrustedredirecturis:
                untrustedredirecturis_item = untrustedredirecturis_item_data.to_dict()

                untrustedredirecturis.append(untrustedredirecturis_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if untrustedredirecturis is not UNSET:
            field_dict["untrustedredirecturis"] = untrustedredirecturis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import untrusted_redirect_uri as untrusted_redirect_uri_m
        except ImportError:
            import sys

            untrusted_redirect_uri_m = sys.modules[__package__ + "untrusted_redirect_uri"]

        d = src_dict.copy()

        _BasePage_kwargs = super().from_dict(src_dict=d).to_dict()

        untrustedredirecturis = []
        _untrustedredirecturis = d.pop("untrustedredirecturis", UNSET)
        for untrustedredirecturis_item_data in _untrustedredirecturis or []:
            untrustedredirecturis_item = untrusted_redirect_uri_m.UntrustedRedirectURI.from_dict(
                untrustedredirecturis_item_data
            )

            untrustedredirecturis.append(untrustedredirecturis_item)

        untrustedredirecturis_page = cls(
            untrustedredirecturis=untrustedredirecturis,
            **_BasePage_kwargs,
        )

        untrustedredirecturis_page.additional_properties = d
        return untrustedredirecturis_page

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
