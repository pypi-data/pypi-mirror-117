from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateHubDetails")


@attr.s(auto_attribs=True)
class CreateHubDetails:
    """ """

    is_allowed: "Union[Unset, bool]" = UNSET
    error_id: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_allowed = self.is_allowed
        error_id = self.error_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_allowed is not UNSET:
            field_dict["isAllowed"] = is_allowed
        if error_id is not UNSET:
            field_dict["errorId"] = error_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        is_allowed = d.pop("isAllowed", UNSET)

        error_id = d.pop("errorId", UNSET)

        create_hub_details = cls(
            is_allowed=is_allowed,
            error_id=error_id,
        )

        return create_hub_details
