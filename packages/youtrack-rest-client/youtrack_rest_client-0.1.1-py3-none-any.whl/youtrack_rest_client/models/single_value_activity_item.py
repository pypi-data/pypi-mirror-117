from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.activity_item import ActivityItem

T = TypeVar("T", bound="SingleValueActivityItem")


@attr.s(auto_attribs=True)
class SingleValueActivityItem(ActivityItem):
    """Describe change of properties that can have single value."""

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

        single_value_activity_item = cls(
            **_ActivityItem_kwargs,
        )

        single_value_activity_item.additional_properties = d
        return single_value_activity_item

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
