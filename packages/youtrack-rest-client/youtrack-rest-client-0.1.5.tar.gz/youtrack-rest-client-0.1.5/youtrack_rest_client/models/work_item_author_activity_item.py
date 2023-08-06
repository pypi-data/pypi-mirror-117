from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkItemAuthorActivityItem")


try:
    from ..models import single_value_activity_item
except ImportError:
    import sys

    single_value_activity_item = sys.modules[__package__ + "single_value_activity_item"]


@attr.s(auto_attribs=True)
class WorkItemAuthorActivityItem(single_value_activity_item.SingleValueActivityItem):
    """Represents a change in the `author` attribute of a work item."""

    target: "Union[Unset, issue_work_item_m.IssueWorkItem]" = UNSET
    removed: "Union[Unset, user_m.User]" = UNSET
    added: "Union[Unset, user_m.User]" = UNSET

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
        _SingleValueActivityItem_dict = super().to_dict()
        field_dict.update(_SingleValueActivityItem_dict)
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
            from ..models import issue_work_item as issue_work_item_m
            from ..models import user as user_m
        except ImportError:
            import sys

            user_m = sys.modules[__package__ + "user"]
            issue_work_item_m = sys.modules[__package__ + "issue_work_item"]

        d = src_dict.copy()

        _SingleValueActivityItem_kwargs = super().from_dict(src_dict=d).to_dict()
        _SingleValueActivityItem_kwargs.pop("$type")

        _target = d.pop("target", UNSET)
        target: Union[Unset, issue_work_item_m.IssueWorkItem]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = issue_work_item_m.IssueWorkItem.from_dict(_target)

        _removed = d.pop("removed", UNSET)
        removed: Union[Unset, user_m.User]
        if isinstance(_removed, Unset):
            removed = UNSET
        else:
            removed = user_m.User.from_dict(_removed)

        _added = d.pop("added", UNSET)
        added: Union[Unset, user_m.User]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = user_m.User.from_dict(_added)

        work_item_author_activity_item = cls(
            target=target,
            removed=removed,
            added=added,
            **_SingleValueActivityItem_kwargs,
        )

        return work_item_author_activity_item
