from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectteamsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class ProjectteamsPage(base_page.BasePage):
    """ """

    projectteams: "Union[Unset, List[project_team_m.ProjectTeam]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        projectteams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projectteams, Unset):
            projectteams = []
            for projectteams_item_data in self.projectteams:
                projectteams_item = projectteams_item_data.to_dict()

                projectteams.append(projectteams_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if projectteams is not UNSET:
            field_dict["projectteams"] = projectteams

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import project_team as project_team_m
        except ImportError:
            import sys

            project_team_m = sys.modules[__package__ + "project_team"]

        d = src_dict.copy()

        projectteams = []
        _projectteams = d.pop("projectteams", UNSET)
        for projectteams_item_data in _projectteams or []:
            projectteams_item = project_team_m.ProjectTeam.from_dict(projectteams_item_data)

            projectteams.append(projectteams_item)

        projectteams_page = cls(
            projectteams=projectteams,
        )

        projectteams_page.additional_properties = d
        return projectteams_page

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
