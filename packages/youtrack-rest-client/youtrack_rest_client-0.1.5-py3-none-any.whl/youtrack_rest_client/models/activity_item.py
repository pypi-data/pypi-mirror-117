from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityItem")


@attr.s(auto_attribs=True)
class ActivityItem:
    """Represents a change in an issue or in its related entities. In the UI, you see these changes as
    the Activity stream. It shows a feed of all updates of the issue: issue history, comments, attachments,
    VCS changes, work items, and so on."""

    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        activity_item = cls(
            id=id,
            type=type,
        )

        return activity_item
