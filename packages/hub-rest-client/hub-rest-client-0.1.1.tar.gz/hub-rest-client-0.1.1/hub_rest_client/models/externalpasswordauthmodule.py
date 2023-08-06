from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_store import KeyStore
else:
    KeyStore = "KeyStore"

from ..models.externalauthmodule import Externalauthmodule

T = TypeVar("T", bound="Externalpasswordauthmodule")


@attr.s(auto_attribs=True)
class Externalpasswordauthmodule(Externalauthmodule):
    """ """

    allowed_to_save_password: Union[Unset, bool] = UNSET
    change_password_uri: Union[Unset, str] = UNSET
    key_store: Union[Unset, KeyStore] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allowed_to_save_password = self.allowed_to_save_password
        change_password_uri = self.change_password_uri
        key_store: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_store, Unset):
            key_store = self.key_store.to_dict()

        field_dict: Dict[str, Any] = {}
        _Externalauthmodule_dict = super(Externalauthmodule).to_dict()
        field_dict.update(_Externalauthmodule_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_to_save_password is not UNSET:
            field_dict["allowedToSavePassword"] = allowed_to_save_password
        if change_password_uri is not UNSET:
            field_dict["changePasswordUri"] = change_password_uri
        if key_store is not UNSET:
            field_dict["keyStore"] = key_store

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Externalauthmodule_kwargs = super(Externalauthmodule).from_dict(src_dict=d).to_dict()

        allowed_to_save_password = d.pop("allowedToSavePassword", UNSET)

        change_password_uri = d.pop("changePasswordUri", UNSET)

        _key_store = d.pop("keyStore", UNSET)
        key_store: Union[Unset, KeyStore]
        if isinstance(_key_store, Unset):
            key_store = UNSET
        else:
            key_store = KeyStore.from_dict(_key_store)

        externalpasswordauthmodule = cls(
            allowed_to_save_password=allowed_to_save_password,
            change_password_uri=change_password_uri,
            key_store=key_store,
            **_Externalauthmodule_kwargs,
        )

        externalpasswordauthmodule.additional_properties = d
        return externalpasswordauthmodule

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
