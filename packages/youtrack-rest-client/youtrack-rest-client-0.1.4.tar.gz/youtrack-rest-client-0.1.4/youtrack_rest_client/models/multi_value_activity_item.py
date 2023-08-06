from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="MultiValueActivityItem")


try:
    from ..models import activity_item
except ImportError:
    import sys

    activity_item = sys.modules[__package__ + "activity_item"]


@attr.s(auto_attribs=True)
class MultiValueActivityItem(activity_item.ActivityItem):
    """Represents a change in an entity attribute that has type of `Array of &lt;Entities&gt;`."""

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _ActivityItem_dict = super().to_dict()
        field_dict.update(_ActivityItem_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        multi_value_activity_item = cls()

        return multi_value_activity_item
