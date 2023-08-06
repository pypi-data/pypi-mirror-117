from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddNewGroupOption")


try:
    from ..models import access_grant_option
except ImportError:
    import sys

    access_grant_option = sys.modules[__package__ + "access_grant_option"]


@attr.s(auto_attribs=True)
class AddNewGroupOption(access_grant_option.AccessGrantOption):
    """ """

    group_name: "Union[Unset, str]" = UNSET
    project: "Union[Unset, project_m.Project]" = UNSET
    role: "Union[Unset, role_m.Role]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        group_name = self.group_name
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        role: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        field_dict: Dict[str, Any] = {}
        _AccessGrantOption_dict = super().to_dict()
        field_dict.update(_AccessGrantOption_dict)
        field_dict.update({})
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
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

        group_name = d.pop("groupName", UNSET)

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

        add_new_group_option = cls(
            group_name=group_name,
            project=project,
            role=role,
        )

        return add_new_group_option
