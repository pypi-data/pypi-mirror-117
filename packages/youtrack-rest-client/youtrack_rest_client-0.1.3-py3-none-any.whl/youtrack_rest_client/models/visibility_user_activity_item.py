from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VisibilityUserActivityItem")


try:
    from ..models import visibility_activity_item
except ImportError:
    import sys

    visibility_activity_item = sys.modules[__package__ + "visibility_activity_item"]


@attr.s(auto_attribs=True)
class VisibilityUserActivityItem(visibility_activity_item.VisibilityActivityItem):
    """Represents the event when a user adds or removes a user to/from the Visibility settings of the target entity."""

    target_member: "Union[Unset, str]" = UNSET
    target_sub_member: "Union[Unset, str]" = UNSET
    removed: "Union[Unset, List[user_m.User]]" = UNSET
    added: "Union[Unset, List[user_m.User]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target_member = self.target_member
        target_sub_member = self.target_sub_member
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
        _VisibilityActivityItem_dict = super().to_dict()
        field_dict.update(_VisibilityActivityItem_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_member is not UNSET:
            field_dict["targetMember"] = target_member
        if target_sub_member is not UNSET:
            field_dict["targetSubMember"] = target_sub_member
        if removed is not UNSET:
            field_dict["removed"] = removed
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import user as user_m
        except ImportError:
            import sys

            user_m = sys.modules[__package__ + "user"]

        d = src_dict.copy()

        target_member = d.pop("targetMember", UNSET)

        target_sub_member = d.pop("targetSubMember", UNSET)

        removed = []
        _removed = d.pop("removed", UNSET)
        for removed_item_data in _removed or []:
            removed_item = user_m.User.from_dict(removed_item_data)

            removed.append(removed_item)

        added = []
        _added = d.pop("added", UNSET)
        for added_item_data in _added or []:
            added_item = user_m.User.from_dict(added_item_data)

            added.append(added_item)

        visibility_user_activity_item = cls(
            target_member=target_member,
            target_sub_member=target_sub_member,
            removed=removed,
            added=added,
        )

        visibility_user_activity_item.additional_properties = d
        return visibility_user_activity_item

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
