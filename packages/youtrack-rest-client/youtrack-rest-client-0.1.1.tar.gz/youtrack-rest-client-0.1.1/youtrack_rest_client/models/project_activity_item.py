from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue import Issue
    from ..models.project_activity_item_added import ProjectActivityItemAdded
    from ..models.project_activity_item_removed import ProjectActivityItemRemoved
else:
    ProjectActivityItemRemoved = "ProjectActivityItemRemoved"
    ProjectActivityItemAdded = "ProjectActivityItemAdded"
    Issue = "Issue"

from ..models.single_value_activity_item import SingleValueActivityItem

T = TypeVar("T", bound="ProjectActivityItem")


@attr.s(auto_attribs=True)
class ProjectActivityItem(SingleValueActivityItem):
    """Represents the change in the project attribute on an Issue."""

    target: Union[Unset, Issue] = UNSET
    removed: Union[Unset, ProjectActivityItemRemoved] = UNSET
    added: Union[Unset, ProjectActivityItemAdded] = UNSET
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
        target: Union[Unset, Issue]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = Issue.from_dict(_target)

        _removed = d.pop("removed", UNSET)
        removed: Union[Unset, ProjectActivityItemRemoved]
        if isinstance(_removed, Unset):
            removed = UNSET
        else:
            removed = ProjectActivityItemRemoved.from_dict(_removed)

        _added = d.pop("added", UNSET)
        added: Union[Unset, ProjectActivityItemAdded]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = ProjectActivityItemAdded.from_dict(_added)

        project_activity_item = cls(
            target=target,
            removed=removed,
            added=added,
            **_SingleValueActivityItem_kwargs,
        )

        project_activity_item.additional_properties = d
        return project_activity_item

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
