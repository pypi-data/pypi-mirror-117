from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.multi_value_activity_item import MultiValueActivityItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="VisibilityActivityItem")


@attr.s(auto_attribs=True)
class VisibilityActivityItem(MultiValueActivityItem):
    """Represents the changes of properties responsible for visibility restriction.
    Can be <a href="api-entity-VisibilityGroupActivityItem.xml">VisibilityGroupActivityItem</a> or <a href="api-entity-VisibilityUserActivityItem.xml">VisibilityUserActivityItem</a>"""

    target_member: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target_member = self.target_member

        field_dict: Dict[str, Any] = {}
        _MultiValueActivityItem_dict = super().to_dict()
        field_dict.update(_MultiValueActivityItem_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_member is not UNSET:
            field_dict["targetMember"] = target_member

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _MultiValueActivityItem_kwargs = super().from_dict(src_dict=d).to_dict()

        target_member = d.pop("targetMember", UNSET)

        visibility_activity_item = cls(
            target_member=target_member,
            **_MultiValueActivityItem_kwargs,
        )

        visibility_activity_item.additional_properties = d
        return visibility_activity_item

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
