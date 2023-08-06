from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MergeTokens")


@attr.s(auto_attribs=True)
class MergeTokens:
    """ """

    user_id: Union[Unset, str] = UNSET
    found_users: Union[Unset, List[str]] = UNSET
    no_user_attempts: Union[Unset, List[str]] = UNSET
    create_hub_details: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        found_users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.found_users, Unset):
            found_users = self.found_users

        no_user_attempts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.no_user_attempts, Unset):
            no_user_attempts = self.no_user_attempts

        create_hub_details = self.create_hub_details

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if found_users is not UNSET:
            field_dict["foundUsers"] = found_users
        if no_user_attempts is not UNSET:
            field_dict["noUserAttempts"] = no_user_attempts
        if create_hub_details is not UNSET:
            field_dict["createHubDetails"] = create_hub_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        user_id = d.pop("userId", UNSET)

        found_users = cast(List[str], d.pop("foundUsers", UNSET))

        no_user_attempts = cast(List[str], d.pop("noUserAttempts", UNSET))

        create_hub_details = d.pop("createHubDetails", UNSET)

        merge_tokens = cls(
            user_id=user_id,
            found_users=found_users,
            no_user_attempts=no_user_attempts,
            create_hub_details=create_hub_details,
        )

        merge_tokens.additional_properties = d
        return merge_tokens

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
