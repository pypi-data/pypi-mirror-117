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

        d = src_dict.copy()

        _ActivityItem_kwargs = super().from_dict(src_dict=d).to_dict()
        _ActivityItem_kwargs.pop("$type")

        single_value_activity_item = cls(
            **_ActivityItem_kwargs,
        )

        return single_value_activity_item
