from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="RoleSource")


@attr.s(auto_attribs=True)
class RoleSource:
    """ """

    type: "str"

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        type = d.pop("type")

        role_source = cls(
            type=type,
        )

        return role_source
