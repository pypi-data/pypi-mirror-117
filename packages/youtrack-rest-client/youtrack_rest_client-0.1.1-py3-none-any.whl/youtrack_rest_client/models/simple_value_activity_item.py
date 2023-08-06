from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.simple_value_activity_item_added import SimpleValueActivityItemAdded
    from ..models.simple_value_activity_item_removed import SimpleValueActivityItemRemoved
else:
    SimpleValueActivityItemRemoved = "SimpleValueActivityItemRemoved"
    SimpleValueActivityItemAdded = "SimpleValueActivityItemAdded"

from ..models.single_value_activity_item import SingleValueActivityItem

T = TypeVar("T", bound="SimpleValueActivityItem")


@attr.s(auto_attribs=True)
class SimpleValueActivityItem(SingleValueActivityItem):
    """Represents the change in attributes of a simple type in the target entity:
    Issue, IssueComment, WorkItem, IssueAttachment."""

    removed: Union[Unset, SimpleValueActivityItemRemoved] = UNSET
    added: Union[Unset, SimpleValueActivityItemAdded] = UNSET
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
        d = src_dict.copy()

        _SingleValueActivityItem_kwargs = super().from_dict(src_dict=d).to_dict()

        _removed = d.pop("removed", UNSET)
        removed: Union[Unset, SimpleValueActivityItemRemoved]
        if isinstance(_removed, Unset):
            removed = UNSET
        else:
            removed = SimpleValueActivityItemRemoved.from_dict(_removed)

        _added = d.pop("added", UNSET)
        added: Union[Unset, SimpleValueActivityItemAdded]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = SimpleValueActivityItemAdded.from_dict(_added)

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
