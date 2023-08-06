from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateUserReliablity")


@attr.s(auto_attribs=True)
class DuplicateUserReliablity:
    """ """

    id: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        duplicate_user_reliablity = cls(
            id=id,
        )

        return duplicate_user_reliablity
