from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.settings import Settings
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportSettings")


@attr.s(auto_attribs=True)
class ImportSettings(Settings):
    """ """

    import_folder: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        import_folder = self.import_folder

        field_dict: Dict[str, Any] = {}
        _Settings_dict = super(Settings).to_dict()
        field_dict.update(_Settings_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if import_folder is not UNSET:
            field_dict["importFolder"] = import_folder

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Settings_kwargs = super(Settings).from_dict(src_dict=d).to_dict()

        import_folder = d.pop("importFolder", UNSET)

        import_settings = cls(
            import_folder=import_folder,
            **_Settings_kwargs,
        )

        import_settings.additional_properties = d
        return import_settings

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
