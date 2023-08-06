from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Alias")


@attr.s(auto_attribs=True)
class Alias:
    """ """

    id: "Union[Unset, str]" = UNSET
    action: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        action = self.action

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        action = d.pop("action", UNSET)

        alias = cls(
            id=id,
            action=action,
        )

        return alias
