from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User
else:
    User = "User"


T = TypeVar("T", bound="ApplicationPassword")


@attr.s(auto_attribs=True)
class ApplicationPassword:
    """ """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    user: Union[Unset, User] = UNSET
    creation_time: Union[Unset, int] = UNSET
    last_access_time: Union[Unset, int] = UNSET
    last_access_address: Union[Unset, str] = UNSET
    last_access_user_agent: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        password = self.password
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        creation_time = self.creation_time
        last_access_time = self.last_access_time
        last_access_address = self.last_access_address
        last_access_user_agent = self.last_access_user_agent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if password is not UNSET:
            field_dict["password"] = password
        if user is not UNSET:
            field_dict["user"] = user
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if last_access_time is not UNSET:
            field_dict["lastAccessTime"] = last_access_time
        if last_access_address is not UNSET:
            field_dict["lastAccessAddress"] = last_access_address
        if last_access_user_agent is not UNSET:
            field_dict["lastAccessUserAgent"] = last_access_user_agent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        password = d.pop("password", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        creation_time = d.pop("creationTime", UNSET)

        last_access_time = d.pop("lastAccessTime", UNSET)

        last_access_address = d.pop("lastAccessAddress", UNSET)

        last_access_user_agent = d.pop("lastAccessUserAgent", UNSET)

        application_password = cls(
            id=id,
            name=name,
            password=password,
            user=user,
            creation_time=creation_time,
            last_access_time=last_access_time,
            last_access_address=last_access_address,
            last_access_user_agent=last_access_user_agent,
        )

        application_password.additional_properties = d
        return application_password

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
