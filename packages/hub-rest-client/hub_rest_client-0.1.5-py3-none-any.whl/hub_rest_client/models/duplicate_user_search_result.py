from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateUserSearchResult")


@attr.s(auto_attribs=True)
class DuplicateUserSearchResult:
    """ """

    id: "Union[Unset, str]" = UNSET
    progress: "Union[Unset, duplicate_search_progress_m.DuplicateSearchProgress]" = UNSET
    cluster_count: "Union[Unset, int]" = UNSET
    clusters: "Union[Unset, List[duplicate_user_cluster_m.DuplicateUserCluster]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        progress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        cluster_count = self.cluster_count
        clusters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.clusters, Unset):
            clusters = []
            for clusters_item_data in self.clusters:
                clusters_item = clusters_item_data.to_dict()

                clusters.append(clusters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if progress is not UNSET:
            field_dict["progress"] = progress
        if cluster_count is not UNSET:
            field_dict["clusterCount"] = cluster_count
        if clusters is not UNSET:
            field_dict["clusters"] = clusters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import duplicate_search_progress as duplicate_search_progress_m
            from ..models import duplicate_user_cluster as duplicate_user_cluster_m
        except ImportError:
            import sys

            duplicate_user_cluster_m = sys.modules[__package__ + "duplicate_user_cluster"]
            duplicate_search_progress_m = sys.modules[__package__ + "duplicate_search_progress"]

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        _progress = d.pop("progress", UNSET)
        progress: Union[Unset, duplicate_search_progress_m.DuplicateSearchProgress]
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = duplicate_search_progress_m.DuplicateSearchProgress.from_dict(_progress)

        cluster_count = d.pop("clusterCount", UNSET)

        clusters = []
        _clusters = d.pop("clusters", UNSET)
        for clusters_item_data in _clusters or []:
            clusters_item = duplicate_user_cluster_m.DuplicateUserCluster.from_dict(clusters_item_data)

            clusters.append(clusters_item)

        duplicate_user_search_result = cls(
            id=id,
            progress=progress,
            cluster_count=cluster_count,
            clusters=clusters,
        )

        return duplicate_user_search_result
