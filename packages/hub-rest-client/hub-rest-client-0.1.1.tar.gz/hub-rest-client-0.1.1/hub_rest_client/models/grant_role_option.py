from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project import Project
    from ..models.role import Role
else:
    Role = "Role"
    Project = "Project"

from ..models.access_grant_option import AccessGrantOption

T = TypeVar("T", bound="GrantRoleOption")


@attr.s(auto_attribs=True)
class GrantRoleOption(AccessGrantOption):
    """ """

    project: Union[Unset, Project] = UNSET
    role: Union[Unset, Role] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        role: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        field_dict: Dict[str, Any] = {}
        _AccessGrantOption_dict = super(AccessGrantOption).to_dict()
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
        d = src_dict.copy()

        _AccessGrantOption_kwargs = super(AccessGrantOption).from_dict(src_dict=d).to_dict()

        _project = d.pop("project", UNSET)
        project: Union[Unset, Project]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)

        _role = d.pop("role", UNSET)
        role: Union[Unset, Role]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = Role.from_dict(_role)

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
