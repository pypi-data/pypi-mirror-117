from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldActivityItem")


try:
    from ..models import activity_item
except ImportError:
    import sys

    activity_item = sys.modules[__package__ + "activity_item"]


@attr.s(auto_attribs=True)
class CustomFieldActivityItem(activity_item.ActivityItem):
    """Represents an activity that affects a custom field of an issue."""

    target: "Union[Unset, issue_m.Issue]" = UNSET
    removed: "Union[Unset, custom_field_activity_item_removed_m.CustomFieldActivityItemRemoved]" = UNSET
    added: "Union[Unset, custom_field_activity_item_added_m.CustomFieldActivityItemAdded]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        removed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.removed, Unset):
            removed = self.removed.to_dict()

        added: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.to_dict()

        field_dict: Dict[str, Any] = {}
        _ActivityItem_dict = super().to_dict()
        field_dict.update(_ActivityItem_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target is not UNSET:
            field_dict["target"] = target
        if removed is not UNSET:
            field_dict["removed"] = removed
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import custom_field_activity_item_added as custom_field_activity_item_added_m
            from ..models import custom_field_activity_item_removed as custom_field_activity_item_removed_m
            from ..models import issue as issue_m
        except ImportError:
            import sys

            issue_m = sys.modules[__package__ + "issue"]
            custom_field_activity_item_removed_m = sys.modules[__package__ + "custom_field_activity_item_removed"]
            custom_field_activity_item_added_m = sys.modules[__package__ + "custom_field_activity_item_added"]

        d = src_dict.copy()

        _target = d.pop("target", UNSET)
        target: Union[Unset, issue_m.Issue]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = issue_m.Issue.from_dict(_target)

        _removed = d.pop("removed", UNSET)
        removed: Union[Unset, custom_field_activity_item_removed_m.CustomFieldActivityItemRemoved]
        if isinstance(_removed, Unset):
            removed = UNSET
        else:
            removed = custom_field_activity_item_removed_m.CustomFieldActivityItemRemoved.from_dict(_removed)

        _added = d.pop("added", UNSET)
        added: Union[Unset, custom_field_activity_item_added_m.CustomFieldActivityItemAdded]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = custom_field_activity_item_added_m.CustomFieldActivityItemAdded.from_dict(_added)

        custom_field_activity_item = cls(
            target=target,
            removed=removed,
            added=added,
        )

        custom_field_activity_item.additional_properties = d
        return custom_field_activity_item

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
