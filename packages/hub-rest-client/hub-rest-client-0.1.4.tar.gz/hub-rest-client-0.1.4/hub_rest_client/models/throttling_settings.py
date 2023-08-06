from typing import Any, Dict, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThrottlingSettings")


try:
    from ..models import settings
except ImportError:
    import sys

    settings = sys.modules[__package__ + "settings"]


@attr.s(auto_attribs=True)
class ThrottlingSettings(settings.Settings):
    """ """

    enabled: "Union[Unset, bool]" = UNSET
    white_list: "Union[Unset, List[str]]" = UNSET
    max_tracking_keys: "Union[Unset, int]" = UNSET
    max_failures_per_key: "Union[Unset, int]" = UNSET
    cooldown_value: "Union[Unset, int]" = UNSET
    cooldown_period_sec: "Union[Unset, int]" = UNSET
    blocked_keys: "Union[Unset, blocked_keys_m.BlockedKeys]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        white_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.white_list, Unset):
            white_list = self.white_list

        max_tracking_keys = self.max_tracking_keys
        max_failures_per_key = self.max_failures_per_key
        cooldown_value = self.cooldown_value
        cooldown_period_sec = self.cooldown_period_sec
        blocked_keys: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.blocked_keys, Unset):
            blocked_keys = self.blocked_keys.to_dict()

        field_dict: Dict[str, Any] = {}
        _Settings_dict = super().to_dict()
        field_dict.update(_Settings_dict)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if white_list is not UNSET:
            field_dict["whiteList"] = white_list
        if max_tracking_keys is not UNSET:
            field_dict["maxTrackingKeys"] = max_tracking_keys
        if max_failures_per_key is not UNSET:
            field_dict["maxFailuresPerKey"] = max_failures_per_key
        if cooldown_value is not UNSET:
            field_dict["cooldownValue"] = cooldown_value
        if cooldown_period_sec is not UNSET:
            field_dict["cooldownPeriodSec"] = cooldown_period_sec
        if blocked_keys is not UNSET:
            field_dict["blockedKeys"] = blocked_keys

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import blocked_keys as blocked_keys_m
        except ImportError:
            import sys

            blocked_keys_m = sys.modules[__package__ + "blocked_keys"]

        d = src_dict.copy()

        enabled = d.pop("enabled", UNSET)

        white_list = cast(List[str], d.pop("whiteList", UNSET))

        max_tracking_keys = d.pop("maxTrackingKeys", UNSET)

        max_failures_per_key = d.pop("maxFailuresPerKey", UNSET)

        cooldown_value = d.pop("cooldownValue", UNSET)

        cooldown_period_sec = d.pop("cooldownPeriodSec", UNSET)

        _blocked_keys = d.pop("blockedKeys", UNSET)
        blocked_keys: Union[Unset, blocked_keys_m.BlockedKeys]
        if isinstance(_blocked_keys, Unset):
            blocked_keys = UNSET
        else:
            blocked_keys = blocked_keys_m.BlockedKeys.from_dict(_blocked_keys)

        throttling_settings = cls(
            enabled=enabled,
            white_list=white_list,
            max_tracking_keys=max_tracking_keys,
            max_failures_per_key=max_failures_per_key,
            cooldown_value=cooldown_value,
            cooldown_period_sec=cooldown_period_sec,
            blocked_keys=blocked_keys,
        )

        return throttling_settings
