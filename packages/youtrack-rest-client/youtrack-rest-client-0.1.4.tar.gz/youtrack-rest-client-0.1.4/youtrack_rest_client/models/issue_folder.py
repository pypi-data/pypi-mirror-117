from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueFolder")


@attr.s(auto_attribs=True)
class IssueFolder:
    """Represents an issue folder, such as a project, a saved search, or a tag."""

    name: "Union[Unset, str]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        issue_folder = cls(
            name=name,
            id=id,
            type=type,
        )

        return issue_folder
