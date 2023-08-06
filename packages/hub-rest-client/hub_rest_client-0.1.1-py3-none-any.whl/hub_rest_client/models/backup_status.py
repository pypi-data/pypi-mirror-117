from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_data import BackupData
else:
    BackupData = "BackupData"


T = TypeVar("T", bound="BackupStatus")


@attr.s(auto_attribs=True)
class BackupStatus:
    """ """

    in_progress: Union[Unset, bool] = UNSET
    saved_data: Union[Unset, List[BackupData]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        in_progress = self.in_progress
        saved_data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.saved_data, Unset):
            saved_data = []
            for saved_data_item_data in self.saved_data:
                saved_data_item = saved_data_item_data.to_dict()

                saved_data.append(saved_data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if in_progress is not UNSET:
            field_dict["inProgress"] = in_progress
        if saved_data is not UNSET:
            field_dict["savedData"] = saved_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        in_progress = d.pop("inProgress", UNSET)

        saved_data = []
        _saved_data = d.pop("savedData", UNSET)
        for saved_data_item_data in _saved_data or []:
            saved_data_item = BackupData.from_dict(saved_data_item_data)

            saved_data.append(saved_data_item)

        backup_status = cls(
            in_progress=in_progress,
            saved_data=saved_data,
        )

        backup_status.additional_properties = d
        return backup_status

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
