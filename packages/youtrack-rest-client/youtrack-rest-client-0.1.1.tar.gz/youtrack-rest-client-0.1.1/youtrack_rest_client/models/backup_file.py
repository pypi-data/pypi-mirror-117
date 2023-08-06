from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupFile")


@attr.s(auto_attribs=True)
class BackupFile:
    """Represents the backup file."""

    name: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    creation_date: Union[Unset, int] = UNSET
    link: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        size = self.size
        creation_date = self.creation_date
        link = self.link
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if link is not UNSET:
            field_dict["link"] = link
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        creation_date = d.pop("creationDate", UNSET)

        link = d.pop("link", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        backup_file = cls(
            name=name,
            size=size,
            creation_date=creation_date,
            link=link,
            id=id,
            type=type,
        )

        backup_file.additional_properties = d
        return backup_file

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
