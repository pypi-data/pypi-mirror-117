from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.info import Info
    from ..models.resolution import Resolution
else:
    Info = "Info"
    Resolution = "Resolution"


T = TypeVar("T", bound="Conflict")


@attr.s(auto_attribs=True)
class Conflict:
    """ """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    local: Union[Unset, Info] = UNSET
    remote: Union[Unset, Info] = UNSET
    resolution: Union[Unset, Resolution] = UNSET
    matches: Union[Unset, Info] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        local: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local, Unset):
            local = self.local.to_dict()

        remote: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remote, Unset):
            remote = self.remote.to_dict()

        resolution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.to_dict()

        matches: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.matches, Unset):
            matches = self.matches.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if local is not UNSET:
            field_dict["local"] = local
        if remote is not UNSET:
            field_dict["remote"] = remote
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if matches is not UNSET:
            field_dict["matches"] = matches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        _local = d.pop("local", UNSET)
        local: Union[Unset, Info]
        if isinstance(_local, Unset):
            local = UNSET
        else:
            local = Info.from_dict(_local)

        _remote = d.pop("remote", UNSET)
        remote: Union[Unset, Info]
        if isinstance(_remote, Unset):
            remote = UNSET
        else:
            remote = Info.from_dict(_remote)

        _resolution = d.pop("resolution", UNSET)
        resolution: Union[Unset, Resolution]
        if isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = Resolution.from_dict(_resolution)

        _matches = d.pop("matches", UNSET)
        matches: Union[Unset, Info]
        if isinstance(_matches, Unset):
            matches = UNSET
        else:
            matches = Info.from_dict(_matches)

        conflict = cls(
            id=id,
            type=type,
            local=local,
            remote=remote,
            resolution=resolution,
            matches=matches,
        )

        conflict.additional_properties = d
        return conflict

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
