from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueVoters")


@attr.s(auto_attribs=True)
class IssueVoters:
    """Represents users that have voted for the issue or its duplicates."""

    has_vote: "Union[Unset, bool]" = UNSET
    original: "Union[Unset, List[user_m.User]]" = UNSET
    duplicate: "Union[Unset, List[duplicate_vote_m.DuplicateVote]]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        has_vote = self.has_vote
        original: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.original, Unset):
            original = []
            for original_item_data in self.original:
                original_item = original_item_data.to_dict()

                original.append(original_item)

        duplicate: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.duplicate, Unset):
            duplicate = []
            for duplicate_item_data in self.duplicate:
                duplicate_item = duplicate_item_data.to_dict()

                duplicate.append(duplicate_item)

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if has_vote is not UNSET:
            field_dict["hasVote"] = has_vote
        if original is not UNSET:
            field_dict["original"] = original
        if duplicate is not UNSET:
            field_dict["duplicate"] = duplicate
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import duplicate_vote as duplicate_vote_m
            from ..models import user as user_m
        except ImportError:
            import sys

            user_m = sys.modules[__package__ + "user"]
            duplicate_vote_m = sys.modules[__package__ + "duplicate_vote"]

        d = src_dict.copy()

        has_vote = d.pop("hasVote", UNSET)

        original = []
        _original = d.pop("original", UNSET)
        for original_item_data in _original or []:
            original_item = user_m.User.from_dict(original_item_data)

            original.append(original_item)

        duplicate = []
        _duplicate = d.pop("duplicate", UNSET)
        for duplicate_item_data in _duplicate or []:
            duplicate_item = duplicate_vote_m.DuplicateVote.from_dict(duplicate_item_data)

            duplicate.append(duplicate_item)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        issue_voters = cls(
            has_vote=has_vote,
            original=original,
            duplicate=duplicate,
            id=id,
            type=type,
        )

        return issue_voters
