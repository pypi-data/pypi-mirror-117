from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Avatar")


@attr.s(auto_attribs=True)
class Avatar:
    """ """

    type: str
    url: Union[Unset, str] = UNSET
    picture_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        url = self.url
        picture_url = self.picture_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        avatar.additional_properties = d
        return avatar

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
