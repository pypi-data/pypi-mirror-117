from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateVote")


@attr.s(auto_attribs=True)
class DuplicateVote:
    """Represents a vote for duplicates of the issue."""

    issue: "Union[Unset, issue_m.Issue]" = UNSET
    user: "Union[Unset, user_m.User]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if issue is not UNSET:
            field_dict["issue"] = issue
        if user is not UNSET:
            field_dict["user"] = user
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import issue as issue_m
            from ..models import user as user_m
        except ImportError:
            import sys

            issue_m = sys.modules[__package__ + "issue"]
            user_m = sys.modules[__package__ + "user"]

        d = src_dict.copy()

        _issue = d.pop("issue", UNSET)
        issue: Union[Unset, issue_m.Issue]
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = issue_m.Issue.from_dict(_issue)

        _user = d.pop("user", UNSET)
        user: Union[Unset, user_m.User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = user_m.User.from_dict(_user)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        duplicate_vote = cls(
            issue=issue,
            user=user,
            id=id,
            type=type,
        )

        return duplicate_vote
