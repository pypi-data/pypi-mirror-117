from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GrantRoleOption")


try:
    from ..models import access_grant_option
except ImportError:
    import sys

    access_grant_option = sys.modules[__package__ + "access_grant_option"]


@attr.s(auto_attribs=True)
class GrantRoleOption(access_grant_option.AccessGrantOption):
    """ """

    project: "Union[Unset, project_m.Project]" = UNSET
    role: "Union[Unset, role_m.Role]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        role: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        field_dict: Dict[str, Any] = {}
        _AccessGrantOption_dict = super().to_dict()
        field_dict.update(_AccessGrantOption_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project is not UNSET:
            field_dict["project"] = project
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import project as project_m
            from ..models import role as role_m
        except ImportError:
            import sys

            project_m = sys.modules[__package__ + "project"]
            role_m = sys.modules[__package__ + "role"]

        d = src_dict.copy()

        _AccessGrantOption_kwargs = super().from_dict(src_dict=d).to_dict()

        _project = d.pop("project", UNSET)
        project: Union[Unset, project_m.Project]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = project_m.Project.from_dict(_project)

        _role = d.pop("role", UNSET)
        role: Union[Unset, role_m.Role]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = role_m.Role.from_dict(_role)

        grant_role_option = cls(
            project=project,
            role=role,
            **_AccessGrantOption_kwargs,
        )

        grant_role_option.additional_properties = d
        return grant_role_option

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
