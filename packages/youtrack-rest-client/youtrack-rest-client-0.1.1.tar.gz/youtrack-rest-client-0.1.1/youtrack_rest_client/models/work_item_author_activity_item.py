from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_work_item import IssueWorkItem
    from ..models.user import User
else:
    IssueWorkItem = "IssueWorkItem"
    User = "User"

from ..models.single_value_activity_item import SingleValueActivityItem

T = TypeVar("T", bound="WorkItemAuthorActivityItem")


@attr.s(auto_attribs=True)
class WorkItemAuthorActivityItem(SingleValueActivityItem):
    """Represents a change in the `author` attribute of a work item."""

    target: Union[Unset, IssueWorkItem] = UNSET
    removed: Union[Unset, User] = UNSET
    added: Union[Unset, User] = UNSET
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
        _SingleValueActivityItem_dict = super().to_dict()
        field_dict.update(_SingleValueActivityItem_dict)
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
        d = src_dict.copy()

        _SingleValueActivityItem_kwargs = super().from_dict(src_dict=d).to_dict()

        _target = d.pop("target", UNSET)
        target: Union[Unset, IssueWorkItem]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = IssueWorkItem.from_dict(_target)

        _removed = d.pop("removed", UNSET)
        removed: Union[Unset, User]
        if isinstance(_removed, Unset):
            removed = UNSET
        else:
            removed = User.from_dict(_removed)

        _added = d.pop("added", UNSET)
        added: Union[Unset, User]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = User.from_dict(_added)

        work_item_author_activity_item = cls(
            target=target,
            removed=removed,
            added=added,
            **_SingleValueActivityItem_kwargs,
        )

        work_item_author_activity_item.additional_properties = d
        return work_item_author_activity_item

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
