from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextCustomFieldActivityItem")


try:
    from ..models import custom_field_activity_item
except ImportError:
    import sys

    custom_field_activity_item = sys.modules[__package__ + "custom_field_activity_item"]


@attr.s(auto_attribs=True)
class TextCustomFieldActivityItem(custom_field_activity_item.CustomFieldActivityItem):
    """Represents an activity that affects a custom field of the `text` type of an issue."""

    target: "Union[Unset, issue_m.Issue]" = UNSET
    removed: "Union[Unset, str]" = UNSET
    added: "Union[Unset, str]" = UNSET
    markup: "Union[Unset, str]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        removed = self.removed
        added = self.added
        markup = self.markup

        field_dict: Dict[str, Any] = {}
        _CustomFieldActivityItem_dict = super().to_dict()
        field_dict.update(_CustomFieldActivityItem_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target is not UNSET:
            field_dict["target"] = target
        if removed is not UNSET:
            field_dict["removed"] = removed
        if added is not UNSET:
            field_dict["added"] = added
        if markup is not UNSET:
            field_dict["markup"] = markup

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import issue as issue_m
        except ImportError:
            import sys

            issue_m = sys.modules[__package__ + "issue"]

        d = src_dict.copy()

        _target = d.pop("target", UNSET)
        target: Union[Unset, issue_m.Issue]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = issue_m.Issue.from_dict(_target)

        removed = d.pop("removed", UNSET)

        added = d.pop("added", UNSET)

        markup = d.pop("markup", UNSET)

        text_custom_field_activity_item = cls(
            target=target,
            removed=removed,
            added=added,
            markup=markup,
        )

        text_custom_field_activity_item.additional_properties = d
        return text_custom_field_activity_item

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
