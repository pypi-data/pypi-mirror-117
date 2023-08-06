from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserDashboardImport")


@attr.s(auto_attribs=True)
class UserDashboardImport:
    """ """

    id: "Union[Unset, str]" = UNSET
    user: "Union[Unset, str]" = UNSET
    favorite: "Union[Unset, bool]" = UNSET
    ordinal: "Union[Unset, int]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user = self.user
        favorite = self.favorite
        ordinal = self.ordinal

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user is not UNSET:
            field_dict["user"] = user
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        user = d.pop("user", UNSET)

        favorite = d.pop("favorite", UNSET)

        ordinal = d.pop("ordinal", UNSET)

        user_dashboard_import = cls(
            id=id,
            user=user,
            favorite=favorite,
            ordinal=ordinal,
        )

        return user_dashboard_import
