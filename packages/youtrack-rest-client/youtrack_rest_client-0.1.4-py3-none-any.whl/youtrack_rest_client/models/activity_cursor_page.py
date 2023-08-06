from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityCursorPage")


@attr.s(auto_attribs=True)
class ActivityCursorPage:
    """Represents a page object that wraps a list of issue activities.
    The main advantage of the page in comparision to a list of activities is cursors.
    The page provides boundary marks that allow continuous iteration over the activities from the place
    the page is finished."""

    reverse: "Union[Unset, bool]" = UNSET
    before_cursor: "Union[Unset, str]" = UNSET
    after_cursor: "Union[Unset, str]" = UNSET
    has_before: "Union[Unset, bool]" = UNSET
    has_after: "Union[Unset, bool]" = UNSET
    activities: "Union[Unset, List[activity_item_m.ActivityItem]]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        reverse = self.reverse
        before_cursor = self.before_cursor
        after_cursor = self.after_cursor
        has_before = self.has_before
        has_after = self.has_after
        activities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.activities, Unset):
            activities = []
            for activities_item_data in self.activities:
                activities_item = activities_item_data.to_dict()

                activities.append(activities_item)

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if reverse is not UNSET:
            field_dict["reverse"] = reverse
        if before_cursor is not UNSET:
            field_dict["beforeCursor"] = before_cursor
        if after_cursor is not UNSET:
            field_dict["afterCursor"] = after_cursor
        if has_before is not UNSET:
            field_dict["hasBefore"] = has_before
        if has_after is not UNSET:
            field_dict["hasAfter"] = has_after
        if activities is not UNSET:
            field_dict["activities"] = activities
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import activity_item as activity_item_m
        except ImportError:
            import sys

            activity_item_m = sys.modules[__package__ + "activity_item"]

        d = src_dict.copy()

        reverse = d.pop("reverse", UNSET)

        before_cursor = d.pop("beforeCursor", UNSET)

        after_cursor = d.pop("afterCursor", UNSET)

        has_before = d.pop("hasBefore", UNSET)

        has_after = d.pop("hasAfter", UNSET)

        activities = []
        _activities = d.pop("activities", UNSET)
        for activities_item_data in _activities or []:
            activities_item = activity_item_m.ActivityItem.from_dict(activities_item_data)

            activities.append(activities_item)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        activity_cursor_page = cls(
            reverse=reverse,
            before_cursor=before_cursor,
            after_cursor=after_cursor,
            has_before=has_before,
            has_after=has_after,
            activities=activities,
            id=id,
            type=type,
        )

        return activity_cursor_page
