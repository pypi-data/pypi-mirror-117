from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthResults")


@attr.s(auto_attribs=True)
class AuthResults:
    """ """

    found_users: "Union[Unset, List[auth_found_user_m.AuthFoundUser]]" = UNSET
    no_user_attempts: "Union[Unset, List[auth_attempt_m.AuthAttempt]]" = UNSET
    create_hub_details: "Union[Unset, create_hub_details_m.CreateHubDetails]" = UNSET

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

        try:
            from ..models import auth_attempt as auth_attempt_m
            from ..models import auth_found_user as auth_found_user_m
            from ..models import create_hub_details as create_hub_details_m
        except ImportError:
            import sys

            auth_attempt_m = sys.modules[__package__ + "auth_attempt"]
            create_hub_details_m = sys.modules[__package__ + "create_hub_details"]
            auth_found_user_m = sys.modules[__package__ + "auth_found_user"]

        d = src_dict.copy()

        found_users = []
        _found_users = d.pop("foundUsers", UNSET)
        for found_users_item_data in _found_users or []:
            found_users_item = auth_found_user_m.AuthFoundUser.from_dict(found_users_item_data)

            found_users.append(found_users_item)

        no_user_attempts = []
        _no_user_attempts = d.pop("noUserAttempts", UNSET)
        for no_user_attempts_item_data in _no_user_attempts or []:
            no_user_attempts_item = auth_attempt_m.AuthAttempt.from_dict(no_user_attempts_item_data)

            no_user_attempts.append(no_user_attempts_item)

        _create_hub_details = d.pop("createHubDetails", UNSET)
        create_hub_details: Union[Unset, create_hub_details_m.CreateHubDetails]
        if isinstance(_create_hub_details, Unset):
            create_hub_details = UNSET
        else:
            create_hub_details = create_hub_details_m.CreateHubDetails.from_dict(_create_hub_details)

        auth_results = cls(
            found_users=found_users,
            no_user_attempts=no_user_attempts,
            create_hub_details=create_hub_details,
        )

        return auth_results
