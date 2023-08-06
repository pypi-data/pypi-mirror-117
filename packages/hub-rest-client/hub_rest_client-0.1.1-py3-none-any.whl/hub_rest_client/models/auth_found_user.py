from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_attempt import AuthAttempt
    from ..models.user import User
else:
    AuthAttempt = "AuthAttempt"
    User = "User"

from ..models.uuid import Uuid

T = TypeVar("T", bound="AuthFoundUser")


@attr.s(auto_attribs=True)
class AuthFoundUser(Uuid):
    """ """

    user: Union[Unset, User] = UNSET
    attempts: Union[Unset, List[AuthAttempt]] = UNSET
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
        _Uuid_dict = super(Uuid).to_dict()
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
        d = src_dict.copy()

        _Uuid_kwargs = super(Uuid).from_dict(src_dict=d).to_dict()

        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        attempts = []
        _attempts = d.pop("attempts", UNSET)
        for attempts_item_data in _attempts or []:
            attempts_item = AuthAttempt.from_dict(attempts_item_data)

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
