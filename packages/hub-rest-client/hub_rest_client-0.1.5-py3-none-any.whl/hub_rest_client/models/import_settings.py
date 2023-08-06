from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportSettings")


try:
    from ..models import settings
except ImportError:
    import sys

    settings = sys.modules[__package__ + "settings"]


@attr.s(auto_attribs=True)
class ImportSettings(settings.Settings):
    """ """

    import_folder: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        import_folder = self.import_folder

        field_dict: Dict[str, Any] = {}
        _Settings_dict = super().to_dict()
        field_dict.update(_Settings_dict)
        field_dict.update({})
        if import_folder is not UNSET:
            field_dict["importFolder"] = import_folder

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _Settings_kwargs = super().from_dict(src_dict=d).to_dict()
        _Settings_kwargs.pop("$type")

        import_folder = d.pop("importFolder", UNSET)

        import_settings = cls(
            import_folder=import_folder,
            **_Settings_kwargs,
        )

        return import_settings
