from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="CreatedDeletedActivityItem")


try:
    from ..models import activity_item
except ImportError:
    import sys

    activity_item = sys.modules[__package__ + "activity_item"]


@attr.s(auto_attribs=True)
class CreatedDeletedActivityItem(activity_item.ActivityItem):
    """Represents an action when an entity is created or deleted in an issue. For example, a new comment is created in the issue."""

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _ActivityItem_dict = super().to_dict()
        field_dict.update(_ActivityItem_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        created_deleted_activity_item = cls()

        return created_deleted_activity_item
