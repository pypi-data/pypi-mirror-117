from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue import Issue
    from ..models.issue_attachment import IssueAttachment
    from ..models.user import User
    from ..models.visibility import Visibility
else:
    Visibility = "Visibility"
    User = "User"
    IssueAttachment = "IssueAttachment"
    Issue = "Issue"


T = TypeVar("T", bound="IssueComment")


@attr.s(auto_attribs=True)
class IssueComment:
    """Represents an existing issue comment."""

    text: Union[Unset, str] = UNSET
    uses_markdown: Union[Unset, bool] = UNSET
    text_preview: Union[Unset, str] = UNSET
    created: Union[Unset, int] = UNSET
    updated: Union[Unset, int] = UNSET
    author: Union[Unset, User] = UNSET
    issue: Union[Unset, Issue] = UNSET
    attachments: Union[Unset, List[IssueAttachment]] = UNSET
    visibility: Union[Unset, Visibility] = UNSET
    deleted: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        uses_markdown = self.uses_markdown
        text_preview = self.text_preview
        created = self.created
        updated = self.updated
        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        attachments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()

                attachments.append(attachments_item)

        visibility: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        deleted = self.deleted
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if uses_markdown is not UNSET:
            field_dict["usesMarkdown"] = uses_markdown
        if text_preview is not UNSET:
            field_dict["textPreview"] = text_preview
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if author is not UNSET:
            field_dict["author"] = author
        if issue is not UNSET:
            field_dict["issue"] = issue
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        text = d.pop("text", UNSET)

        uses_markdown = d.pop("usesMarkdown", UNSET)

        text_preview = d.pop("textPreview", UNSET)

        created = d.pop("created", UNSET)

        updated = d.pop("updated", UNSET)

        _author = d.pop("author", UNSET)
        author: Union[Unset, User]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = User.from_dict(_author)

        _issue = d.pop("issue", UNSET)
        issue: Union[Unset, Issue]
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = Issue.from_dict(_issue)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = IssueAttachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, Visibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = Visibility.from_dict(_visibility)

        deleted = d.pop("deleted", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        issue_comment = cls(
            text=text,
            uses_markdown=uses_markdown,
            text_preview=text_preview,
            created=created,
            updated=updated,
            author=author,
            issue=issue,
            attachments=attachments,
            visibility=visibility,
            deleted=deleted,
            id=id,
            type=type,
        )

        issue_comment.additional_properties = d
        return issue_comment

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
