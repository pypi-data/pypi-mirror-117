from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmtpMessage")


@attr.s(auto_attribs=True)
class SmtpMessage:
    """ """

    to: "Union[Unset, user_m.User]" = UNSET
    subject: "Union[Unset, str]" = UNSET
    html_text: "Union[Unset, str]" = UNSET
    unsubscribe_url: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        subject = self.subject
        html_text = self.html_text
        unsubscribe_url = self.unsubscribe_url

        field_dict: Dict[str, Any] = {}
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

        try:
            from ..models import user as user_m
        except ImportError:
            import sys

            user_m = sys.modules[__package__ + "user"]

        d = src_dict.copy()

        _to = d.pop("to", UNSET)
        to: Union[Unset, user_m.User]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = user_m.User.from_dict(_to)

        subject = d.pop("subject", UNSET)

        html_text = d.pop("htmlText", UNSET)

        unsubscribe_url = d.pop("unsubscribeURL", UNSET)

        smtp_message = cls(
            to=to,
            subject=subject,
            html_text=html_text,
            unsubscribe_url=unsubscribe_url,
        )

        return smtp_message
