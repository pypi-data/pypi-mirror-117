from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.simple_value_activity_item import SimpleValueActivityItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="TextMarkupActivityItem")


@attr.s(auto_attribs=True)
class TextMarkupActivityItem(SimpleValueActivityItem):
    """Represents a change in a `String`-type attribute with the support of markup:
    `description` in an Issue or IssueWorkItem, and the `text` of the IssueComment.
    This entity lets you get the rendered text after the change."""

    removed: Union[Unset, str] = UNSET
    added: Union[Unset, str] = UNSET
    markup: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        removed = self.removed
        added = self.added
        markup = self.markup

        field_dict: Dict[str, Any] = {}
        _SimpleValueActivityItem_dict = super().to_dict()
        field_dict.update(_SimpleValueActivityItem_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if removed is not UNSET:
            field_dict["removed"] = removed
        if added is not UNSET:
            field_dict["added"] = added
        if markup is not UNSET:
            field_dict["markup"] = markup

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _SimpleValueActivityItem_kwargs = super().from_dict(src_dict=d).to_dict()

        removed = d.pop("removed", UNSET)

        added = d.pop("added", UNSET)

        markup = d.pop("markup", UNSET)

        text_markup_activity_item = cls(
            removed=removed,
            added=added,
            markup=markup,
            **_SimpleValueActivityItem_kwargs,
        )

        text_markup_activity_item.additional_properties = d
        return text_markup_activity_item

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
