from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SshPublicKey")


@attr.s(auto_attribs=True)
class SshPublicKey:
    """ """

    finger_print: Union[Unset, str] = UNSET
    data: Union[Unset, str] = UNSET
    open_ssh_key: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        finger_print = self.finger_print
        data = self.data
        open_ssh_key = self.open_ssh_key
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if finger_print is not UNSET:
            field_dict["fingerPrint"] = finger_print
        if data is not UNSET:
            field_dict["data"] = data
        if open_ssh_key is not UNSET:
            field_dict["openSshKey"] = open_ssh_key
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        finger_print = d.pop("fingerPrint", UNSET)

        data = d.pop("data", UNSET)

        open_ssh_key = d.pop("openSshKey", UNSET)

        comment = d.pop("comment", UNSET)

        ssh_public_key = cls(
            finger_print=finger_print,
            data=data,
            open_ssh_key=open_ssh_key,
            comment=comment,
        )

        ssh_public_key.additional_properties = d
        return ssh_public_key

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
