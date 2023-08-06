from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueWatchers")


@attr.s(auto_attribs=True)
class IssueWatchers:
    """Represents users that are subscribed to notifications about the issue."""

    has_star: "Union[Unset, bool]" = UNSET
    issue_watchers: "Union[Unset, List[issue_watcher_m.IssueWatcher]]" = UNSET
    duplicate_watchers: "Union[Unset, List[issue_watcher_m.IssueWatcher]]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        has_star = self.has_star
        issue_watchers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.issue_watchers, Unset):
            issue_watchers = []
            for issue_watchers_item_data in self.issue_watchers:
                issue_watchers_item = issue_watchers_item_data.to_dict()

                issue_watchers.append(issue_watchers_item)

        duplicate_watchers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.duplicate_watchers, Unset):
            duplicate_watchers = []
            for duplicate_watchers_item_data in self.duplicate_watchers:
                duplicate_watchers_item = duplicate_watchers_item_data.to_dict()

                duplicate_watchers.append(duplicate_watchers_item)

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if has_star is not UNSET:
            field_dict["hasStar"] = has_star
        if issue_watchers is not UNSET:
            field_dict["issueWatchers"] = issue_watchers
        if duplicate_watchers is not UNSET:
            field_dict["duplicateWatchers"] = duplicate_watchers
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import issue_watcher as issue_watcher_m
        except ImportError:
            import sys

            issue_watcher_m = sys.modules[__package__ + "issue_watcher"]

        d = src_dict.copy()

        has_star = d.pop("hasStar", UNSET)

        issue_watchers = []
        _issue_watchers = d.pop("issueWatchers", UNSET)
        for issue_watchers_item_data in _issue_watchers or []:
            issue_watchers_item = issue_watcher_m.IssueWatcher.from_dict(issue_watchers_item_data)

            issue_watchers.append(issue_watchers_item)

        duplicate_watchers = []
        _duplicate_watchers = d.pop("duplicateWatchers", UNSET)
        for duplicate_watchers_item_data in _duplicate_watchers or []:
            duplicate_watchers_item = issue_watcher_m.IssueWatcher.from_dict(duplicate_watchers_item_data)

            duplicate_watchers.append(duplicate_watchers_item)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        issue_watchers = cls(
            has_star=has_star,
            issue_watchers=issue_watchers,
            duplicate_watchers=duplicate_watchers,
            id=id,
            type=type,
        )

        return issue_watchers
