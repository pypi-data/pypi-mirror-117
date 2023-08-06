from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientCertificateAuthModule")


try:
    from ..models import user_creation_auth_module
except ImportError:
    import sys

    user_creation_auth_module = sys.modules[__package__ + "user_creation_auth_module"]


@attr.s(auto_attribs=True)
class ClientCertificateAuthModule(user_creation_auth_module.UserCreationAuthModule):
    """ """

    email_rdn: "Union[Unset, str]" = UNSET
    trusted_issuers: "Union[Unset, List[certificate_m.Certificate]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        email_rdn = self.email_rdn
        trusted_issuers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.trusted_issuers, Unset):
            trusted_issuers = []
            for trusted_issuers_item_data in self.trusted_issuers:
                trusted_issuers_item = trusted_issuers_item_data.to_dict()

                trusted_issuers.append(trusted_issuers_item)

        field_dict: Dict[str, Any] = {}
        _UserCreationAuthModule_dict = super().to_dict()
        field_dict.update(_UserCreationAuthModule_dict)
        field_dict.update({})
        if email_rdn is not UNSET:
            field_dict["emailRdn"] = email_rdn
        if trusted_issuers is not UNSET:
            field_dict["trustedIssuers"] = trusted_issuers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import certificate as certificate_m
        except ImportError:
            import sys

            certificate_m = sys.modules[__package__ + "certificate"]

        d = src_dict.copy()

        _UserCreationAuthModule_kwargs = super().from_dict(src_dict=d).to_dict()
        _UserCreationAuthModule_kwargs.pop("$type")

        email_rdn = d.pop("emailRdn", UNSET)

        trusted_issuers = []
        _trusted_issuers = d.pop("trustedIssuers", UNSET)
        for trusted_issuers_item_data in _trusted_issuers or []:
            trusted_issuers_item = certificate_m.Certificate.from_dict(trusted_issuers_item_data)

            trusted_issuers.append(trusted_issuers_item)

        client_certificate_auth_module = cls(
            email_rdn=email_rdn,
            trusted_issuers=trusted_issuers,
            **_UserCreationAuthModule_kwargs,
        )

        return client_certificate_auth_module
