from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role_source import RoleSource
else:
    RoleSource = "RoleSource"

from ..models.project_role import ProjectRole

T = TypeVar("T", bound="SourcedProjectRole")


@attr.s(auto_attribs=True)
class SourcedProjectRole(ProjectRole):
    """ """

    sources: Union[Unset, List[RoleSource]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()

                sources.append(sources_item)

        field_dict: Dict[str, Any] = {}
        _ProjectRole_dict = super(ProjectRole).to_dict()
        field_dict.update(_ProjectRole_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _ProjectRole_kwargs = super(ProjectRole).from_dict(src_dict=d).to_dict()

        sources = []
        _sources = d.pop("sources", UNSET)
        for sources_item_data in _sources or []:
            sources_item = RoleSource.from_dict(sources_item_data)

            sources.append(sources_item)

        sourced_project_role = cls(
            sources=sources,
            **_ProjectRole_kwargs,
        )

        sourced_project_role.additional_properties = d
        return sourced_project_role

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
