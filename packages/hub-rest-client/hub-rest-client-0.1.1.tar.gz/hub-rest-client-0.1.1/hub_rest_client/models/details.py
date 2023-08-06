from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alias import Alias
    from ..models.authmodule import Authmodule
    from ..models.email import Email
    from ..models.user import User
else:
    Authmodule = "Authmodule"
    User = "User"
    Email = "Email"
    Alias = "Alias"


T = TypeVar("T", bound="Details")


@attr.s(auto_attribs=True)
class Details:
    """ """

    type: str
    id: Union[Unset, str] = UNSET
    aliases: Union[Unset, List[Alias]] = UNSET
    email: Union[Unset, Email] = UNSET
    auth_module: Union[Unset, Authmodule] = UNSET
    auth_module_name: Union[Unset, str] = UNSET
    user: Union[Unset, User] = UNSET
    last_access_time: Union[Unset, int] = UNSET
    last_access_address: Union[Unset, str] = UNSET
    last_access_user_agent: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        id = self.id
        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()

                aliases.append(aliases_item)

        email: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        auth_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auth_module, Unset):
            auth_module = self.auth_module.to_dict()

        auth_module_name = self.auth_module_name
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        last_access_time = self.last_access_time
        last_access_address = self.last_access_address
        last_access_user_agent = self.last_access_user_agent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if email is not UNSET:
            field_dict["email"] = email
        if auth_module is not UNSET:
            field_dict["authModule"] = auth_module
        if auth_module_name is not UNSET:
            field_dict["authModuleName"] = auth_module_name
        if user is not UNSET:
            field_dict["user"] = user
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

        type = d.pop("type")

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        _email = d.pop("email", UNSET)
        email: Union[Unset, Email]
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = Email.from_dict(_email)

        _auth_module = d.pop("authModule", UNSET)
        auth_module: Union[Unset, Authmodule]
        if isinstance(_auth_module, Unset):
            auth_module = UNSET
        else:
            auth_module = Authmodule.from_dict(_auth_module)

        auth_module_name = d.pop("authModuleName", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        last_access_time = d.pop("lastAccessTime", UNSET)

        last_access_address = d.pop("lastAccessAddress", UNSET)

        last_access_user_agent = d.pop("lastAccessUserAgent", UNSET)

        details = cls(
            type=type,
            id=id,
            aliases=aliases,
            email=email,
            auth_module=auth_module,
            auth_module_name=auth_module_name,
            user=user,
            last_access_time=last_access_time,
            last_access_address=last_access_address,
            last_access_user_agent=last_access_user_agent,
        )

        details.additional_properties = d
        return details

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
