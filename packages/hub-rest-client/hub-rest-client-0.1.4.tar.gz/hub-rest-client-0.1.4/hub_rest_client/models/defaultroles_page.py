from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DefaultrolesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class DefaultrolesPage(base_page.BasePage):
    """ """

    defaultroles: "Union[Unset, List[role_m.Role]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        defaultroles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.defaultroles, Unset):
            defaultroles = []
            for defaultroles_item_data in self.defaultroles:
                defaultroles_item = defaultroles_item_data.to_dict()

                defaultroles.append(defaultroles_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if defaultroles is not UNSET:
            field_dict["defaultroles"] = defaultroles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import role as role_m
        except ImportError:
            import sys

            role_m = sys.modules[__package__ + "role"]

        d = src_dict.copy()

        defaultroles = []
        _defaultroles = d.pop("defaultroles", UNSET)
        for defaultroles_item_data in _defaultroles or []:
            defaultroles_item = role_m.Role.from_dict(defaultroles_item_data)

            defaultroles.append(defaultroles_item)

        defaultroles_page = cls(
            defaultroles=defaultroles,
        )

        return defaultroles_page
