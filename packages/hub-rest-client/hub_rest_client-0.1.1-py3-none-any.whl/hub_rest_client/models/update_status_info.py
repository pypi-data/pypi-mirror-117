from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateStatusInfo")


@attr.s(auto_attribs=True)
class UpdateStatusInfo:
    """ """

    message: Union[Unset, str] = UNSET
    download_url: Union[Unset, str] = UNSET
    date: Union[Unset, int] = UNSET
    free: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        download_url = self.download_url
        date = self.date
        free = self.free

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url
        if date is not UNSET:
            field_dict["date"] = date
        if free is not UNSET:
            field_dict["free"] = free

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        message = d.pop("message", UNSET)

        download_url = d.pop("downloadUrl", UNSET)

        date = d.pop("date", UNSET)

        free = d.pop("free", UNSET)

        update_status_info = cls(
            message=message,
            download_url=download_url,
            date=date,
            free=free,
        )

        update_status_info.additional_properties = d
        return update_status_info

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
