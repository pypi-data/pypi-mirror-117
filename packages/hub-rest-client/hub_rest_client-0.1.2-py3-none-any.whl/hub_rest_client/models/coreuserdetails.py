from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Coreuserdetails")


try:
    from ..models import details
except ImportError:
    import sys

    details = sys.modules[__package__ + "details"]


@attr.s(auto_attribs=True)
class Coreuserdetails(details.Details):
    """ """

    jabber: "Union[Unset, jabber_m.Jabber]" = UNSET
    password: "Union[Unset, password_m.Password]" = UNSET
    origin_service: "Union[Unset, service_m.Service]" = UNSET
    password_change_required: "Union[Unset, bool]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        jabber: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.jabber, Unset):
            jabber = self.jabber.to_dict()

        password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        origin_service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.origin_service, Unset):
            origin_service = self.origin_service.to_dict()

        password_change_required = self.password_change_required

        field_dict: Dict[str, Any] = {}
        _Details_dict = super().to_dict()
        field_dict.update(_Details_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jabber is not UNSET:
            field_dict["jabber"] = jabber
        if password is not UNSET:
            field_dict["password"] = password
        if origin_service is not UNSET:
            field_dict["originService"] = origin_service
        if password_change_required is not UNSET:
            field_dict["passwordChangeRequired"] = password_change_required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import jabber as jabber_m
            from ..models import password as password_m
            from ..models import service as service_m
        except ImportError:
            import sys

            password_m = sys.modules[__package__ + "password"]
            jabber_m = sys.modules[__package__ + "jabber"]
            service_m = sys.modules[__package__ + "service"]

        d = src_dict.copy()

        _Details_kwargs = super().from_dict(src_dict=d).to_dict()

        _jabber = d.pop("jabber", UNSET)
        jabber: Union[Unset, jabber_m.Jabber]
        if isinstance(_jabber, Unset):
            jabber = UNSET
        else:
            jabber = jabber_m.Jabber.from_dict(_jabber)

        _password = d.pop("password", UNSET)
        password: Union[Unset, password_m.Password]
        if isinstance(_password, Unset):
            password = UNSET
        else:
            password = password_m.Password.from_dict(_password)

        _origin_service = d.pop("originService", UNSET)
        origin_service: Union[Unset, service_m.Service]
        if isinstance(_origin_service, Unset):
            origin_service = UNSET
        else:
            origin_service = service_m.Service.from_dict(_origin_service)

        password_change_required = d.pop("passwordChangeRequired", UNSET)

        coreuserdetails = cls(
            jabber=jabber,
            password=password,
            origin_service=origin_service,
            password_change_required=password_change_required,
            **_Details_kwargs,
        )

        coreuserdetails.additional_properties = d
        return coreuserdetails

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
