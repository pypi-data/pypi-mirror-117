from typing import Any, Dict, Type, TypeVar, Union

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

            auth_attempt_m = sys.modules[__package__ + "auth_attempt"]
            user_m = sys.modules[__package__ + "user"]

        d = src_dict.copy()

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
        )

        return auth_found_user
