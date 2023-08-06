from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Error")


@attr.s(auto_attribs=True)
class Error:
    """ """

    error: "Union[Unset, str]" = UNSET
    error_code: "Union[Unset, int]" = UNSET
    error_description: "Union[Unset, str]" = UNSET
    error_developer_message: "Union[Unset, str]" = UNSET
    error_uri: "Union[Unset, str]" = UNSET
    error_field: "Union[Unset, str]" = UNSET
    error_params: "Union[Unset, List[name_value_m.NameValue]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        error = self.error
        error_code = self.error_code
        error_description = self.error_description
        error_developer_message = self.error_developer_message
        error_uri = self.error_uri
        error_field = self.error_field
        error_params: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.error_params, Unset):
            error_params = []
            for error_params_item_data in self.error_params:
                error_params_item = error_params_item_data.to_dict()

                error_params.append(error_params_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if error_description is not UNSET:
            field_dict["error_description"] = error_description
        if error_developer_message is not UNSET:
            field_dict["error_developer_message"] = error_developer_message
        if error_uri is not UNSET:
            field_dict["error_uri"] = error_uri
        if error_field is not UNSET:
            field_dict["error_field"] = error_field
        if error_params is not UNSET:
            field_dict["error_params"] = error_params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import name_value as name_value_m
        except ImportError:
            import sys

            name_value_m = sys.modules[__package__ + "name_value"]

        d = src_dict.copy()

        error = d.pop("error", UNSET)

        error_code = d.pop("error_code", UNSET)

        error_description = d.pop("error_description", UNSET)

        error_developer_message = d.pop("error_developer_message", UNSET)

        error_uri = d.pop("error_uri", UNSET)

        error_field = d.pop("error_field", UNSET)

        error_params = []
        _error_params = d.pop("error_params", UNSET)
        for error_params_item_data in _error_params or []:
            error_params_item = name_value_m.NameValue.from_dict(error_params_item_data)

            error_params.append(error_params_item)

        error = cls(
            error=error,
            error_code=error_code,
            error_description=error_description,
            error_developer_message=error_developer_message,
            error_uri=error_uri,
            error_field=error_field,
            error_params=error_params,
        )

        return error
