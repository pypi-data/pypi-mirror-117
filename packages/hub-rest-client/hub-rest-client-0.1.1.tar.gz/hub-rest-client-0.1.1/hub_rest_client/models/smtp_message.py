from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User
else:
    User = "User"


T = TypeVar("T", bound="SmtpMessage")


@attr.s(auto_attribs=True)
class SmtpMessage:
    """ """

    to: Union[Unset, User] = UNSET
    subject: Union[Unset, str] = UNSET
    html_text: Union[Unset, str] = UNSET
    unsubscribe_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        subject = self.subject
        html_text = self.html_text
        unsubscribe_url = self.unsubscribe_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if to is not UNSET:
            field_dict["to"] = to
        if subject is not UNSET:
            field_dict["subject"] = subject
        if html_text is not UNSET:
            field_dict["htmlText"] = html_text
        if unsubscribe_url is not UNSET:
            field_dict["unsubscribeURL"] = unsubscribe_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _to = d.pop("to", UNSET)
        to: Union[Unset, User]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = User.from_dict(_to)

        subject = d.pop("subject", UNSET)

        html_text = d.pop("htmlText", UNSET)

        unsubscribe_url = d.pop("unsubscribeURL", UNSET)

        smtp_message = cls(
            to=to,
            subject=subject,
            html_text=html_text,
            unsubscribe_url=unsubscribe_url,
        )

        smtp_message.additional_properties = d
        return smtp_message

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
