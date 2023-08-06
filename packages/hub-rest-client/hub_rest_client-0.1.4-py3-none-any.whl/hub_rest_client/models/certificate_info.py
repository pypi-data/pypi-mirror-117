from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificateInfo")


@attr.s(auto_attribs=True)
class CertificateInfo:
    """ """

    certificate_type: "Union[Unset, str]" = UNSET
    version: "Union[Unset, int]" = UNSET
    serial_number: "Union[Unset, str]" = UNSET
    issued_by: "Union[Unset, str]" = UNSET
    issued_to: "Union[Unset, str]" = UNSET
    valid_from: "Union[Unset, int]" = UNSET
    valid_to: "Union[Unset, int]" = UNSET
    algorithm: "Union[Unset, str]" = UNSET
    fingerprint: "Union[Unset, fingerprint_m.Fingerprint]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        certificate_type = self.certificate_type
        version = self.version
        serial_number = self.serial_number
        issued_by = self.issued_by
        issued_to = self.issued_to
        valid_from = self.valid_from
        valid_to = self.valid_to
        algorithm = self.algorithm
        fingerprint: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fingerprint, Unset):
            fingerprint = self.fingerprint.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if certificate_type is not UNSET:
            field_dict["certificateType"] = certificate_type
        if version is not UNSET:
            field_dict["version"] = version
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if issued_by is not UNSET:
            field_dict["issuedBy"] = issued_by
        if issued_to is not UNSET:
            field_dict["issuedTo"] = issued_to
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to
        if algorithm is not UNSET:
            field_dict["algorithm"] = algorithm
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import fingerprint as fingerprint_m
        except ImportError:
            import sys

            fingerprint_m = sys.modules[__package__ + "fingerprint"]

        d = src_dict.copy()

        certificate_type = d.pop("certificateType", UNSET)

        version = d.pop("version", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        issued_by = d.pop("issuedBy", UNSET)

        issued_to = d.pop("issuedTo", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        algorithm = d.pop("algorithm", UNSET)

        _fingerprint = d.pop("fingerprint", UNSET)
        fingerprint: Union[Unset, fingerprint_m.Fingerprint]
        if isinstance(_fingerprint, Unset):
            fingerprint = UNSET
        else:
            fingerprint = fingerprint_m.Fingerprint.from_dict(_fingerprint)

        certificate_info = cls(
            certificate_type=certificate_type,
            version=version,
            serial_number=serial_number,
            issued_by=issued_by,
            issued_to=issued_to,
            valid_from=valid_from,
            valid_to=valid_to,
            algorithm=algorithm,
            fingerprint=fingerprint,
        )

        return certificate_info
