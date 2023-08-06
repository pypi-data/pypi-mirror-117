from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conflict import Conflict
    from ..models.import_phase import ImportPhase
else:
    ImportPhase = "ImportPhase"
    Conflict = "Conflict"


T = TypeVar("T", bound="Import")


@attr.s(auto_attribs=True)
class Import:
    """ """

    id: Union[Unset, str] = UNSET
    admin_console_url: Union[Unset, str] = UNSET
    remote_url: Union[Unset, str] = UNSET
    local_url: Union[Unset, str] = UNSET
    phase: Union[Unset, ImportPhase] = UNSET
    conflicts: Union[Unset, List[Conflict]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        admin_console_url = self.admin_console_url
        remote_url = self.remote_url
        local_url = self.local_url
        phase: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.to_dict()

        conflicts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conflicts, Unset):
            conflicts = []
            for conflicts_item_data in self.conflicts:
                conflicts_item = conflicts_item_data.to_dict()

                conflicts.append(conflicts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if admin_console_url is not UNSET:
            field_dict["adminConsoleUrl"] = admin_console_url
        if remote_url is not UNSET:
            field_dict["remoteUrl"] = remote_url
        if local_url is not UNSET:
            field_dict["localUrl"] = local_url
        if phase is not UNSET:
            field_dict["phase"] = phase
        if conflicts is not UNSET:
            field_dict["conflicts"] = conflicts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        id = d.pop("id", UNSET)

        admin_console_url = d.pop("adminConsoleUrl", UNSET)

        remote_url = d.pop("remoteUrl", UNSET)

        local_url = d.pop("localUrl", UNSET)

        _phase = d.pop("phase", UNSET)
        phase: Union[Unset, ImportPhase]
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = ImportPhase.from_dict(_phase)

        conflicts = []
        _conflicts = d.pop("conflicts", UNSET)
        for conflicts_item_data in _conflicts or []:
            conflicts_item = Conflict.from_dict(conflicts_item_data)

            conflicts.append(conflicts_item)

        import_ = cls(
            id=id,
            admin_console_url=admin_console_url,
            remote_url=remote_url,
            local_url=local_url,
            phase=phase,
            conflicts=conflicts,
        )

        import_.additional_properties = d
        return import_

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
