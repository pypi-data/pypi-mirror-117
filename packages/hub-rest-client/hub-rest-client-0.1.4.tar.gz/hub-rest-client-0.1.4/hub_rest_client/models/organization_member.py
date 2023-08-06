from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationMember")


try:
    from ..models import user
except ImportError:
    import sys

    user = sys.modules[__package__ + "user"]


@attr.s(auto_attribs=True)
class OrganizationMember(user.User):
    """ """

    organization_own_user: "Union[Unset, bool]" = UNSET
    organization_groups: "Union[Unset, List[user_group_m.UserGroup]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        organization_own_user = self.organization_own_user
        organization_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organization_groups, Unset):
            organization_groups = []
            for organization_groups_item_data in self.organization_groups:
                organization_groups_item = organization_groups_item_data.to_dict()

                organization_groups.append(organization_groups_item)

        field_dict: Dict[str, Any] = {}
        _User_dict = super().to_dict()
        field_dict.update(_User_dict)
        field_dict.update({})
        if organization_own_user is not UNSET:
            field_dict["organizationOwnUser"] = organization_own_user
        if organization_groups is not UNSET:
            field_dict["organizationGroups"] = organization_groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            user_group_m = sys.modules[__package__ + "user_group"]

        d = src_dict.copy()

        organization_own_user = d.pop("organizationOwnUser", UNSET)

        organization_groups = []
        _organization_groups = d.pop("organizationGroups", UNSET)
        for organization_groups_item_data in _organization_groups or []:
            organization_groups_item = user_group_m.UserGroup.from_dict(organization_groups_item_data)

            organization_groups.append(organization_groups_item)

        organization_member = cls(
            organization_own_user=organization_own_user,
            organization_groups=organization_groups,
        )

        return organization_member
