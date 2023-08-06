from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_status_info import UpdateStatusInfo
else:
    UpdateStatusInfo = "UpdateStatusInfo"


T = TypeVar("T", bound="UpdateStatus")


@attr.s(auto_attribs=True)
class UpdateStatus:
    """ """

    succeed: Union[Unset, bool] = UNSET
    update: Union[Unset, UpdateStatusInfo] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        succeed = self.succeed
        update: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if succeed is not UNSET:
            field_dict["succeed"] = succeed
        if update is not UNSET:
            field_dict["update"] = update

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        succeed = d.pop("succeed", UNSET)

        _update = d.pop("update", UNSET)
        update: Union[Unset, UpdateStatusInfo]
        if isinstance(_update, Unset):
            update = UNSET
        else:
            update = UpdateStatusInfo.from_dict(_update)

        update_status = cls(
            succeed=succeed,
            update=update,
        )

        update_status.additional_properties = d
        return update_status

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
