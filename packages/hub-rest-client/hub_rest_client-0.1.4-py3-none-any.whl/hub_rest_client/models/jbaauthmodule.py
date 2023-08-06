from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Jbaauthmodule")


try:
    from ..models import externalpasswordauthmodule
except ImportError:
    import sys

    externalpasswordauthmodule = sys.modules[__package__ + "externalpasswordauthmodule"]


@attr.s(auto_attribs=True)
class Jbaauthmodule(externalpasswordauthmodule.Externalpasswordauthmodule):
    """ """

    registration_enabled: "Union[Unset, bool]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        registration_enabled = self.registration_enabled

        field_dict: Dict[str, Any] = {}
        _Externalpasswordauthmodule_dict = super().to_dict()
        field_dict.update(_Externalpasswordauthmodule_dict)
        field_dict.update({})
        if registration_enabled is not UNSET:
            field_dict["registrationEnabled"] = registration_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        registration_enabled = d.pop("registrationEnabled", UNSET)

        jbaauthmodule = cls(
            registration_enabled=registration_enabled,
        )

        return jbaauthmodule
