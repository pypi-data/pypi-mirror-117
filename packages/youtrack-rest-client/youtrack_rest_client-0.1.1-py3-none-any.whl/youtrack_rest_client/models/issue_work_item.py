from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration_value import DurationValue
    from ..models.issue import Issue
    from ..models.user import User
    from ..models.work_item_type import WorkItemType
else:
    DurationValue = "DurationValue"
    WorkItemType = "WorkItemType"
    User = "User"
    Issue = "Issue"


T = TypeVar("T", bound="IssueWorkItem")


@attr.s(auto_attribs=True)
class IssueWorkItem:
    """Represents a work item in an issue."""

    author: Union[Unset, User] = UNSET
    creator: Union[Unset, User] = UNSET
    text: Union[Unset, str] = UNSET
    text_preview: Union[Unset, str] = UNSET
    type: Union[Unset, WorkItemType] = UNSET
    created: Union[Unset, int] = UNSET
    updated: Union[Unset, int] = UNSET
    duration: Union[Unset, DurationValue] = UNSET
    date: Union[Unset, int] = UNSET
    issue: Union[Unset, Issue] = UNSET
    uses_markdown: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        creator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        text = self.text
        text_preview = self.text_preview
        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        created = self.created
        updated = self.updated
        duration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.to_dict()

        date = self.date
        issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        uses_markdown = self.uses_markdown
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if creator is not UNSET:
            field_dict["creator"] = creator
        if text is not UNSET:
            field_dict["text"] = text
        if text_preview is not UNSET:
            field_dict["textPreview"] = text_preview
        if type is not UNSET:
            field_dict["type"] = type
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if duration is not UNSET:
            field_dict["duration"] = duration
        if date is not UNSET:
            field_dict["date"] = date
        if issue is not UNSET:
            field_dict["issue"] = issue
        if uses_markdown is not UNSET:
            field_dict["usesMarkdown"] = uses_markdown
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _author = d.pop("author", UNSET)
        author: Union[Unset, User]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = User.from_dict(_author)

        _creator = d.pop("creator", UNSET)
        creator: Union[Unset, User]
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = User.from_dict(_creator)

        text = d.pop("text", UNSET)

        text_preview = d.pop("textPreview", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, WorkItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = WorkItemType.from_dict(_type)

        created = d.pop("created", UNSET)

        updated = d.pop("updated", UNSET)

        _duration = d.pop("duration", UNSET)
        duration: Union[Unset, DurationValue]
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = DurationValue.from_dict(_duration)

        date = d.pop("date", UNSET)

        _issue = d.pop("issue", UNSET)
        issue: Union[Unset, Issue]
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = Issue.from_dict(_issue)

        uses_markdown = d.pop("usesMarkdown", UNSET)

        id = d.pop("id", UNSET)

        issue_work_item = cls(
            author=author,
            creator=creator,
            text=text,
            text_preview=text_preview,
            type=type,
            created=created,
            updated=updated,
            duration=duration,
            date=date,
            issue=issue,
            uses_markdown=uses_markdown,
            id=id,
        )

        issue_work_item.additional_properties = d
        return issue_work_item

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
