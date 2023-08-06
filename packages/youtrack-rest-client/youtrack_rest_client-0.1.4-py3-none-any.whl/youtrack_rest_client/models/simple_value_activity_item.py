from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SimpleValueActivityItem")


try:
    from ..models import single_value_activity_item
except ImportError:
    import sys

    single_value_activity_item = sys.modules[__package__ + "single_value_activity_item"]


@attr.s(auto_attribs=True)
class SimpleValueActivityItem(single_value_activity_item.SingleValueActivityItem):
    """Represents the change in attributes of a simple type in the target entity:
    Issue, IssueComment, WorkItem, IssueAttachment."""

    removed: "Union[Unset, simple_value_activity_item_removed_m.SimpleValueActivityItemRemoved]" = UNSET
    added: "Union[Unset, simple_value_activity_item_added_m.SimpleValueActivityItemAdded]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        removed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.removed, Unset):
            removed = self.removed.to_dict()

        added: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.to_dict()

        field_dict: Dict[str, Any] = {}
        _SingleValueActivityItem_dict = super().to_dict()
        field_dict.update(_SingleValueActivityItem_dict)
        field_dict.update({})
        if removed is not UNSET:
            field_dict["removed"] = removed
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import simple_value_activity_item_added as simple_value_activity_item_added_m
            from ..models import simple_value_activity_item_removed as simple_value_activity_item_removed_m
        except ImportError:
            import sys

            simple_value_activity_item_added_m = sys.modules[__package__ + "simple_value_activity_item_added"]
            simple_value_activity_item_removed_m = sys.modules[__package__ + "simple_value_activity_item_removed"]

        d = src_dict.copy()

        _removed = d.pop("removed", UNSET)
        removed: Union[Unset, simple_value_activity_item_removed_m.SimpleValueActivityItemRemoved]
        if isinstance(_removed, Unset):
            removed = UNSET
        else:
            removed = simple_value_activity_item_removed_m.SimpleValueActivityItemRemoved.from_dict(_removed)

        _added = d.pop("added", UNSET)
        added: Union[Unset, simple_value_activity_item_added_m.SimpleValueActivityItemAdded]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = simple_value_activity_item_added_m.SimpleValueActivityItemAdded.from_dict(_added)

        simple_value_activity_item = cls(
            removed=removed,
            added=added,
        )

        return simple_value_activity_item
