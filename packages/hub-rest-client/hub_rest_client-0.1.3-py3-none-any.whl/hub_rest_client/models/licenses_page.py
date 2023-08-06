from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicensesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class LicensesPage(base_page.BasePage):
    """ """

    licenses: "Union[Unset, List[license__m.License]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        licenses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.licenses, Unset):
            licenses = []
            for licenses_item_data in self.licenses:
                licenses_item = licenses_item_data.to_dict()

                licenses.append(licenses_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if licenses is not UNSET:
            field_dict["licenses"] = licenses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import license_ as license__m
        except ImportError:
            import sys

            license__m = sys.modules[__package__ + "license_"]

        d = src_dict.copy()

        licenses = []
        _licenses = d.pop("licenses", UNSET)
        for licenses_item_data in _licenses or []:
            licenses_item = license__m.License.from_dict(licenses_item_data)

            licenses.append(licenses_item)

        licenses_page = cls(
            licenses=licenses,
        )

        licenses_page.additional_properties = d
        return licenses_page

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
