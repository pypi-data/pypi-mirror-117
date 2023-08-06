from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.authmodule import Authmodule
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserCreationAuthModule")


@attr.s(auto_attribs=True)
class UserCreationAuthModule(Authmodule):
    """ """

    allowed_create_new_users: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allowed_create_new_users = self.allowed_create_new_users

        field_dict: Dict[str, Any] = {}
        _Authmodule_dict = super(Authmodule).to_dict()
        field_dict.update(_Authmodule_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_create_new_users is not UNSET:
            field_dict["allowedCreateNewUsers"] = allowed_create_new_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Authmodule_kwargs = super(Authmodule).from_dict(src_dict=d).to_dict()

        allowed_create_new_users = d.pop("allowedCreateNewUsers", UNSET)

        user_creation_auth_module = cls(
            allowed_create_new_users=allowed_create_new_users,
            **_Authmodule_kwargs,
        )

        user_creation_auth_module.additional_properties = d
        return user_creation_auth_module

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
