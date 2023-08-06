from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_work_item import IssueWorkItem
else:
    IssueWorkItem = "IssueWorkItem"

from ..models.created_deleted_activity_item import CreatedDeletedActivityItem

T = TypeVar("T", bound="WorkItemActivityItem")


@attr.s(auto_attribs=True)
class WorkItemActivityItem(CreatedDeletedActivityItem):
    """Represents a change in a list of work items in an issue."""

    target: Union[Unset, IssueWorkItem] = UNSET
    removed: Union[Unset, List[IssueWorkItem]] = UNSET
    added: Union[Unset, List[IssueWorkItem]] = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _CreatedDeletedActivityItem_kwargs = super().from_dict(src_dict=d).to_dict()

        _target = d.pop("target", UNSET)
        target: Union[Unset, IssueWorkItem]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = IssueWorkItem.from_dict(_target)

        removed = []
        _removed = d.pop("removed", UNSET)
        for removed_item_data in _removed or []:
            removed_item = IssueWorkItem.from_dict(removed_item_data)

            removed.append(removed_item)

        added = []
        _added = d.pop("added", UNSET)
        for added_item_data in _added or []:
            added_item = IssueWorkItem.from_dict(added_item_data)

            added.append(added_item)

        work_item_activity_item = cls(
            target=target,
            removed=removed,
            added=added,
            **_CreatedDeletedActivityItem_kwargs,
        )

        work_item_activity_item.additional_properties = d
        return work_item_activity_item

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
