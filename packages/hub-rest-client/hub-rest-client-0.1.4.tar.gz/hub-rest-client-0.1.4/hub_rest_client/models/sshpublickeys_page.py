from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SshpublickeysPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class SshpublickeysPage(base_page.BasePage):
    """ """

    sshpublickeys: "Union[Unset, List[ssh_public_key_m.SshPublicKey]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        sshpublickeys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sshpublickeys, Unset):
            sshpublickeys = []
            for sshpublickeys_item_data in self.sshpublickeys:
                sshpublickeys_item = sshpublickeys_item_data.to_dict()

                sshpublickeys.append(sshpublickeys_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if sshpublickeys is not UNSET:
            field_dict["sshpublickeys"] = sshpublickeys

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import ssh_public_key as ssh_public_key_m
        except ImportError:
            import sys

            ssh_public_key_m = sys.modules[__package__ + "ssh_public_key"]

        d = src_dict.copy()

        sshpublickeys = []
        _sshpublickeys = d.pop("sshpublickeys", UNSET)
        for sshpublickeys_item_data in _sshpublickeys or []:
            sshpublickeys_item = ssh_public_key_m.SshPublicKey.from_dict(sshpublickeys_item_data)

            sshpublickeys.append(sshpublickeys_item)

        sshpublickeys_page = cls(
            sshpublickeys=sshpublickeys,
        )

        return sshpublickeys_page
