from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupError")


@attr.s(auto_attribs=True)
class BackupError:
    """Represents an error that appeared during the backup."""

    date: Union[Unset, int] = UNSET
    error_message: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date
        error_message = self.error_message
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        date = d.pop("date", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        backup_error = cls(
            date=date,
            error_message=error_message,
            id=id,
            type=type,
        )

        backup_error.additional_properties = d
        return backup_error

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
