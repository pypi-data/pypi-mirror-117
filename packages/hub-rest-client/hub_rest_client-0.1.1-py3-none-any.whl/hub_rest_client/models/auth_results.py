from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_attempt import AuthAttempt
    from ..models.auth_found_user import AuthFoundUser
    from ..models.create_hub_details import CreateHubDetails
else:
    AuthAttempt = "AuthAttempt"
    AuthFoundUser = "AuthFoundUser"
    CreateHubDetails = "CreateHubDetails"


T = TypeVar("T", bound="AuthResults")


@attr.s(auto_attribs=True)
class AuthResults:
    """ """

    found_users: Union[Unset, List[AuthFoundUser]] = UNSET
    no_user_attempts: Union[Unset, List[AuthAttempt]] = UNSET
    create_hub_details: Union[Unset, CreateHubDetails] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        found_users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.found_users, Unset):
            found_users = []
            for found_users_item_data in self.found_users:
                found_users_item = found_users_item_data.to_dict()

                found_users.append(found_users_item)

        no_user_attempts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.no_user_attempts, Unset):
            no_user_attempts = []
            for no_user_attempts_item_data in self.no_user_attempts:
                no_user_attempts_item = no_user_attempts_item_data.to_dict()

                no_user_attempts.append(no_user_attempts_item)

        create_hub_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.create_hub_details, Unset):
            create_hub_details = self.create_hub_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

        found_users = []
        _found_users = d.pop("foundUsers", UNSET)
        for found_users_item_data in _found_users or []:
            found_users_item = AuthFoundUser.from_dict(found_users_item_data)

            found_users.append(found_users_item)

        no_user_attempts = []
        _no_user_attempts = d.pop("noUserAttempts", UNSET)
        for no_user_attempts_item_data in _no_user_attempts or []:
            no_user_attempts_item = AuthAttempt.from_dict(no_user_attempts_item_data)

            no_user_attempts.append(no_user_attempts_item)

        _create_hub_details = d.pop("createHubDetails", UNSET)
        create_hub_details: Union[Unset, CreateHubDetails]
        if isinstance(_create_hub_details, Unset):
            create_hub_details = UNSET
        else:
            create_hub_details = CreateHubDetails.from_dict(_create_hub_details)

        auth_results = cls(
            found_users=found_users,
            no_user_attempts=no_user_attempts,
            create_hub_details=create_hub_details,
        )

        auth_results.additional_properties = d
        return auth_results

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
