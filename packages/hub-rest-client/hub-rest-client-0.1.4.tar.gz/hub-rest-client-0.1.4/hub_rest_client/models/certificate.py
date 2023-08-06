from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Certificate")


@attr.s(auto_attribs=True)
class Certificate:
    """ """

    id: "Union[Unset, str]" = UNSET
    aliases: "Union[Unset, List[alias_m.Alias]]" = UNSET
    disabled: "Union[Unset, bool]" = UNSET
    name: "Union[Unset, str]" = UNSET
    data: "Union[Unset, str]" = UNSET
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
        id = self.id
        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()

                aliases.append(aliases_item)

        disabled = self.disabled
        name = self.name
        data = self.data
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
        if id is not UNSET:
            field_dict["id"] = id
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if name is not UNSET:
            field_dict["name"] = name
        if data is not UNSET:
            field_dict["data"] = data
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
            from ..models import alias as alias_m
            from ..models import fingerprint as fingerprint_m
        except ImportError:
            import sys

            fingerprint_m = sys.modules[__package__ + "fingerprint"]
            alias_m = sys.modules[__package__ + "alias"]

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = alias_m.Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        disabled = d.pop("disabled", UNSET)

        name = d.pop("name", UNSET)

        data = d.pop("data", UNSET)

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

        certificate = cls(
            id=id,
            aliases=aliases,
            disabled=disabled,
            name=name,
            data=data,
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

        return certificate
