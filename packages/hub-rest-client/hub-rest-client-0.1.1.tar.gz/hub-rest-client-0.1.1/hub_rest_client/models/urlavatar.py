from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.avatar import Avatar
from ..types import UNSET, Unset

T = TypeVar("T", bound="Urlavatar")


@attr.s(auto_attribs=True)
class Urlavatar(Avatar):
    """ """

    avatar_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        avatar_url = self.avatar_url

        field_dict: Dict[str, Any] = {}
        _Avatar_dict = super(Avatar).to_dict()
        field_dict.update(_Avatar_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Avatar_kwargs = super(Avatar).from_dict(src_dict=d).to_dict()

        avatar_url = d.pop("avatarUrl", UNSET)

        urlavatar = cls(
            avatar_url=avatar_url,
            **_Avatar_kwargs,
        )

        urlavatar.additional_properties = d
        return urlavatar

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
