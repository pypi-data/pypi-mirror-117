from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class MetricsPage(base_page.BasePage):
    """ """

    metrics: "Union[Unset, List[metrics_m.Metrics]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        metrics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()

                metrics.append(metrics_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import metrics as metrics_m
        except ImportError:
            import sys

            metrics_m = sys.modules[__package__ + "metrics"]

        d = src_dict.copy()

        _BasePage_kwargs = super().from_dict(src_dict=d).to_dict()
        _BasePage_kwargs.pop("$type")

        metrics = []
        _metrics = d.pop("metrics", UNSET)
        for metrics_item_data in _metrics or []:
            metrics_item = metrics_m.Metrics.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        metrics_page = cls(
            metrics=metrics,
            **_BasePage_kwargs,
        )

        return metrics_page
