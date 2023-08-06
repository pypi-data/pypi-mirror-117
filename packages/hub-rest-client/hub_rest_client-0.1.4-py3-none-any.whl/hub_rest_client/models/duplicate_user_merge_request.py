from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateUserMergeRequest")


@attr.s(auto_attribs=True)
class DuplicateUserMergeRequest:
    """ """

    all_: "Union[Unset, bool]" = UNSET
    clusters: "Union[Unset, List[duplicate_user_cluster_m.DuplicateUserCluster]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        all_ = self.all_
        clusters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.clusters, Unset):
            clusters = []
            for clusters_item_data in self.clusters:
                clusters_item = clusters_item_data.to_dict()

                clusters.append(clusters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if clusters is not UNSET:
            field_dict["clusters"] = clusters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import duplicate_user_cluster as duplicate_user_cluster_m
        except ImportError:
            import sys

            duplicate_user_cluster_m = sys.modules[__package__ + "duplicate_user_cluster"]

        d = src_dict.copy()

        all_ = d.pop("all", UNSET)

        clusters = []
        _clusters = d.pop("clusters", UNSET)
        for clusters_item_data in _clusters or []:
            clusters_item = duplicate_user_cluster_m.DuplicateUserCluster.from_dict(clusters_item_data)

            clusters.append(clusters_item)

        duplicate_user_merge_request = cls(
            all_=all_,
            clusters=clusters,
        )

        return duplicate_user_merge_request
