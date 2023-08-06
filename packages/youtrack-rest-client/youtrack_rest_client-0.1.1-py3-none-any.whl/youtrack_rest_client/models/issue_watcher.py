from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue import Issue
    from ..models.user import User
else:
    User = "User"
    Issue = "Issue"


T = TypeVar("T", bound="IssueWatcher")


@attr.s(auto_attribs=True)
class IssueWatcher:
    """Represents a user who subscribed for notifications about an issue."""

    user: Union[Unset, User] = UNSET
    issue: Union[Unset, Issue] = UNSET
    is_starred: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        is_starred = self.is_starred
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if issue is not UNSET:
            field_dict["issue"] = issue
        if is_starred is not UNSET:
            field_dict["isStarred"] = is_starred
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        _issue = d.pop("issue", UNSET)
        issue: Union[Unset, Issue]
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = Issue.from_dict(_issue)

        is_starred = d.pop("isStarred", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        issue_watcher = cls(
            user=user,
            issue=issue,
            is_starred=is_starred,
            id=id,
            type=type,
        )

        issue_watcher.additional_properties = d
        return issue_watcher

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
