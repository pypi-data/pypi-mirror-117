from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_watcher import IssueWatcher
else:
    IssueWatcher = "IssueWatcher"


T = TypeVar("T", bound="IssueWatchers")


@attr.s(auto_attribs=True)
class IssueWatchers:
    """Represents users that are subscribed to notifications about the issue."""

    has_star: Union[Unset, bool] = UNSET
    issue_watchers: Union[Unset, List[IssueWatcher]] = UNSET
    duplicate_watchers: Union[Unset, List[IssueWatcher]] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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
        d = src_dict.copy()

        has_star = d.pop("hasStar", UNSET)

        issue_watchers = []
        _issue_watchers = d.pop("issueWatchers", UNSET)
        for issue_watchers_item_data in _issue_watchers or []:
            issue_watchers_item = IssueWatcher.from_dict(issue_watchers_item_data)

            issue_watchers.append(issue_watchers_item)

        duplicate_watchers = []
        _duplicate_watchers = d.pop("duplicateWatchers", UNSET)
        for duplicate_watchers_item_data in _duplicate_watchers or []:
            duplicate_watchers_item = IssueWatcher.from_dict(duplicate_watchers_item_data)

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

        issue_watchers.additional_properties = d
        return issue_watchers

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
