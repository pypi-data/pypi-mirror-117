from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authority_holder import AuthorityHolder
else:
    AuthorityHolder = "AuthorityHolder"

from ..models.hub_feature import HubFeature

T = TypeVar("T", bound="ScopedFeature")


@attr.s(auto_attribs=True)
class ScopedFeature(HubFeature):
    """ """

    scopes: Union[Unset, List[AuthorityHolder]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scopes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.to_dict()

                scopes.append(scopes_item)

        field_dict: Dict[str, Any] = {}
        _HubFeature_dict = super(HubFeature).to_dict()
        field_dict.update(_HubFeature_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _HubFeature_kwargs = super(HubFeature).from_dict(src_dict=d).to_dict()

        scopes = []
        _scopes = d.pop("scopes", UNSET)
        for scopes_item_data in _scopes or []:
            scopes_item = AuthorityHolder.from_dict(scopes_item_data)

            scopes.append(scopes_item)

        scoped_feature = cls(
            scopes=scopes,
            **_HubFeature_kwargs,
        )

        scoped_feature.additional_properties = d
        return scoped_feature

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
