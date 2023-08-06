from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project import Project
else:
    Project = "Project"

from ..models.base_page import BasePage

T = TypeVar("T", bound="FavoriteprojectsPage")


@attr.s(auto_attribs=True)
class FavoriteprojectsPage(BasePage):
    """ """

    favoriteprojects: Union[Unset, List[Project]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        favoriteprojects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.favoriteprojects, Unset):
            favoriteprojects = []
            for favoriteprojects_item_data in self.favoriteprojects:
                favoriteprojects_item = favoriteprojects_item_data.to_dict()

                favoriteprojects.append(favoriteprojects_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super(BasePage).to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if favoriteprojects is not UNSET:
            field_dict["favoriteprojects"] = favoriteprojects

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BasePage_kwargs = super(BasePage).from_dict(src_dict=d).to_dict()

        favoriteprojects = []
        _favoriteprojects = d.pop("favoriteprojects", UNSET)
        for favoriteprojects_item_data in _favoriteprojects or []:
            favoriteprojects_item = Project.from_dict(favoriteprojects_item_data)

            favoriteprojects.append(favoriteprojects_item)

        favoriteprojects_page = cls(
            favoriteprojects=favoriteprojects,
            **_BasePage_kwargs,
        )

        favoriteprojects_page.additional_properties = d
        return favoriteprojects_page

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
