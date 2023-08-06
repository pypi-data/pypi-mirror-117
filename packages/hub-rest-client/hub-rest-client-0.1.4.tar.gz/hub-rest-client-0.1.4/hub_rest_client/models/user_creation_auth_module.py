from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserCreationAuthModule")


try:
    from ..models import authmodule
except ImportError:
    import sys

    authmodule = sys.modules[__package__ + "authmodule"]


@attr.s(auto_attribs=True)
class UserCreationAuthModule(authmodule.Authmodule):
    """ """

    allowed_create_new_users: "Union[Unset, bool]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        allowed_create_new_users = self.allowed_create_new_users

        field_dict: Dict[str, Any] = {}
        _Authmodule_dict = super().to_dict()
        field_dict.update(_Authmodule_dict)
        field_dict.update({})
        if allowed_create_new_users is not UNSET:
            field_dict["allowedCreateNewUsers"] = allowed_create_new_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        allowed_create_new_users = d.pop("allowedCreateNewUsers", UNSET)

        user_creation_auth_module = cls(
            allowed_create_new_users=allowed_create_new_users,
        )

        return user_creation_auth_module
