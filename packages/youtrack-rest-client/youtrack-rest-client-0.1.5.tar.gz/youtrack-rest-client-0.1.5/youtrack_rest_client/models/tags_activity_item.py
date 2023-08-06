from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TagsActivityItem")


try:
    from ..models import multi_value_activity_item
except ImportError:
    import sys

    multi_value_activity_item = sys.modules[__package__ + "multi_value_activity_item"]


@attr.s(auto_attribs=True)
class TagsActivityItem(multi_value_activity_item.MultiValueActivityItem):
    """Represents a change in the list of tags of an issue."""

    target: "Union[Unset, issue_m.Issue]" = UNSET
    removed: "Union[Unset, List[issue_tag_m.IssueTag]]" = UNSET
    added: "Union[Unset, List[issue_tag_m.IssueTag]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        target: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        removed: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.removed, Unset):
            removed = []
            for removed_item_data in self.removed:
                removed_item = removed_item_data.to_dict()

                removed.append(removed_item)

        added: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.added, Unset):
            added = []
            for added_item_data in self.added:
                added_item = added_item_data.to_dict()

                added.append(added_item)

        field_dict: Dict[str, Any] = {}
        _MultiValueActivityItem_dict = super().to_dict()
        field_dict.update(_MultiValueActivityItem_dict)
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
            from ..models import issue_tag as issue_tag_m
        except ImportError:
            import sys

            issue_m = sys.modules[__package__ + "issue"]
            issue_tag_m = sys.modules[__package__ + "issue_tag"]

        d = src_dict.copy()

        _MultiValueActivityItem_kwargs = super().from_dict(src_dict=d).to_dict()
        _MultiValueActivityItem_kwargs.pop("$type")

        _target = d.pop("target", UNSET)
        target: Union[Unset, issue_m.Issue]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = issue_m.Issue.from_dict(_target)

        removed = []
        _removed = d.pop("removed", UNSET)
        for removed_item_data in _removed or []:
            removed_item = issue_tag_m.IssueTag.from_dict(removed_item_data)

            removed.append(removed_item)

        added = []
        _added = d.pop("added", UNSET)
        for added_item_data in _added or []:
            added_item = issue_tag_m.IssueTag.from_dict(added_item_data)

            added.append(added_item)

        tags_activity_item = cls(
            target=target,
            removed=removed,
            added=added,
            **_MultiValueActivityItem_kwargs,
        )

        return tags_activity_item
