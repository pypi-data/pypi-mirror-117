from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextMarkupActivityItem")


try:
    from ..models import simple_value_activity_item
except ImportError:
    import sys

    simple_value_activity_item = sys.modules[__package__ + "simple_value_activity_item"]


@attr.s(auto_attribs=True)
class TextMarkupActivityItem(simple_value_activity_item.SimpleValueActivityItem):
    """Represents a change in a `String`-type attribute with the support of markup:
    `description` in an Issue or IssueWorkItem, and the `text` of the IssueComment.
    This entity lets you get the rendered text after the change."""

    removed: "Union[Unset, str]" = UNSET
    added: "Union[Unset, str]" = UNSET
    markup: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        removed = self.removed
        added = self.added
        markup = self.markup

        field_dict: Dict[str, Any] = {}
        _SimpleValueActivityItem_dict = super().to_dict()
        field_dict.update(_SimpleValueActivityItem_dict)
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
        _SimpleValueActivityItem_kwargs.pop("$type")

        removed = d.pop("removed", UNSET)

        added = d.pop("added", UNSET)

        markup = d.pop("markup", UNSET)

        text_markup_activity_item = cls(
            removed=removed,
            added=added,
            markup=markup,
            **_SimpleValueActivityItem_kwargs,
        )

        return text_markup_activity_item
