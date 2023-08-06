from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcedProjectRole")


try:
    from ..models import project_role
except ImportError:
    import sys

    project_role = sys.modules[__package__ + "project_role"]


@attr.s(auto_attribs=True)
class SourcedProjectRole(project_role.ProjectRole):
    """ """

    sources: "Union[Unset, List[role_source_m.RoleSource]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        sources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()

                sources.append(sources_item)

        field_dict: Dict[str, Any] = {}
        _ProjectRole_dict = super().to_dict()
        field_dict.update(_ProjectRole_dict)
        field_dict.update({})
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import role_source as role_source_m
        except ImportError:
            import sys

            role_source_m = sys.modules[__package__ + "role_source"]

        d = src_dict.copy()

        sources = []
        _sources = d.pop("sources", UNSET)
        for sources_item_data in _sources or []:
            sources_item = role_source_m.RoleSource.from_dict(sources_item_data)

            sources.append(sources_item)

        sourced_project_role = cls(
            sources=sources,
        )

        return sourced_project_role
