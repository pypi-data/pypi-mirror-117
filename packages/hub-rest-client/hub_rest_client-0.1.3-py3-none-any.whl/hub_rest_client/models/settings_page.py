from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SettingsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class SettingsPage(base_page.BasePage):
    """ """

    settings: "Union[Unset, List[settings_m.Settings]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        settings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = []
            for settings_item_data in self.settings:
                settings_item = settings_item_data.to_dict()

                settings.append(settings_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import settings as settings_m
        except ImportError:
            import sys

            settings_m = sys.modules[__package__ + "settings"]

        d = src_dict.copy()

        settings = []
        _settings = d.pop("settings", UNSET)
        for settings_item_data in _settings or []:
            settings_item = settings_m.Settings.from_dict(settings_item_data)

            settings.append(settings_item)

        settings_page = cls(
            settings=settings,
        )

        settings_page.additional_properties = d
        return settings_page

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
