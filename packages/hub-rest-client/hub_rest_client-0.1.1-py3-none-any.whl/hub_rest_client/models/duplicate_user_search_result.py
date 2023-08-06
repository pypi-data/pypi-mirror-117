from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duplicate_search_progress import DuplicateSearchProgress
    from ..models.duplicate_user_cluster import DuplicateUserCluster
else:
    DuplicateUserCluster = "DuplicateUserCluster"
    DuplicateSearchProgress = "DuplicateSearchProgress"


T = TypeVar("T", bound="DuplicateUserSearchResult")


@attr.s(auto_attribs=True)
class DuplicateUserSearchResult:
    """ """

    id: Union[Unset, str] = UNSET
    progress: Union[Unset, DuplicateSearchProgress] = UNSET
    cluster_count: Union[Unset, int] = UNSET
    clusters: Union[Unset, List[DuplicateUserCluster]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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
        d = src_dict.copy()

        id = d.pop("id", UNSET)

        _progress = d.pop("progress", UNSET)
        progress: Union[Unset, DuplicateSearchProgress]
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = DuplicateSearchProgress.from_dict(_progress)

        cluster_count = d.pop("clusterCount", UNSET)

        clusters = []
        _clusters = d.pop("clusters", UNSET)
        for clusters_item_data in _clusters or []:
            clusters_item = DuplicateUserCluster.from_dict(clusters_item_data)

            clusters.append(clusters_item)

        duplicate_user_search_result = cls(
            id=id,
            progress=progress,
            cluster_count=cluster_count,
            clusters=clusters,
        )

        duplicate_user_search_result.additional_properties = d
        return duplicate_user_search_result

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
