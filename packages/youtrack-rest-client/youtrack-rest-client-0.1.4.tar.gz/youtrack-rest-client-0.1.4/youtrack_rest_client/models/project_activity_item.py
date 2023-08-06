from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectActivityItem")


try:
    from ..models import single_value_activity_item
except ImportError:
    import sys

    single_value_activity_item = sys.modules[__package__ + "single_value_activity_item"]


@attr.s(auto_attribs=True)
class ProjectActivityItem(single_value_activity_item.SingleValueActivityItem):
    """Represents the change in the project attribute on an Issue."""

    target: "Union[Unset, issue_m.Issue]" = UNSET
    removed: "Union[Unset, project_activity_item_removed_m.ProjectActivityItemRemoved]" = UNSET
    added: "Union[Unset, project_activity_item_added_m.ProjectActivityItemAdded]" = UNSET

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
            from ..models import issue as issue_m
            from ..models import project_activity_item_added as project_activity_item_added_m
            from ..models import project_activity_item_removed as project_activity_item_removed_m
        except ImportError:
            import sys

            issue_m = sys.modules[__package__ + "issue"]
            project_activity_item_added_m = sys.modules[__package__ + "project_activity_item_added"]
            project_activity_item_removed_m = sys.modules[__package__ + "project_activity_item_removed"]

        d = src_dict.copy()

        _target = d.pop("target", UNSET)
        target: Union[Unset, issue_m.Issue]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = issue_m.Issue.from_dict(_target)

        _removed = d.pop("removed", UNSET)
        removed: Union[Unset, project_activity_item_removed_m.ProjectActivityItemRemoved]
        if isinstance(_removed, Unset):
            removed = UNSET
        else:
            removed = project_activity_item_removed_m.ProjectActivityItemRemoved.from_dict(_removed)

        _added = d.pop("added", UNSET)
        added: Union[Unset, project_activity_item_added_m.ProjectActivityItemAdded]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = project_activity_item_added_m.ProjectActivityItemAdded.from_dict(_added)

        project_activity_item = cls(
            target=target,
            removed=removed,
            added=added,
        )

        return project_activity_item
