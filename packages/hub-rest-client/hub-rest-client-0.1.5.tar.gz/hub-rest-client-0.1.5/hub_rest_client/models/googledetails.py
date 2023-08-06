from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Googledetails")


try:
    from ..models import details
except ImportError:
    import sys

    details = sys.modules[__package__ + "details"]


@attr.s(auto_attribs=True)
class Googledetails(details.Details):
    """ """

    identifier: "Union[Unset, str]" = UNSET
    full_name: "Union[Unset, str]" = UNSET
    avatar: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier
        full_name = self.full_name
        avatar = self.avatar

        field_dict: Dict[str, Any] = {}
        _Details_dict = super().to_dict()
        field_dict.update(_Details_dict)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _Details_kwargs = super().from_dict(src_dict=d).to_dict()
        _Details_kwargs.pop("$type")

        identifier = d.pop("identifier", UNSET)

        full_name = d.pop("fullName", UNSET)

        avatar = d.pop("avatar", UNSET)

        googledetails = cls(
            identifier=identifier,
            full_name=full_name,
            avatar=avatar,
            **_Details_kwargs,
        )

        return googledetails
