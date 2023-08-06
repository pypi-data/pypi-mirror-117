from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Metrics")


@attr.s(auto_attribs=True)
class Metrics:
    """ """

    id: "Union[Unset, str]" = UNSET
    aliases: "Union[Unset, List[alias_m.Alias]]" = UNSET
    available_processors: "Union[Unset, int]" = UNSET
    memory: "Union[Unset, memory_m.Memory]" = UNSET
    database: "Union[Unset, database_m.Database]" = UNSET
    server_start_time: "Union[Unset, int]" = UNSET
    logs_folder: "Union[Unset, str]" = UNSET

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

        try:
            from ..models import alias as alias_m
            from ..models import database as database_m
            from ..models import memory as memory_m
        except ImportError:
            import sys

            database_m = sys.modules[__package__ + "database"]
            alias_m = sys.modules[__package__ + "alias"]
            memory_m = sys.modules[__package__ + "memory"]

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = alias_m.Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        available_processors = d.pop("availableProcessors", UNSET)

        _memory = d.pop("memory", UNSET)
        memory: Union[Unset, memory_m.Memory]
        if isinstance(_memory, Unset):
            memory = UNSET
        else:
            memory = memory_m.Memory.from_dict(_memory)

        _database = d.pop("database", UNSET)
        database: Union[Unset, database_m.Database]
        if isinstance(_database, Unset):
            database = UNSET
        else:
            database = database_m.Database.from_dict(_database)

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

        return metrics
