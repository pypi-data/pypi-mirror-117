from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Import")


@attr.s(auto_attribs=True)
class Import:
    """ """

    id: "Union[Unset, str]" = UNSET
    admin_console_url: "Union[Unset, str]" = UNSET
    remote_url: "Union[Unset, str]" = UNSET
    local_url: "Union[Unset, str]" = UNSET
    phase: "Union[Unset, import_phase_m.ImportPhase]" = UNSET
    conflicts: "Union[Unset, List[conflict_m.Conflict]]" = UNSET

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

        try:
            from ..models import conflict as conflict_m
            from ..models import import_phase as import_phase_m
        except ImportError:
            import sys

            import_phase_m = sys.modules[__package__ + "import_phase"]
            conflict_m = sys.modules[__package__ + "conflict"]

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        admin_console_url = d.pop("adminConsoleUrl", UNSET)

        remote_url = d.pop("remoteUrl", UNSET)

        local_url = d.pop("localUrl", UNSET)

        _phase = d.pop("phase", UNSET)
        phase: Union[Unset, import_phase_m.ImportPhase]
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = import_phase_m.ImportPhase.from_dict(_phase)

        conflicts = []
        _conflicts = d.pop("conflicts", UNSET)
        for conflicts_item_data in _conflicts or []:
            conflicts_item = conflict_m.Conflict.from_dict(conflicts_item_data)

            conflicts.append(conflicts_item)

        import_ = cls(
            id=id,
            admin_console_url=admin_console_url,
            remote_url=remote_url,
            local_url=local_url,
            phase=phase,
            conflicts=conflicts,
        )

        return import_
