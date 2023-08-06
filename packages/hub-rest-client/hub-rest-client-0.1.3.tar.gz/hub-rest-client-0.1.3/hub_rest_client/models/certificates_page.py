from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificatesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class CertificatesPage(base_page.BasePage):
    """ """

    certificates: "Union[Unset, List[certificate_m.Certificate]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.certificates, Unset):
            certificates = []
            for certificates_item_data in self.certificates:
                certificates_item = certificates_item_data.to_dict()

                certificates.append(certificates_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificates is not UNSET:
            field_dict["certificates"] = certificates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import certificate as certificate_m
        except ImportError:
            import sys

            certificate_m = sys.modules[__package__ + "certificate"]

        d = src_dict.copy()

        certificates = []
        _certificates = d.pop("certificates", UNSET)
        for certificates_item_data in _certificates or []:
            certificates_item = certificate_m.Certificate.from_dict(certificates_item_data)

            certificates.append(certificates_item)

        certificates_page = cls(
            certificates=certificates,
        )

        certificates_page.additional_properties = d
        return certificates_page

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
