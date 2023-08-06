from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alias import Alias
    from ..models.database import Database
    from ..models.memory import Memory
else:
    Database = "Database"
    Memory = "Memory"
    Alias = "Alias"


T = TypeVar("T", bound="Metrics")


@attr.s(auto_attribs=True)
class Metrics:
    """ """

    id: Union[Unset, str] = UNSET
    aliases: Union[Unset, List[Alias]] = UNSET
    available_processors: Union[Unset, int] = UNSET
    memory: Union[Unset, Memory] = UNSET
    database: Union[Unset, Database] = UNSET
    server_start_time: Union[Unset, int] = UNSET
    logs_folder: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()

                aliases.append(aliases_item)

        available_processors = self.available_processors
        memory: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.memory, Unset):
            memory = self.memory.to_dict()

        database: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.database, Unset):
            database = self.database.to_dict()

        server_start_time = self.server_start_time
        logs_folder = self.logs_folder

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if available_processors is not UNSET:
            field_dict["availableProcessors"] = available_processors
        if memory is not UNSET:
            field_dict["memory"] = memory
        if database is not UNSET:
            field_dict["database"] = database
        if server_start_time is not UNSET:
            field_dict["serverStartTime"] = server_start_time
        if logs_folder is not UNSET:
            field_dict["logsFolder"] = logs_folder

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        available_processors = d.pop("availableProcessors", UNSET)

        _memory = d.pop("memory", UNSET)
        memory: Union[Unset, Memory]
        if isinstance(_memory, Unset):
            memory = UNSET
        else:
            memory = Memory.from_dict(_memory)

        _database = d.pop("database", UNSET)
        database: Union[Unset, Database]
        if isinstance(_database, Unset):
            database = UNSET
        else:
            database = Database.from_dict(_database)

        server_start_time = d.pop("serverStartTime", UNSET)

        logs_folder = d.pop("logsFolder", UNSET)

        metrics = cls(
            id=id,
            aliases=aliases,
            available_processors=available_processors,
            memory=memory,
            database=database,
            server_start_time=server_start_time,
            logs_folder=logs_folder,
        )

        metrics.additional_properties = d
        return metrics

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
