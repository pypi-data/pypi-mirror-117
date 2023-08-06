from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UntrustedRedirectURI")


@attr.s(auto_attribs=True)
class UntrustedRedirectURI:
    """ """

    redirect_uri: "Union[Unset, str]" = UNSET
    tried_from: "Union[Unset, str]" = UNSET
    tried_at: "Union[Unset, int]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        redirect_uri = self.redirect_uri
        tried_from = self.tried_from
        tried_at = self.tried_at

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if redirect_uri is not UNSET:
            field_dict["redirectURI"] = redirect_uri
        if tried_from is not UNSET:
            field_dict["triedFrom"] = tried_from
        if tried_at is not UNSET:
            field_dict["triedAt"] = tried_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        redirect_uri = d.pop("redirectURI", UNSET)

        tried_from = d.pop("triedFrom", UNSET)

        tried_at = d.pop("triedAt", UNSET)

        untrusted_redirect_uri = cls(
            redirect_uri=redirect_uri,
            tried_from=tried_from,
            tried_at=tried_at,
        )

        return untrusted_redirect_uri
