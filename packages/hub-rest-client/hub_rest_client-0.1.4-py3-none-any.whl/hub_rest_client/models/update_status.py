from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateStatus")


@attr.s(auto_attribs=True)
class UpdateStatus:
    """ """

    succeed: "Union[Unset, bool]" = UNSET
    update: "Union[Unset, update_status_info_m.UpdateStatusInfo]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        succeed = self.succeed
        update: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if succeed is not UNSET:
            field_dict["succeed"] = succeed
        if update is not UNSET:
            field_dict["update"] = update

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import update_status_info as update_status_info_m
        except ImportError:
            import sys

            update_status_info_m = sys.modules[__package__ + "update_status_info"]

        d = src_dict.copy()

        succeed = d.pop("succeed", UNSET)

        _update = d.pop("update", UNSET)
        update: Union[Unset, update_status_info_m.UpdateStatusInfo]
        if isinstance(_update, Unset):
            update = UNSET
        else:
            update = update_status_info_m.UpdateStatusInfo.from_dict(_update)

        update_status = cls(
            succeed=succeed,
            update=update,
        )

        return update_status
