from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="SingleValueActivityItem")


try:
    from ..models import activity_item
except ImportError:
    import sys

    activity_item = sys.modules[__package__ + "activity_item"]


@attr.s(auto_attribs=True)
class SingleValueActivityItem(activity_item.ActivityItem):
    """Describe change of properties that can have single value."""

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _ActivityItem_dict = super().to_dict()
        field_dict.update(_ActivityItem_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        single_value_activity_item = cls()

        return single_value_activity_item
