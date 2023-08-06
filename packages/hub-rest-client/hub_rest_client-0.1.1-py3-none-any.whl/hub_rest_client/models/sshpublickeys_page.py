from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssh_public_key import SshPublicKey
else:
    SshPublicKey = "SshPublicKey"

from ..models.base_page import BasePage

T = TypeVar("T", bound="SshpublickeysPage")


@attr.s(auto_attribs=True)
class SshpublickeysPage(BasePage):
    """ """

    sshpublickeys: Union[Unset, List[SshPublicKey]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sshpublickeys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sshpublickeys, Unset):
            sshpublickeys = []
            for sshpublickeys_item_data in self.sshpublickeys:
                sshpublickeys_item = sshpublickeys_item_data.to_dict()

                sshpublickeys.append(sshpublickeys_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sshpublickeys is not UNSET:
            field_dict["sshpublickeys"] = sshpublickeys

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        sshpublickeys = []
        _sshpublickeys = d.pop("sshpublickeys", UNSET)
        for sshpublickeys_item_data in _sshpublickeys or []:
            sshpublickeys_item = SshPublicKey.from_dict(sshpublickeys_item_data)

            sshpublickeys.append(sshpublickeys_item)

        sshpublickeys_page = cls(
            sshpublickeys=sshpublickeys,
            **_BasePage_kwargs,
        )

        sshpublickeys_page.additional_properties = d
        return sshpublickeys_page

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
