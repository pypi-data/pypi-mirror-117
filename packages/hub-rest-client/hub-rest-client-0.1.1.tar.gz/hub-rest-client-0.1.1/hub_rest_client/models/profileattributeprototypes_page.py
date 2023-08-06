from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_attribute_prototype import ProfileAttributePrototype
else:
    ProfileAttributePrototype = "ProfileAttributePrototype"

from ..models.base_page import BasePage

T = TypeVar("T", bound="ProfileattributeprototypesPage")


@attr.s(auto_attribs=True)
class ProfileattributeprototypesPage(BasePage):
    """ """

    profileattributeprototypes: Union[Unset, List[ProfileAttributePrototype]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        profileattributeprototypes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.profileattributeprototypes, Unset):
            profileattributeprototypes = []
            for profileattributeprototypes_item_data in self.profileattributeprototypes:
                profileattributeprototypes_item = profileattributeprototypes_item_data.to_dict()

                profileattributeprototypes.append(profileattributeprototypes_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profileattributeprototypes is not UNSET:
            field_dict["profileattributeprototypes"] = profileattributeprototypes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        profileattributeprototypes = []
        _profileattributeprototypes = d.pop("profileattributeprototypes", UNSET)
        for profileattributeprototypes_item_data in _profileattributeprototypes or []:
            profileattributeprototypes_item = ProfileAttributePrototype.from_dict(profileattributeprototypes_item_data)

            profileattributeprototypes.append(profileattributeprototypes_item)

        profileattributeprototypes_page = cls(
            profileattributeprototypes=profileattributeprototypes,
            **_BasePage_kwargs,
        )

        profileattributeprototypes_page.additional_properties = d
        return profileattributeprototypes_page

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
