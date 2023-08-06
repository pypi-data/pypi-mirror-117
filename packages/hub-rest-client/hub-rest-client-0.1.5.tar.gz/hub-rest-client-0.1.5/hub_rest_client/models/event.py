from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Event")


@attr.s(auto_attribs=True)
class Event:
    """ """

    id: "Union[Unset, str]" = UNSET
    aliases: "Union[Unset, List[alias_m.Alias]]" = UNSET
    target_id: "Union[Unset, str]" = UNSET
    target_type: "Union[Unset, str]" = UNSET
    target_presentation: "Union[Unset, str]" = UNSET
    author: "Union[Unset, str]" = UNSET
    author_presentation: "Union[Unset, str]" = UNSET
    author_type: "Union[Unset, str]" = UNSET
    changes: "Union[Unset, List[change_m.Change]]" = UNSET
    type: "Union[Unset, str]" = UNSET
    timestamp: "Union[Unset, int]" = UNSET
    erase_timestamp: "Union[Unset, int]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()

                aliases.append(aliases_item)

        target_id = self.target_id
        target_type = self.target_type
        target_presentation = self.target_presentation
        author = self.author
        author_presentation = self.author_presentation
        author_type = self.author_type
        changes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.changes, Unset):
            changes = []
            for changes_item_data in self.changes:
                changes_item = changes_item_data.to_dict()

                changes.append(changes_item)

        type = self.type
        timestamp = self.timestamp
        erase_timestamp = self.erase_timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if target_presentation is not UNSET:
            field_dict["targetPresentation"] = target_presentation
        if author is not UNSET:
            field_dict["author"] = author
        if author_presentation is not UNSET:
            field_dict["authorPresentation"] = author_presentation
        if author_type is not UNSET:
            field_dict["authorType"] = author_type
        if changes is not UNSET:
            field_dict["changes"] = changes
        if type is not UNSET:
            field_dict["type"] = type
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if erase_timestamp is not UNSET:
            field_dict["eraseTimestamp"] = erase_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import alias as alias_m
            from ..models import change as change_m
        except ImportError:
            import sys

            alias_m = sys.modules[__package__ + "alias"]
            change_m = sys.modules[__package__ + "change"]

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = alias_m.Alias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        target_id = d.pop("targetId", UNSET)

        target_type = d.pop("targetType", UNSET)

        target_presentation = d.pop("targetPresentation", UNSET)

        author = d.pop("author", UNSET)

        author_presentation = d.pop("authorPresentation", UNSET)

        author_type = d.pop("authorType", UNSET)

        changes = []
        _changes = d.pop("changes", UNSET)
        for changes_item_data in _changes or []:
            changes_item = change_m.Change.from_dict(changes_item_data)

            changes.append(changes_item)

        type = d.pop("type", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        erase_timestamp = d.pop("eraseTimestamp", UNSET)

        event = cls(
            id=id,
            aliases=aliases,
            target_id=target_id,
            target_type=target_type,
            target_presentation=target_presentation,
            author=author,
            author_presentation=author_presentation,
            author_type=author_type,
            changes=changes,
            type=type,
            timestamp=timestamp,
            erase_timestamp=erase_timestamp,
        )

        return event
