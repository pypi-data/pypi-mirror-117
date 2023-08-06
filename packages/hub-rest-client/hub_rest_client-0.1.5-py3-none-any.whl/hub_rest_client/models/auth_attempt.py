from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthAttempt")


try:
    from ..models import uuid
except ImportError:
    import sys

    uuid = sys.modules[__package__ + "uuid"]


@attr.s(auto_attribs=True)
class AuthAttempt(uuid.Uuid):
    """ """

    external_user_details: "Union[Unset, details_m.Details]" = UNSET
    persisted_user_details: "Union[Unset, details_m.Details]" = UNSET
    similar_user: "Union[Unset, user_m.User]" = UNSET
    auth_module: "Union[Unset, authmodule_m.Authmodule]" = UNSET

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
        _Uuid_dict = super().to_dict()
        field_dict.update(_Uuid_dict)
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

        try:
            from ..models import authmodule as authmodule_m
            from ..models import details as details_m
            from ..models import user as user_m
        except ImportError:
            import sys

            authmodule_m = sys.modules[__package__ + "authmodule"]
            details_m = sys.modules[__package__ + "details"]
            user_m = sys.modules[__package__ + "user"]

        d = src_dict.copy()

        _Uuid_kwargs = super().from_dict(src_dict=d).to_dict()
        _Uuid_kwargs.pop("$type")

        _external_user_details = d.pop("externalUserDetails", UNSET)
        external_user_details: Union[Unset, details_m.Details]
        if isinstance(_external_user_details, Unset):
            external_user_details = UNSET
        else:
            external_user_details = details_m.Details.from_dict(_external_user_details)

        _persisted_user_details = d.pop("persistedUserDetails", UNSET)
        persisted_user_details: Union[Unset, details_m.Details]
        if isinstance(_persisted_user_details, Unset):
            persisted_user_details = UNSET
        else:
            persisted_user_details = details_m.Details.from_dict(_persisted_user_details)

        _similar_user = d.pop("similarUser", UNSET)
        similar_user: Union[Unset, user_m.User]
        if isinstance(_similar_user, Unset):
            similar_user = UNSET
        else:
            similar_user = user_m.User.from_dict(_similar_user)

        _auth_module = d.pop("authModule", UNSET)
        auth_module: Union[Unset, authmodule_m.Authmodule]
        if isinstance(_auth_module, Unset):
            auth_module = UNSET
        else:
            auth_module = authmodule_m.Authmodule.from_dict(_auth_module)

        auth_attempt = cls(
            external_user_details=external_user_details,
            persisted_user_details=persisted_user_details,
            similar_user=similar_user,
            auth_module=auth_module,
            **_Uuid_kwargs,
        )

        return auth_attempt
