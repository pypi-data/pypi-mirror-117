from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.details import Details
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientCertificateUserDetails")


@attr.s(auto_attribs=True)
class ClientCertificateUserDetails(Details):
    """ """

    thumbprint: Union[Unset, str] = UNSET
    common_name: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        thumbprint = self.thumbprint
        common_name = self.common_name
        disabled = self.disabled

        field_dict: Dict[str, Any] = {}
        _Details_dict = super(Details).to_dict()
        field_dict.update(_Details_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if thumbprint is not UNSET:
            field_dict["thumbprint"] = thumbprint
        if common_name is not UNSET:
            field_dict["commonName"] = common_name
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Details_kwargs = super(Details).from_dict(src_dict=d).to_dict()

        thumbprint = d.pop("thumbprint", UNSET)

        common_name = d.pop("commonName", UNSET)

        disabled = d.pop("disabled", UNSET)

        client_certificate_user_details = cls(
            thumbprint=thumbprint,
            common_name=common_name,
            disabled=disabled,
            **_Details_kwargs,
        )

        client_certificate_user_details.additional_properties = d
        return client_certificate_user_details

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
