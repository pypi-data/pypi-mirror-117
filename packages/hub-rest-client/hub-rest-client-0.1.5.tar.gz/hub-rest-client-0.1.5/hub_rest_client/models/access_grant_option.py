from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="AccessGrantOption")


@attr.s(auto_attribs=True)
class AccessGrantOption:
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        access_grant_option = cls()

        return access_grant_option
