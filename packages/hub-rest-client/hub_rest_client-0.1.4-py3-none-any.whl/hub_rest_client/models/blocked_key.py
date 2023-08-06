from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlockedKey")


@attr.s(auto_attribs=True)
class BlockedKey:
    """ """

    key: "Union[Unset, str]" = UNSET
    description: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        key = d.pop("key", UNSET)

        description = d.pop("description", UNSET)

        blocked_key = cls(
            key=key,
            description=description,
        )

        return blocked_key
