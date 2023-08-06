from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_comment import IssueComment
    from ..models.user_group import UserGroup
else:
    IssueComment = "IssueComment"
    UserGroup = "UserGroup"

from ..models.created_deleted_activity_item import CreatedDeletedActivityItem

T = TypeVar("T", bound="CommentActivityItem")


@attr.s(auto_attribs=True)
class CommentActivityItem(CreatedDeletedActivityItem):
    """Represents a change in the comments of an issue."""

    target: Union[Unset, IssueComment] = UNSET
    removed: Union[Unset, List[IssueComment]] = UNSET
    added: Union[Unset, List[IssueComment]] = UNSET
    author_group: Union[Unset, UserGroup] = UNSET
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

        author_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author_group, Unset):
            author_group = self.author_group.to_dict()

        field_dict: Dict[str, Any] = {}
        _CreatedDeletedActivityItem_dict = super().to_dict()
        field_dict.update(_CreatedDeletedActivityItem_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target is not UNSET:
            field_dict["target"] = target
        if removed is not UNSET:
            field_dict["removed"] = removed
        if added is not UNSET:
            field_dict["added"] = added
        if author_group is not UNSET:
            field_dict["authorGroup"] = author_group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _CreatedDeletedActivityItem_kwargs = super().from_dict(src_dict=d).to_dict()

        _target = d.pop("target", UNSET)
        target: Union[Unset, IssueComment]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = IssueComment.from_dict(_target)

        removed = []
        _removed = d.pop("removed", UNSET)
        for removed_item_data in _removed or []:
            removed_item = IssueComment.from_dict(removed_item_data)

            removed.append(removed_item)

        added = []
        _added = d.pop("added", UNSET)
        for added_item_data in _added or []:
            added_item = IssueComment.from_dict(added_item_data)

            added.append(added_item)

        _author_group = d.pop("authorGroup", UNSET)
        author_group: Union[Unset, UserGroup]
        if isinstance(_author_group, Unset):
            author_group = UNSET
        else:
            author_group = UserGroup.from_dict(_author_group)

        comment_activity_item = cls(
            target=target,
            removed=removed,
            added=added,
            author_group=author_group,
            **_CreatedDeletedActivityItem_kwargs,
        )

        comment_activity_item.additional_properties = d
        return comment_activity_item

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
