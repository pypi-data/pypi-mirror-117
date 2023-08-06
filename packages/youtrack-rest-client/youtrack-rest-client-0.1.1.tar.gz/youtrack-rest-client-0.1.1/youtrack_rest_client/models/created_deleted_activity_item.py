from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.activity_item import ActivityItem

T = TypeVar("T", bound="CreatedDeletedActivityItem")


@attr.s(auto_attribs=True)
class CreatedDeletedActivityItem(ActivityItem):
    """Represents an action when an entity is created or deleted in an issue. For example, a new comment is created in the issue."""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _ActivityItem_dict = super().to_dict()
        field_dict.update(_ActivityItem_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _ActivityItem_kwargs = super().from_dict(src_dict=d).to_dict()

        created_deleted_activity_item = cls(
            **_ActivityItem_kwargs,
        )

        created_deleted_activity_item.additional_properties = d
        return created_deleted_activity_item

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
