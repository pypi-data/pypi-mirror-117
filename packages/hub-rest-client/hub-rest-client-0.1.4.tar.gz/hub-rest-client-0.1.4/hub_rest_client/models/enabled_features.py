from typing import Any, Dict, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnabledFeatures")


@attr.s(auto_attribs=True)
class EnabledFeatures:
    """ """

    enabled: "Union[Unset, List[str]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        enabled: Union[Unset, List[str]] = UNSET
        if not isinstance(self.enabled, Unset):
            enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        enabled = cast(List[str], d.pop("enabled", UNSET))

        enabled_features = cls(
            enabled=enabled,
        )

        return enabled_features
