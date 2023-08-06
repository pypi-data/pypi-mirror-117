from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueAttachment")


@attr.s(auto_attribs=True)
class IssueAttachment:
    """Represents a file that is attached to an issue or a comment."""

    name: "Union[Unset, str]" = UNSET
    author: "Union[Unset, user_m.User]" = UNSET
    created: "Union[Unset, int]" = UNSET
    updated: "Union[Unset, int]" = UNSET
    size: "Union[Unset, int]" = UNSET
    extension: "Union[Unset, str]" = UNSET
    charset: "Union[Unset, str]" = UNSET
    mime_type: "Union[Unset, str]" = UNSET
    meta_data: "Union[Unset, str]" = UNSET
    draft: "Union[Unset, bool]" = UNSET
    removed: "Union[Unset, bool]" = UNSET
    base_64_content: "Union[Unset, str]" = UNSET
    url: "Union[Unset, str]" = UNSET
    visibility: "Union[Unset, visibility_m.Visibility]" = UNSET
    issue: "Union[Unset, issue_m.Issue]" = UNSET
    comment: "Union[Unset, issue_comment_m.IssueComment]" = UNSET
    thumbnail_url: "Union[Unset, str]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        created = self.created
        updated = self.updated
        size = self.size
        extension = self.extension
        charset = self.charset
        mime_type = self.mime_type
        meta_data = self.meta_data
        draft = self.draft
        removed = self.removed
        base_64_content = self.base_64_content
        url = self.url
        visibility: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        thumbnail_url = self.thumbnail_url
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if author is not UNSET:
            field_dict["author"] = author
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if size is not UNSET:
            field_dict["size"] = size
        if extension is not UNSET:
            field_dict["extension"] = extension
        if charset is not UNSET:
            field_dict["charset"] = charset
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data
        if draft is not UNSET:
            field_dict["draft"] = draft
        if removed is not UNSET:
            field_dict["removed"] = removed
        if base_64_content is not UNSET:
            field_dict["base64Content"] = base_64_content
        if url is not UNSET:
            field_dict["url"] = url
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if issue is not UNSET:
            field_dict["issue"] = issue
        if comment is not UNSET:
            field_dict["comment"] = comment
        if thumbnail_url is not UNSET:
            field_dict["thumbnailURL"] = thumbnail_url
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import issue as issue_m
            from ..models import issue_comment as issue_comment_m
            from ..models import user as user_m
            from ..models import visibility as visibility_m
        except ImportError:
            import sys

            issue_m = sys.modules[__package__ + "issue"]
            user_m = sys.modules[__package__ + "user"]
            visibility_m = sys.modules[__package__ + "visibility"]
            issue_comment_m = sys.modules[__package__ + "issue_comment"]

        d = src_dict.copy()

        name = d.pop("name", UNSET)

        _author = d.pop("author", UNSET)
        author: Union[Unset, user_m.User]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = user_m.User.from_dict(_author)

        created = d.pop("created", UNSET)

        updated = d.pop("updated", UNSET)

        size = d.pop("size", UNSET)

        extension = d.pop("extension", UNSET)

        charset = d.pop("charset", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        meta_data = d.pop("metaData", UNSET)

        draft = d.pop("draft", UNSET)

        removed = d.pop("removed", UNSET)

        base_64_content = d.pop("base64Content", UNSET)

        url = d.pop("url", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, visibility_m.Visibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = visibility_m.Visibility.from_dict(_visibility)

        _issue = d.pop("issue", UNSET)
        issue: Union[Unset, issue_m.Issue]
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = issue_m.Issue.from_dict(_issue)

        _comment = d.pop("comment", UNSET)
        comment: Union[Unset, issue_comment_m.IssueComment]
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = issue_comment_m.IssueComment.from_dict(_comment)

        thumbnail_url = d.pop("thumbnailURL", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        issue_attachment = cls(
            name=name,
            author=author,
            created=created,
            updated=updated,
            size=size,
            extension=extension,
            charset=charset,
            mime_type=mime_type,
            meta_data=meta_data,
            draft=draft,
            removed=removed,
            base_64_content=base_64_content,
            url=url,
            visibility=visibility,
            issue=issue,
            comment=comment,
            thumbnail_url=thumbnail_url,
            id=id,
            type=type,
        )

        return issue_attachment
