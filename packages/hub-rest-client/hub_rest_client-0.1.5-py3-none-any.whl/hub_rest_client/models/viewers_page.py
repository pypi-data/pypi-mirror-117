from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewersPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class ViewersPage(base_page.BasePage):
    """ """

    viewers: "Union[Unset, List[authority_holder_m.AuthorityHolder]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        viewers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.viewers, Unset):
            viewers = []
            for viewers_item_data in self.viewers:
                viewers_item = viewers_item_data.to_dict()

                viewers.append(viewers_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if viewers is not UNSET:
            field_dict["viewers"] = viewers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import authority_holder as authority_holder_m
        except ImportError:
            import sys

            authority_holder_m = sys.modules[__package__ + "authority_holder"]

        d = src_dict.copy()

        _BasePage_kwargs = super().from_dict(src_dict=d).to_dict()
        _BasePage_kwargs.pop("$type")

        viewers = []
        _viewers = d.pop("viewers", UNSET)
        for viewers_item_data in _viewers or []:
            viewers_item = authority_holder_m.AuthorityHolder.from_dict(viewers_item_data)

            viewers.append(viewers_item)

        viewers_page = cls(
            viewers=viewers,
            **_BasePage_kwargs,
        )

        return viewers_page
