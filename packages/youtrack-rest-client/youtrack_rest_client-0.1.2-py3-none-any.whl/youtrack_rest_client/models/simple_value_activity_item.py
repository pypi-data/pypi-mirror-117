from typing import Any, Dict, List, Type, TypeVar, Union

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
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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

            simple_value_activity_item_removed_m = sys.modules[__package__ + "simple_value_activity_item_removed"]
            simple_value_activity_item_added_m = sys.modules[__package__ + "simple_value_activity_item_added"]

        d = src_dict.copy()

        _SingleValueActivityItem_kwargs = super().from_dict(src_dict=d).to_dict()

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
            **_SingleValueActivityItem_kwargs,
        )

        simple_value_activity_item.additional_properties = d
        return simple_value_activity_item

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
