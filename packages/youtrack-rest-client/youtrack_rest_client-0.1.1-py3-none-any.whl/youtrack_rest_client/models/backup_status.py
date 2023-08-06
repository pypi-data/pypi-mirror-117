from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_error import BackupError
else:
    BackupError = "BackupError"


T = TypeVar("T", bound="BackupStatus")


@attr.s(auto_attribs=True)
class BackupStatus:
    """Represents the current status of the backup process."""

    backup_in_progress: Union[Unset, bool] = UNSET
    backup_cancelled: Union[Unset, bool] = UNSET
    backup_error: Union[Unset, BackupError] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        backup_in_progress = self.backup_in_progress
        backup_cancelled = self.backup_cancelled
        backup_error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.backup_error, Unset):
            backup_error = self.backup_error.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_in_progress is not UNSET:
            field_dict["backupInProgress"] = backup_in_progress
        if backup_cancelled is not UNSET:
            field_dict["backupCancelled"] = backup_cancelled
        if backup_error is not UNSET:
            field_dict["backupError"] = backup_error
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        backup_in_progress = d.pop("backupInProgress", UNSET)

        backup_cancelled = d.pop("backupCancelled", UNSET)

        _backup_error = d.pop("backupError", UNSET)
        backup_error: Union[Unset, BackupError]
        if isinstance(_backup_error, Unset):
            backup_error = UNSET
        else:
            backup_error = BackupError.from_dict(_backup_error)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        backup_status = cls(
            backup_in_progress=backup_in_progress,
            backup_cancelled=backup_cancelled,
            backup_error=backup_error,
            id=id,
            type=type,
        )

        backup_status.additional_properties = d
        return backup_status

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
