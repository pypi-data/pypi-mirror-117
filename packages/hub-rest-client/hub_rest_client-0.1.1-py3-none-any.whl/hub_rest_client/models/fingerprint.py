from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Fingerprint")


@attr.s(auto_attribs=True)
class Fingerprint:
    """ """

    md5: Union[Unset, str] = UNSET
    sha1: Union[Unset, str] = UNSET
    sha256: Union[Unset, str] = UNSET
    sha384: Union[Unset, str] = UNSET
    sha512: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        md5 = self.md5
        sha1 = self.sha1
        sha256 = self.sha256
        sha384 = self.sha384
        sha512 = self.sha512

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if md5 is not UNSET:
            field_dict["md5"] = md5
        if sha1 is not UNSET:
            field_dict["sha1"] = sha1
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if sha384 is not UNSET:
            field_dict["sha384"] = sha384
        if sha512 is not UNSET:
            field_dict["sha512"] = sha512

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        md5 = d.pop("md5", UNSET)

        sha1 = d.pop("sha1", UNSET)

        sha256 = d.pop("sha256", UNSET)

        sha384 = d.pop("sha384", UNSET)

        sha512 = d.pop("sha512", UNSET)

        fingerprint = cls(
            md5=md5,
            sha1=sha1,
            sha256=sha256,
            sha384=sha384,
            sha512=sha512,
        )

        fingerprint.additional_properties = d
        return fingerprint

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
