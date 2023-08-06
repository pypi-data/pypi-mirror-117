from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate import Certificate
else:
    Certificate = "Certificate"

from ..models.user_creation_auth_module import UserCreationAuthModule

T = TypeVar("T", bound="ClientCertificateAuthModule")


@attr.s(auto_attribs=True)
class ClientCertificateAuthModule(UserCreationAuthModule):
    """ """

    email_rdn: Union[Unset, str] = UNSET
    trusted_issuers: Union[Unset, List[Certificate]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email_rdn = self.email_rdn
        trusted_issuers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.trusted_issuers, Unset):
            trusted_issuers = []
            for trusted_issuers_item_data in self.trusted_issuers:
                trusted_issuers_item = trusted_issuers_item_data.to_dict()

                trusted_issuers.append(trusted_issuers_item)

        field_dict: Dict[str, Any] = {}
        _UserCreationAuthModule_dict = super(UserCreationAuthModule).to_dict()
        field_dict.update(_UserCreationAuthModule_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email_rdn is not UNSET:
            field_dict["emailRdn"] = email_rdn
        if trusted_issuers is not UNSET:
            field_dict["trustedIssuers"] = trusted_issuers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _UserCreationAuthModule_kwargs = super(UserCreationAuthModule).from_dict(src_dict=d).to_dict()

        email_rdn = d.pop("emailRdn", UNSET)

        trusted_issuers = []
        _trusted_issuers = d.pop("trustedIssuers", UNSET)
        for trusted_issuers_item_data in _trusted_issuers or []:
            trusted_issuers_item = Certificate.from_dict(trusted_issuers_item_data)

            trusted_issuers.append(trusted_issuers_item)

        client_certificate_auth_module = cls(
            email_rdn=email_rdn,
            trusted_issuers=trusted_issuers,
            **_UserCreationAuthModule_kwargs,
        )

        client_certificate_auth_module.additional_properties = d
        return client_certificate_auth_module

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
