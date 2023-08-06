from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicesPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class ServicesPage(base_page.BasePage):
    """ """

    services: "Union[Unset, List[service_m.Service]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        services: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()

                services.append(services_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if services is not UNSET:
            field_dict["services"] = services

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import service as service_m
        except ImportError:
            import sys

            service_m = sys.modules[__package__ + "service"]

        d = src_dict.copy()

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = service_m.Service.from_dict(services_item_data)

            services.append(services_item)

        services_page = cls(
            services=services,
        )

        return services_page
