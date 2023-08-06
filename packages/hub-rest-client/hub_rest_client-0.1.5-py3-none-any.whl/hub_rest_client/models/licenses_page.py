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

        _BasePage_kwargs = super().from_dict(src_dict=d).to_dict()
        _BasePage_kwargs.pop("$type")

        licenses = []
        _licenses = d.pop("licenses", UNSET)
        for licenses_item_data in _licenses or []:
            licenses_item = license__m.License.from_dict(licenses_item_data)

            licenses.append(licenses_item)

        licenses_page = cls(
            licenses=licenses,
            **_BasePage_kwargs,
        )

        return licenses_page
