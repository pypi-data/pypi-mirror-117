from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.permission import Permission
    from ..models.project import Project
    from ..models.resource import Resource
else:
    Permission = "Permission"
    Resource = "Resource"
    Project = "Project"


T = TypeVar("T", bound="CachedPermission")


@attr.s(auto_attribs=True)
class CachedPermission:
    """ """

    permission: Union[Unset, Permission] = UNSET
    global_: Union[Unset, bool] = UNSET
    projects: Union[Unset, List[Project]] = UNSET
    resources: Union[Unset, List[Resource]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permission: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.to_dict()

        global_ = self.global_
        projects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()

                projects.append(projects_item)

        resources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()

                resources.append(resources_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission is not UNSET:
            field_dict["permission"] = permission
        if global_ is not UNSET:
            field_dict["global"] = global_
        if projects is not UNSET:
            field_dict["projects"] = projects
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _permission = d.pop("permission", UNSET)
        permission: Union[Unset, Permission]
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = Permission.from_dict(_permission)

        global_ = d.pop("global", UNSET)

        projects = []
        _projects = d.pop("projects", UNSET)
        for projects_item_data in _projects or []:
            projects_item = Project.from_dict(projects_item_data)

            projects.append(projects_item)

        resources = []
        _resources = d.pop("resources", UNSET)
        for resources_item_data in _resources or []:
            resources_item = Resource.from_dict(resources_item_data)

            resources.append(resources_item)

        cached_permission = cls(
            permission=permission,
            global_=global_,
            projects=projects,
            resources=resources,
        )

        cached_permission.additional_properties = d
        return cached_permission

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
