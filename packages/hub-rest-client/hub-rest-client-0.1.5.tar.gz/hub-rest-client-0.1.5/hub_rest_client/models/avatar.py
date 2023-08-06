from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Avatar")


@attr.s(auto_attribs=True)
class Avatar:
    """ """

    type: "str"
    url: "Union[Unset, str]" = UNSET
    picture_url: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        url = self.url
        picture_url = self.picture_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if picture_url is not UNSET:
            field_dict["pictureUrl"] = picture_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        type = d.pop("type")

        url = d.pop("url", UNSET)

        picture_url = d.pop("pictureUrl", UNSET)

        avatar = cls(
            type=type,
            url=url,
            picture_url=picture_url,
        )

        return avatar
