from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentAttachmentsActivityItem")


try:
    from ..models import multi_value_activity_item
except ImportError:
    import sys

    multi_value_activity_item = sys.modules[__package__ + "multi_value_activity_item"]


@attr.s(auto_attribs=True)
class CommentAttachmentsActivityItem(multi_value_activity_item.MultiValueActivityItem):
    """Represents a change in the `attachments` attribute of an IssueComment."""

    target: "Union[Unset, issue_comment_m.IssueComment]" = UNSET
    removed: "Union[Unset, List[issue_attachment_m.IssueAttachment]]" = UNSET
    added: "Union[Unset, List[issue_attachment_m.IssueAttachment]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
            from ..models import issue_attachment as issue_attachment_m
            from ..models import issue_comment as issue_comment_m
        except ImportError:
            import sys

            issue_comment_m = sys.modules[__package__ + "issue_comment"]
            issue_attachment_m = sys.modules[__package__ + "issue_attachment"]

        d = src_dict.copy()

        _target = d.pop("target", UNSET)
        target: Union[Unset, issue_comment_m.IssueComment]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = issue_comment_m.IssueComment.from_dict(_target)

        removed = []
        _removed = d.pop("removed", UNSET)
        for removed_item_data in _removed or []:
            removed_item = issue_attachment_m.IssueAttachment.from_dict(removed_item_data)

            removed.append(removed_item)

        added = []
        _added = d.pop("added", UNSET)
        for added_item_data in _added or []:
            added_item = issue_attachment_m.IssueAttachment.from_dict(added_item_data)

            added.append(added_item)

        comment_attachments_activity_item = cls(
            target=target,
            removed=removed,
            added=added,
        )

        comment_attachments_activity_item.additional_properties = d
        return comment_attachments_activity_item

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
