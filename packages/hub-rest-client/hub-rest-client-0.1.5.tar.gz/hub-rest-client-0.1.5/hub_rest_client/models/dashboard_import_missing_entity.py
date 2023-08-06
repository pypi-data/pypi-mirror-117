from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardImportMissingEntity")


@attr.s(auto_attribs=True)
class DashboardImportMissingEntity:
    """ """

    entity_type: "Union[Unset, str]" = UNSET
    entity_id: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        entity_type = self.entity_type
        entity_id = self.entity_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        entity_type = d.pop("entityType", UNSET)

        entity_id = d.pop("entityId", UNSET)

        dashboard_import_missing_entity = cls(
            entity_type=entity_type,
            entity_id=entity_id,
        )

        return dashboard_import_missing_entity
