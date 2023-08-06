from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="SystemFeature")


try:
    from ..models import hub_feature
except ImportError:
    import sys

    hub_feature = sys.modules[__package__ + "hub_feature"]


@attr.s(auto_attribs=True)
class SystemFeature(hub_feature.HubFeature):
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _HubFeature_dict = super().to_dict()
        field_dict.update(_HubFeature_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _HubFeature_kwargs = super().from_dict(src_dict=d).to_dict()
        _HubFeature_kwargs.pop("$type")

        system_feature = cls(
            **_HubFeature_kwargs,
        )

        return system_feature
