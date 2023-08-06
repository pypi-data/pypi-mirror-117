from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_status import BackupStatus
else:
    BackupStatus = "BackupStatus"

from ..models.settings import Settings

T = TypeVar("T", bound="BackupSettings")


@attr.s(auto_attribs=True)
class BackupSettings(Settings):
    """ """

    name_prefix: Union[Unset, str] = UNSET
    backup_folder: Union[Unset, str] = UNSET
    resolved_backup_folder: Union[Unset, str] = UNSET
    archive_type: Union[Unset, str] = UNSET
    status: Union[Unset, BackupStatus] = UNSET
    database_readonly: Union[Unset, bool] = UNSET
    cron_expression: Union[Unset, str] = UNSET
    count_to_keep: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name_prefix = self.name_prefix
        backup_folder = self.backup_folder
        resolved_backup_folder = self.resolved_backup_folder
        archive_type = self.archive_type
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        database_readonly = self.database_readonly
        cron_expression = self.cron_expression
        count_to_keep = self.count_to_keep

        field_dict: Dict[str, Any] = {}
        _Settings_dict = super(Settings).to_dict()
        field_dict.update(_Settings_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_prefix is not UNSET:
            field_dict["namePrefix"] = name_prefix
        if backup_folder is not UNSET:
            field_dict["backupFolder"] = backup_folder
        if resolved_backup_folder is not UNSET:
            field_dict["resolvedBackupFolder"] = resolved_backup_folder
        if archive_type is not UNSET:
            field_dict["archiveType"] = archive_type
        if status is not UNSET:
            field_dict["status"] = status
        if database_readonly is not UNSET:
            field_dict["databaseReadonly"] = database_readonly
        if cron_expression is not UNSET:
            field_dict["cronExpression"] = cron_expression
        if count_to_keep is not UNSET:
            field_dict["countToKeep"] = count_to_keep

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Settings_kwargs = super(Settings).from_dict(src_dict=d).to_dict()

        name_prefix = d.pop("namePrefix", UNSET)

        backup_folder = d.pop("backupFolder", UNSET)

        resolved_backup_folder = d.pop("resolvedBackupFolder", UNSET)

        archive_type = d.pop("archiveType", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupStatus.from_dict(_status)

        database_readonly = d.pop("databaseReadonly", UNSET)

        cron_expression = d.pop("cronExpression", UNSET)

        count_to_keep = d.pop("countToKeep", UNSET)

        backup_settings = cls(
            name_prefix=name_prefix,
            backup_folder=backup_folder,
            resolved_backup_folder=resolved_backup_folder,
            archive_type=archive_type,
            status=status,
            database_readonly=database_readonly,
            cron_expression=cron_expression,
            count_to_keep=count_to_keep,
            **_Settings_kwargs,
        )

        backup_settings.additional_properties = d
        return backup_settings

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
