from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectrolesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class ProjectrolesPage(base_page.BasePage):
    """ """

    projectroles: "Union[Unset, List[project_role_m.ProjectRole]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        projectroles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projectroles, Unset):
            projectroles = []
            for projectroles_item_data in self.projectroles:
                projectroles_item = projectroles_item_data.to_dict()

                projectroles.append(projectroles_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if projectroles is not UNSET:
            field_dict["projectroles"] = projectroles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import project_role as project_role_m
        except ImportError:
            import sys

            project_role_m = sys.modules[__package__ + "project_role"]

        d = src_dict.copy()

        _BasePage_kwargs = super().from_dict(src_dict=d).to_dict()

        projectroles = []
        _projectroles = d.pop("projectroles", UNSET)
        for projectroles_item_data in _projectroles or []:
            projectroles_item = project_role_m.ProjectRole.from_dict(projectroles_item_data)

            projectroles.append(projectroles_item)

        projectroles_page = cls(
            projectroles=projectroles,
            **_BasePage_kwargs,
        )

        projectroles_page.additional_properties = d
        return projectroles_page

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
