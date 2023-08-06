from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthRequest")


@attr.s(auto_attribs=True)
class AuthRequest:
    """ """

    user_id: "Union[Unset, str]" = UNSET
    credentials: "Union[Unset, credentials_m.Credentials]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        credentials: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import credentials as credentials_m
        except ImportError:
            import sys

            credentials_m = sys.modules[__package__ + "credentials"]

        d = src_dict.copy()

        user_id = d.pop("userId", UNSET)

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, credentials_m.Credentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = credentials_m.Credentials.from_dict(_credentials)

        auth_request = cls(
            user_id=user_id,
            credentials=credentials,
        )

        return auth_request
