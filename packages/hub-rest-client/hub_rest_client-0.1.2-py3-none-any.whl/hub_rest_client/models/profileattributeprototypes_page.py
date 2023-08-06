from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileattributeprototypesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class ProfileattributeprototypesPage(base_page.BasePage):
    """ """

    profileattributeprototypes: "Union[Unset, List[profile_attribute_prototype_m.ProfileAttributePrototype]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        profileattributeprototypes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.profileattributeprototypes, Unset):
            profileattributeprototypes = []
            for profileattributeprototypes_item_data in self.profileattributeprototypes:
                profileattributeprototypes_item = profileattributeprototypes_item_data.to_dict()

                profileattributeprototypes.append(profileattributeprototypes_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profileattributeprototypes is not UNSET:
            field_dict["profileattributeprototypes"] = profileattributeprototypes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import profile_attribute_prototype as profile_attribute_prototype_m
        except ImportError:
            import sys

            profile_attribute_prototype_m = sys.modules[__package__ + "profile_attribute_prototype"]

        d = src_dict.copy()

        _BasePage_kwargs = super().from_dict(src_dict=d).to_dict()

        profileattributeprototypes = []
        _profileattributeprototypes = d.pop("profileattributeprototypes", UNSET)
        for profileattributeprototypes_item_data in _profileattributeprototypes or []:
            profileattributeprototypes_item = profile_attribute_prototype_m.ProfileAttributePrototype.from_dict(
                profileattributeprototypes_item_data
            )

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
