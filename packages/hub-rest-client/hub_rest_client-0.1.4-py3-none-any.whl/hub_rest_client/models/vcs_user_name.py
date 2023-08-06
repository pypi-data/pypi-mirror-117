from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VcsUserName")


@attr.s(auto_attribs=True)
class VcsUserName:
    """ """

    name: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        name = d.pop("name", UNSET)

        vcs_user_name = cls(
            name=name,
        )

        return vcs_user_name
