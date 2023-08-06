from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_work_item import IssueWorkItem
else:
    IssueWorkItem = "IssueWorkItem"


T = TypeVar("T", bound="IssueTimeTracker")


@attr.s(auto_attribs=True)
class IssueTimeTracker:
    """Represents time tracking settings in the issue."""

    work_items: Union[Unset, List[IssueWorkItem]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        work_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.work_items, Unset):
            work_items = []
            for work_items_item_data in self.work_items:
                work_items_item = work_items_item_data.to_dict()

                work_items.append(work_items_item)

        enabled = self.enabled
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if work_items is not UNSET:
            field_dict["workItems"] = work_items
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        work_items = []
        _work_items = d.pop("workItems", UNSET)
        for work_items_item_data in _work_items or []:
            work_items_item = IssueWorkItem.from_dict(work_items_item_data)

            work_items.append(work_items_item)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        issue_time_tracker = cls(
            work_items=work_items,
            enabled=enabled,
            id=id,
            type=type,
        )

        issue_time_tracker.additional_properties = d
        return issue_time_tracker

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
