from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_grant_option import AccessGrantOption
else:
    AccessGrantOption = "AccessGrantOption"


T = TypeVar("T", bound="AccessGrantOptionList")


@attr.s(auto_attribs=True)
class AccessGrantOptionList:
    """ """

    has_already: Union[Unset, bool] = UNSET
    options: Union[Unset, List[AccessGrantOption]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        has_already = self.has_already
        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()

                options.append(options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_already is not UNSET:
            field_dict["hasAlready"] = has_already
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        has_already = d.pop("hasAlready", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = AccessGrantOption.from_dict(options_item_data)

            options.append(options_item)

        access_grant_option_list = cls(
            has_already=has_already,
            options=options,
        )

        access_grant_option_list.additional_properties = d
        return access_grant_option_list

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
