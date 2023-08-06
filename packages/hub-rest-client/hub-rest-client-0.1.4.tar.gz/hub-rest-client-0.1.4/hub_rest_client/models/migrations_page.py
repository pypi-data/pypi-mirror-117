from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MigrationsPage")


try:
    from ..models import base_page
except ImportError:
    import sys

    base_page = sys.modules[__package__ + "base_page"]


@attr.s(auto_attribs=True)
class MigrationsPage(base_page.BasePage):
    """ """

    migrations: "Union[Unset, List[migrations_m.Migrations]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        migrations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.migrations, Unset):
            migrations = []
            for migrations_item_data in self.migrations:
                migrations_item = migrations_item_data.to_dict()

                migrations.append(migrations_item)

        field_dict: Dict[str, Any] = {}
        _BasePage_dict = super().to_dict()
        field_dict.update(_BasePage_dict)
        field_dict.update({})
        if migrations is not UNSET:
            field_dict["migrations"] = migrations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import migrations as migrations_m
        except ImportError:
            import sys

            migrations_m = sys.modules[__package__ + "migrations"]

        d = src_dict.copy()

        migrations = []
        _migrations = d.pop("migrations", UNSET)
        for migrations_item_data in _migrations or []:
            migrations_item = migrations_m.Migrations.from_dict(migrations_item_data)

            migrations.append(migrations_item)

        migrations_page = cls(
            migrations=migrations,
        )

        return migrations_page
