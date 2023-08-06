from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Database")


@attr.s(auto_attribs=True)
class Database:
    """ """

    location: Union[Unset, str] = UNSET
    data_size: Union[Unset, int] = UNSET
    text_index_size: Union[Unset, int] = UNSET
    blobs_size: Union[Unset, int] = UNSET
    background_threads_count: Union[Unset, int] = UNSET
    pending_jobs_count: Union[Unset, int] = UNSET
    entity_iterable_cache_size: Union[Unset, int] = UNSET
    entity_iterable_cache_hit_rate: Union[Unset, float] = UNSET
    transactions_count: Union[Unset, int] = UNSET
    transactions_per_second: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location = self.location
        data_size = self.data_size
        text_index_size = self.text_index_size
        blobs_size = self.blobs_size
        background_threads_count = self.background_threads_count
        pending_jobs_count = self.pending_jobs_count
        entity_iterable_cache_size = self.entity_iterable_cache_size
        entity_iterable_cache_hit_rate = self.entity_iterable_cache_hit_rate
        transactions_count = self.transactions_count
        transactions_per_second = self.transactions_per_second

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if data_size is not UNSET:
            field_dict["dataSize"] = data_size
        if text_index_size is not UNSET:
            field_dict["textIndexSize"] = text_index_size
        if blobs_size is not UNSET:
            field_dict["blobsSize"] = blobs_size
        if background_threads_count is not UNSET:
            field_dict["backgroundThreadsCount"] = background_threads_count
        if pending_jobs_count is not UNSET:
            field_dict["pendingJobsCount"] = pending_jobs_count
        if entity_iterable_cache_size is not UNSET:
            field_dict["entityIterableCacheSize"] = entity_iterable_cache_size
        if entity_iterable_cache_hit_rate is not UNSET:
            field_dict["entityIterableCacheHitRate"] = entity_iterable_cache_hit_rate
        if transactions_count is not UNSET:
            field_dict["transactionsCount"] = transactions_count
        if transactions_per_second is not UNSET:
            field_dict["transactionsPerSecond"] = transactions_per_second

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        location = d.pop("location", UNSET)

        data_size = d.pop("dataSize", UNSET)

        text_index_size = d.pop("textIndexSize", UNSET)

        blobs_size = d.pop("blobsSize", UNSET)

        background_threads_count = d.pop("backgroundThreadsCount", UNSET)

        pending_jobs_count = d.pop("pendingJobsCount", UNSET)

        entity_iterable_cache_size = d.pop("entityIterableCacheSize", UNSET)

        entity_iterable_cache_hit_rate = d.pop("entityIterableCacheHitRate", UNSET)

        transactions_count = d.pop("transactionsCount", UNSET)

        transactions_per_second = d.pop("transactionsPerSecond", UNSET)

        database = cls(
            location=location,
            data_size=data_size,
            text_index_size=text_index_size,
            blobs_size=blobs_size,
            background_threads_count=background_threads_count,
            pending_jobs_count=pending_jobs_count,
            entity_iterable_cache_size=entity_iterable_cache_size,
            entity_iterable_cache_hit_rate=entity_iterable_cache_hit_rate,
            transactions_count=transactions_count,
            transactions_per_second=transactions_per_second,
        )

        database.additional_properties = d
        return database

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
