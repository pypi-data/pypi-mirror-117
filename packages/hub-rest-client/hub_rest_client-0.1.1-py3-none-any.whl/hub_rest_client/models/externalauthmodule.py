from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_module_custom_attribute_mapping import AuthModuleCustomAttributeMapping
    from ..models.auth_module_group_mapping import AuthModuleGroupMapping
else:
    AuthModuleCustomAttributeMapping = "AuthModuleCustomAttributeMapping"
    AuthModuleGroupMapping = "AuthModuleGroupMapping"

from ..models.user_creation_auth_module import UserCreationAuthModule

T = TypeVar("T", bound="Externalauthmodule")


@attr.s(auto_attribs=True)
class Externalauthmodule(UserCreationAuthModule):
    """ """

    server_url: Union[Unset, str] = UNSET
    connection_timeout: Union[Unset, int] = UNSET
    read_timeout: Union[Unset, int] = UNSET
    group_mappings: Union[Unset, List[AuthModuleGroupMapping]] = UNSET
    attribute_mappings: Union[Unset, List[AuthModuleCustomAttributeMapping]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_url = self.server_url
        connection_timeout = self.connection_timeout
        read_timeout = self.read_timeout
        group_mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.group_mappings, Unset):
            group_mappings = []
            for group_mappings_item_data in self.group_mappings:
                group_mappings_item = group_mappings_item_data.to_dict()

                group_mappings.append(group_mappings_item)

        attribute_mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_mappings, Unset):
            attribute_mappings = []
            for attribute_mappings_item_data in self.attribute_mappings:
                attribute_mappings_item = attribute_mappings_item_data.to_dict()

                attribute_mappings.append(attribute_mappings_item)

        field_dict: Dict[str, Any] = {}
        _UserCreationAuthModule_dict = super(UserCreationAuthModule).to_dict()
        field_dict.update(_UserCreationAuthModule_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server_url is not UNSET:
            field_dict["serverUrl"] = server_url
        if connection_timeout is not UNSET:
            field_dict["connectionTimeout"] = connection_timeout
        if read_timeout is not UNSET:
            field_dict["readTimeout"] = read_timeout
        if group_mappings is not UNSET:
            field_dict["groupMappings"] = group_mappings
        if attribute_mappings is not UNSET:
            field_dict["attributeMappings"] = attribute_mappings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _UserCreationAuthModule_kwargs = super(UserCreationAuthModule).from_dict(src_dict=d).to_dict()

        server_url = d.pop("serverUrl", UNSET)

        connection_timeout = d.pop("connectionTimeout", UNSET)

        read_timeout = d.pop("readTimeout", UNSET)

        group_mappings = []
        _group_mappings = d.pop("groupMappings", UNSET)
        for group_mappings_item_data in _group_mappings or []:
            group_mappings_item = AuthModuleGroupMapping.from_dict(group_mappings_item_data)

            group_mappings.append(group_mappings_item)

        attribute_mappings = []
        _attribute_mappings = d.pop("attributeMappings", UNSET)
        for attribute_mappings_item_data in _attribute_mappings or []:
            attribute_mappings_item = AuthModuleCustomAttributeMapping.from_dict(attribute_mappings_item_data)

            attribute_mappings.append(attribute_mappings_item)

        externalauthmodule = cls(
            server_url=server_url,
            connection_timeout=connection_timeout,
            read_timeout=read_timeout,
            group_mappings=group_mappings,
            attribute_mappings=attribute_mappings,
            **_UserCreationAuthModule_kwargs,
        )

        externalauthmodule.additional_properties = d
        return externalauthmodule

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
