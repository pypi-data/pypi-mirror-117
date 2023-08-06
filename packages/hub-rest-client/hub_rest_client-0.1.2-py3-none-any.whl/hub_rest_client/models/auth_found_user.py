from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthFoundUser")


try:
    from ..models import uuid
except ImportError:
    import sys

    uuid = sys.modules[__package__ + "uuid"]


@attr.s(auto_attribs=True)
class AuthFoundUser(uuid.Uuid):
    """ """

    user: "Union[Unset, user_m.User]" = UNSET
    attempts: "Union[Unset, List[auth_attempt_m.AuthAttempt]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        attempts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attempts, Unset):
            attempts = []
            for attempts_item_data in self.attempts:
                attempts_item = attempts_item_data.to_dict()

                attempts.append(attempts_item)

        field_dict: Dict[str, Any] = {}
        _Uuid_dict = super().to_dict()
        field_dict.update(_Uuid_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if attempts is not UNSET:
            field_dict["attempts"] = attempts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import auth_attempt as auth_attempt_m
            from ..models import user as user_m
        except ImportError:
            import sys

            user_m = sys.modules[__package__ + "user"]
            auth_attempt_m = sys.modules[__package__ + "auth_attempt"]

        d = src_dict.copy()

        _Uuid_kwargs = super().from_dict(src_dict=d).to_dict()

        _user = d.pop("user", UNSET)
        user: Union[Unset, user_m.User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = user_m.User.from_dict(_user)

        attempts = []
        _attempts = d.pop("attempts", UNSET)
        for attempts_item_data in _attempts or []:
            attempts_item = auth_attempt_m.AuthAttempt.from_dict(attempts_item_data)

            attempts.append(attempts_item)

        auth_found_user = cls(
            user=user,
            attempts=attempts,
            **_Uuid_kwargs,
        )

        auth_found_user.additional_properties = d
        return auth_found_user

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
