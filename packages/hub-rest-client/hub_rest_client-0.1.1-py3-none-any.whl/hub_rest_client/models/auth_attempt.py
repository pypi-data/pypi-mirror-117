from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authmodule import Authmodule
    from ..models.details import Details
    from ..models.user import User
else:
    Details = "Details"
    Authmodule = "Authmodule"
    User = "User"

from ..models.uuid import Uuid

T = TypeVar("T", bound="AuthAttempt")


@attr.s(auto_attribs=True)
class AuthAttempt(Uuid):
    """ """

    external_user_details: Union[Unset, Details] = UNSET
    persisted_user_details: Union[Unset, Details] = UNSET
    similar_user: Union[Unset, User] = UNSET
    auth_module: Union[Unset, Authmodule] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_user_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_user_details, Unset):
            external_user_details = self.external_user_details.to_dict()

        persisted_user_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.persisted_user_details, Unset):
            persisted_user_details = self.persisted_user_details.to_dict()

        similar_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.similar_user, Unset):
            similar_user = self.similar_user.to_dict()

        auth_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auth_module, Unset):
            auth_module = self.auth_module.to_dict()

        field_dict: Dict[str, Any] = {}
        _Uuid_dict = super(Uuid).to_dict()
        field_dict.update(_Uuid_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_user_details is not UNSET:
            field_dict["externalUserDetails"] = external_user_details
        if persisted_user_details is not UNSET:
            field_dict["persistedUserDetails"] = persisted_user_details
        if similar_user is not UNSET:
            field_dict["similarUser"] = similar_user
        if auth_module is not UNSET:
            field_dict["authModule"] = auth_module

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Uuid_kwargs = super(Uuid).from_dict(src_dict=d).to_dict()

        _external_user_details = d.pop("externalUserDetails", UNSET)
        external_user_details: Union[Unset, Details]
        if isinstance(_external_user_details, Unset):
            external_user_details = UNSET
        else:
            external_user_details = Details.from_dict(_external_user_details)

        _persisted_user_details = d.pop("persistedUserDetails", UNSET)
        persisted_user_details: Union[Unset, Details]
        if isinstance(_persisted_user_details, Unset):
            persisted_user_details = UNSET
        else:
            persisted_user_details = Details.from_dict(_persisted_user_details)

        _similar_user = d.pop("similarUser", UNSET)
        similar_user: Union[Unset, User]
        if isinstance(_similar_user, Unset):
            similar_user = UNSET
        else:
            similar_user = User.from_dict(_similar_user)

        _auth_module = d.pop("authModule", UNSET)
        auth_module: Union[Unset, Authmodule]
        if isinstance(_auth_module, Unset):
            auth_module = UNSET
        else:
            auth_module = Authmodule.from_dict(_auth_module)

        auth_attempt = cls(
            external_user_details=external_user_details,
            persisted_user_details=persisted_user_details,
            similar_user=similar_user,
            auth_module=auth_module,
            **_Uuid_kwargs,
        )

        auth_attempt.additional_properties = d
        return auth_attempt

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
