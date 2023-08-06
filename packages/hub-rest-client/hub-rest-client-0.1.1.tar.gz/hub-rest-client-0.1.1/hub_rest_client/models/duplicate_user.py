from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User
else:
    User = "User"


T = TypeVar("T", bound="DuplicateUser")


@attr.s(auto_attribs=True)
class DuplicateUser:
    """ """

    user: Union[Unset, User] = UNSET
    reason_fields: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        reason_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.reason_fields, Unset):
            reason_fields = self.reason_fields

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if reason_fields is not UNSET:
            field_dict["reasonFields"] = reason_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        reason_fields = cast(List[str], d.pop("reasonFields", UNSET))

        duplicate_user = cls(
            user=user,
            reason_fields=reason_fields,
        )

        duplicate_user.additional_properties = d
        return duplicate_user

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
