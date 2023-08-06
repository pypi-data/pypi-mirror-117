from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_status import BackupStatus
    from ..models.database_backup_settings_archive_format import DatabaseBackupSettingsArchiveFormat
    from ..models.user import User
else:
    BackupStatus = "BackupStatus"
    DatabaseBackupSettingsArchiveFormat = "DatabaseBackupSettingsArchiveFormat"
    User = "User"


T = TypeVar("T", bound="DatabaseBackupSettings")


@attr.s(auto_attribs=True)
class DatabaseBackupSettings:
    """Represents database backup settings of the YouTrack instance."""

    location: Union[Unset, str] = UNSET
    files_to_keep: Union[Unset, int] = UNSET
    cron_expression: Union[Unset, str] = UNSET
    archive_format: Union[Unset, DatabaseBackupSettingsArchiveFormat] = UNSET
    is_on: Union[Unset, bool] = UNSET
    available_disk_space: Union[Unset, int] = UNSET
    notified_users: Union[Unset, List[User]] = UNSET
    backup_status: Union[Unset, BackupStatus] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location = self.location
        files_to_keep = self.files_to_keep
        cron_expression = self.cron_expression
        archive_format: Union[Unset, str] = UNSET
        if not isinstance(self.archive_format, Unset):
            archive_format = self.archive_format.value

        is_on = self.is_on
        available_disk_space = self.available_disk_space
        notified_users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notified_users, Unset):
            notified_users = []
            for notified_users_item_data in self.notified_users:
                notified_users_item = notified_users_item_data.to_dict()

                notified_users.append(notified_users_item)

        backup_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.backup_status, Unset):
            backup_status = self.backup_status.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if files_to_keep is not UNSET:
            field_dict["filesToKeep"] = files_to_keep
        if cron_expression is not UNSET:
            field_dict["cronExpression"] = cron_expression
        if archive_format is not UNSET:
            field_dict["archiveFormat"] = archive_format
        if is_on is not UNSET:
            field_dict["isOn"] = is_on
        if available_disk_space is not UNSET:
            field_dict["availableDiskSpace"] = available_disk_space
        if notified_users is not UNSET:
            field_dict["notifiedUsers"] = notified_users
        if backup_status is not UNSET:
            field_dict["backupStatus"] = backup_status
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        location = d.pop("location", UNSET)

        files_to_keep = d.pop("filesToKeep", UNSET)

        cron_expression = d.pop("cronExpression", UNSET)

        _archive_format = d.pop("archiveFormat", UNSET)
        archive_format: Union[Unset, DatabaseBackupSettingsArchiveFormat]
        if isinstance(_archive_format, Unset):
            archive_format = UNSET
        else:
            archive_format = DatabaseBackupSettingsArchiveFormat(_archive_format)

        is_on = d.pop("isOn", UNSET)

        available_disk_space = d.pop("availableDiskSpace", UNSET)

        notified_users = []
        _notified_users = d.pop("notifiedUsers", UNSET)
        for notified_users_item_data in _notified_users or []:
            notified_users_item = User.from_dict(notified_users_item_data)

            notified_users.append(notified_users_item)

        _backup_status = d.pop("backupStatus", UNSET)
        backup_status: Union[Unset, BackupStatus]
        if isinstance(_backup_status, Unset):
            backup_status = UNSET
        else:
            backup_status = BackupStatus.from_dict(_backup_status)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        database_backup_settings = cls(
            location=location,
            files_to_keep=files_to_keep,
            cron_expression=cron_expression,
            archive_format=archive_format,
            is_on=is_on,
            available_disk_space=available_disk_space,
            notified_users=notified_users,
            backup_status=backup_status,
            id=id,
            type=type,
        )

        database_backup_settings.additional_properties = d
        return database_backup_settings

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
