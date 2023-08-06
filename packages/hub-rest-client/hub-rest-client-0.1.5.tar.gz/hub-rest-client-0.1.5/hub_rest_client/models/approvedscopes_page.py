from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovedscopesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class ApprovedscopesPage(base_page.BasePage):
    """ """

    approvedscopes: "Union[Unset, List[approved_scope_m.ApprovedScope]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        approvedscopes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.approvedscopes, Unset):
            approvedscopes = []
            for approvedscopes_item_data in self.approvedscopes:
                approvedscopes_item = approvedscopes_item_data.to_dict()

                approvedscopes.append(approvedscopes_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if approvedscopes is not UNSET:
            field_dict["approvedscopes"] = approvedscopes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import approved_scope as approved_scope_m
        except ImportError:
            import sys

            approved_scope_m = sys.modules[__package__ + "approved_scope"]

        d = src_dict.copy()

        _BasePage_kwargs = super().from_dict(src_dict=d).to_dict()
        _BasePage_kwargs.pop("$type")

        approvedscopes = []
        _approvedscopes = d.pop("approvedscopes", UNSET)
        for approvedscopes_item_data in _approvedscopes or []:
            approvedscopes_item = approved_scope_m.ApprovedScope.from_dict(approvedscopes_item_data)

            approvedscopes.append(approvedscopes_item)

        approvedscopes_page = cls(
            approvedscopes=approvedscopes,
            **_BasePage_kwargs,
        )

        return approvedscopes_page
