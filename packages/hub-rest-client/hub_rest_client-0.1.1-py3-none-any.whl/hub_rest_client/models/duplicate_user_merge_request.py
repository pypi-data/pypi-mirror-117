from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duplicate_user_cluster import DuplicateUserCluster
else:
    DuplicateUserCluster = "DuplicateUserCluster"


T = TypeVar("T", bound="DuplicateUserMergeRequest")


@attr.s(auto_attribs=True)
class DuplicateUserMergeRequest:
    """ """

    all_: Union[Unset, bool] = UNSET
    clusters: Union[Unset, List[DuplicateUserCluster]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        all_ = self.all_
        clusters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.clusters, Unset):
            clusters = []
            for clusters_item_data in self.clusters:
                clusters_item = clusters_item_data.to_dict()

                clusters.append(clusters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if clusters is not UNSET:
            field_dict["clusters"] = clusters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        all_ = d.pop("all", UNSET)

        clusters = []
        _clusters = d.pop("clusters", UNSET)
        for clusters_item_data in _clusters or []:
            clusters_item = DuplicateUserCluster.from_dict(clusters_item_data)

            clusters.append(clusters_item)

        duplicate_user_merge_request = cls(
            all_=all_,
            clusters=clusters,
        )

        duplicate_user_merge_request.additional_properties = d
        return duplicate_user_merge_request

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
