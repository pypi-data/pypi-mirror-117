from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CachedPermission")


@attr.s(auto_attribs=True)
class CachedPermission:
    """ """

    permission: "Union[Unset, permission_m.Permission]" = UNSET
    global_: "Union[Unset, bool]" = UNSET
    projects: "Union[Unset, List[project_m.Project]]" = UNSET
    resources: "Union[Unset, List[resource_m.Resource]]" = UNSET

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

        try:
            from ..models import permission as permission_m
            from ..models import project as project_m
            from ..models import resource as resource_m
        except ImportError:
            import sys

            project_m = sys.modules[__package__ + "project"]
            permission_m = sys.modules[__package__ + "permission"]
            resource_m = sys.modules[__package__ + "resource"]

        d = src_dict.copy()

        _permission = d.pop("permission", UNSET)
        permission: Union[Unset, permission_m.Permission]
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = permission_m.Permission.from_dict(_permission)

        global_ = d.pop("global", UNSET)

        projects = []
        _projects = d.pop("projects", UNSET)
        for projects_item_data in _projects or []:
            projects_item = project_m.Project.from_dict(projects_item_data)

            projects.append(projects_item)

        resources = []
        _resources = d.pop("resources", UNSET)
        for resources_item_data in _resources or []:
            resources_item = resource_m.Resource.from_dict(resources_item_data)

            resources.append(resources_item)

        cached_permission = cls(
            permission=permission,
            global_=global_,
            projects=projects,
            resources=resources,
        )

        return cached_permission
