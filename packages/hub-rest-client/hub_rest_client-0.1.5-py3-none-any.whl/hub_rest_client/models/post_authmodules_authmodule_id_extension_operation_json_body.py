from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PostAuthmodulesAuthmoduleIdExtensionOperationJsonBody")


@attr.s(auto_attribs=True)
class PostAuthmodulesAuthmoduleIdExtensionOperationJsonBody:
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        post_authmodules_authmodule_id_extension_operation_json_body = cls()

        return post_authmodules_authmodule_id_extension_operation_json_body
