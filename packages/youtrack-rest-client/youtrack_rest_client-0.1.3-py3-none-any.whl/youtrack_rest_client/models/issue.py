from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Issue")


@attr.s(auto_attribs=True)
class Issue:
    """Represents an issue in YouTrack."""

    id_readable: "Union[Unset, str]" = UNSET
    created: "Union[Unset, int]" = UNSET
    updated: "Union[Unset, int]" = UNSET
    resolved: "Union[Unset, int]" = UNSET
    number_in_project: "Union[Unset, int]" = UNSET
    project: "Union[Unset, project_m.Project]" = UNSET
    summary: "Union[Unset, str]" = UNSET
    description: "Union[Unset, str]" = UNSET
    uses_markdown: "Union[Unset, bool]" = UNSET
    wikified_description: "Union[Unset, str]" = UNSET
    reporter: "Union[Unset, user_m.User]" = UNSET
    updater: "Union[Unset, user_m.User]" = UNSET
    draft_owner: "Union[Unset, user_m.User]" = UNSET
    is_draft: "Union[Unset, bool]" = UNSET
    visibility: "Union[Unset, visibility_m.Visibility]" = UNSET
    votes: "Union[Unset, int]" = UNSET
    comments: "Union[Unset, List[issue_comment_m.IssueComment]]" = UNSET
    comments_count: "Union[Unset, int]" = UNSET
    tags: "Union[Unset, List[issue_tag_m.IssueTag]]" = UNSET
    links: "Union[Unset, List[issue_link_m.IssueLink]]" = UNSET
    external_issue: "Union[Unset, external_issue_m.ExternalIssue]" = UNSET
    custom_fields: "Union[Unset, List[issue_custom_field_m.IssueCustomField]]" = UNSET
    voters: "Union[Unset, issue_voters_m.IssueVoters]" = UNSET
    watchers: "Union[Unset, issue_watchers_m.IssueWatchers]" = UNSET
    attachments: "Union[Unset, List[issue_attachment_m.IssueAttachment]]" = UNSET
    subtasks: "Union[Unset, issue_link_m.IssueLink]" = UNSET
    parent: "Union[Unset, issue_link_m.IssueLink]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_readable = self.id_readable
        created = self.created
        updated = self.updated
        resolved = self.resolved
        number_in_project = self.number_in_project
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        summary = self.summary
        description = self.description
        uses_markdown = self.uses_markdown
        wikified_description = self.wikified_description
        reporter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reporter, Unset):
            reporter = self.reporter.to_dict()

        updater: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updater, Unset):
            updater = self.updater.to_dict()

        draft_owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.draft_owner, Unset):
            draft_owner = self.draft_owner.to_dict()

        is_draft = self.is_draft
        visibility: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        votes = self.votes
        comments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()

                comments.append(comments_item)

        comments_count = self.comments_count
        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()

                links.append(links_item)

        external_issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_issue, Unset):
            external_issue = self.external_issue.to_dict()

        custom_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()

                custom_fields.append(custom_fields_item)

        voters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.voters, Unset):
            voters = self.voters.to_dict()

        watchers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.watchers, Unset):
            watchers = self.watchers.to_dict()

        attachments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()

                attachments.append(attachments_item)

        subtasks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subtasks, Unset):
            subtasks = self.subtasks.to_dict()

        parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id_readable is not UNSET:
            field_dict["idReadable"] = id_readable
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if number_in_project is not UNSET:
            field_dict["numberInProject"] = number_in_project
        if project is not UNSET:
            field_dict["project"] = project
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if uses_markdown is not UNSET:
            field_dict["usesMarkdown"] = uses_markdown
        if wikified_description is not UNSET:
            field_dict["wikifiedDescription"] = wikified_description
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if updater is not UNSET:
            field_dict["updater"] = updater
        if draft_owner is not UNSET:
            field_dict["draftOwner"] = draft_owner
        if is_draft is not UNSET:
            field_dict["isDraft"] = is_draft
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if votes is not UNSET:
            field_dict["votes"] = votes
        if comments is not UNSET:
            field_dict["comments"] = comments
        if comments_count is not UNSET:
            field_dict["commentsCount"] = comments_count
        if tags is not UNSET:
            field_dict["tags"] = tags
        if links is not UNSET:
            field_dict["links"] = links
        if external_issue is not UNSET:
            field_dict["externalIssue"] = external_issue
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if voters is not UNSET:
            field_dict["voters"] = voters
        if watchers is not UNSET:
            field_dict["watchers"] = watchers
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if subtasks is not UNSET:
            field_dict["subtasks"] = subtasks
        if parent is not UNSET:
            field_dict["parent"] = parent
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import external_issue as external_issue_m
            from ..models import issue_attachment as issue_attachment_m
            from ..models import issue_comment as issue_comment_m
            from ..models import issue_custom_field as issue_custom_field_m
            from ..models import issue_link as issue_link_m
            from ..models import issue_tag as issue_tag_m
            from ..models import issue_voters as issue_voters_m
            from ..models import issue_watchers as issue_watchers_m
            from ..models import project as project_m
            from ..models import user as user_m
            from ..models import visibility as visibility_m
        except ImportError:
            import sys

            issue_watchers_m = sys.modules[__package__ + "issue_watchers"]
            issue_comment_m = sys.modules[__package__ + "issue_comment"]
            issue_attachment_m = sys.modules[__package__ + "issue_attachment"]
            visibility_m = sys.modules[__package__ + "visibility"]
            issue_link_m = sys.modules[__package__ + "issue_link"]
            issue_custom_field_m = sys.modules[__package__ + "issue_custom_field"]
            issue_voters_m = sys.modules[__package__ + "issue_voters"]
            project_m = sys.modules[__package__ + "project"]
            issue_tag_m = sys.modules[__package__ + "issue_tag"]
            user_m = sys.modules[__package__ + "user"]
            external_issue_m = sys.modules[__package__ + "external_issue"]

        d = src_dict.copy()

        id_readable = d.pop("idReadable", UNSET)

        created = d.pop("created", UNSET)

        updated = d.pop("updated", UNSET)

        resolved = d.pop("resolved", UNSET)

        number_in_project = d.pop("numberInProject", UNSET)

        _project = d.pop("project", UNSET)
        project: Union[Unset, project_m.Project]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = project_m.Project.from_dict(_project)

        summary = d.pop("summary", UNSET)

        description = d.pop("description", UNSET)

        uses_markdown = d.pop("usesMarkdown", UNSET)

        wikified_description = d.pop("wikifiedDescription", UNSET)

        _reporter = d.pop("reporter", UNSET)
        reporter: Union[Unset, user_m.User]
        if isinstance(_reporter, Unset):
            reporter = UNSET
        else:
            reporter = user_m.User.from_dict(_reporter)

        _updater = d.pop("updater", UNSET)
        updater: Union[Unset, user_m.User]
        if isinstance(_updater, Unset):
            updater = UNSET
        else:
            updater = user_m.User.from_dict(_updater)

        _draft_owner = d.pop("draftOwner", UNSET)
        draft_owner: Union[Unset, user_m.User]
        if isinstance(_draft_owner, Unset):
            draft_owner = UNSET
        else:
            draft_owner = user_m.User.from_dict(_draft_owner)

        is_draft = d.pop("isDraft", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, visibility_m.Visibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = visibility_m.Visibility.from_dict(_visibility)

        votes = d.pop("votes", UNSET)

        comments = []
        _comments = d.pop("comments", UNSET)
        for comments_item_data in _comments or []:
            comments_item = issue_comment_m.IssueComment.from_dict(comments_item_data)

            comments.append(comments_item)

        comments_count = d.pop("commentsCount", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = issue_tag_m.IssueTag.from_dict(tags_item_data)

            tags.append(tags_item)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = issue_link_m.IssueLink.from_dict(links_item_data)

            links.append(links_item)

        _external_issue = d.pop("externalIssue", UNSET)
        external_issue: Union[Unset, external_issue_m.ExternalIssue]
        if isinstance(_external_issue, Unset):
            external_issue = UNSET
        else:
            external_issue = external_issue_m.ExternalIssue.from_dict(_external_issue)

        custom_fields = []
        _custom_fields = d.pop("customFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = issue_custom_field_m.IssueCustomField.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        _voters = d.pop("voters", UNSET)
        voters: Union[Unset, issue_voters_m.IssueVoters]
        if isinstance(_voters, Unset):
            voters = UNSET
        else:
            voters = issue_voters_m.IssueVoters.from_dict(_voters)

        _watchers = d.pop("watchers", UNSET)
        watchers: Union[Unset, issue_watchers_m.IssueWatchers]
        if isinstance(_watchers, Unset):
            watchers = UNSET
        else:
            watchers = issue_watchers_m.IssueWatchers.from_dict(_watchers)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = issue_attachment_m.IssueAttachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        _subtasks = d.pop("subtasks", UNSET)
        subtasks: Union[Unset, issue_link_m.IssueLink]
        if isinstance(_subtasks, Unset):
            subtasks = UNSET
        else:
            subtasks = issue_link_m.IssueLink.from_dict(_subtasks)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, issue_link_m.IssueLink]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = issue_link_m.IssueLink.from_dict(_parent)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        issue = cls(
            id_readable=id_readable,
            created=created,
            updated=updated,
            resolved=resolved,
            number_in_project=number_in_project,
            project=project,
            summary=summary,
            description=description,
            uses_markdown=uses_markdown,
            wikified_description=wikified_description,
            reporter=reporter,
            updater=updater,
            draft_owner=draft_owner,
            is_draft=is_draft,
            visibility=visibility,
            votes=votes,
            comments=comments,
            comments_count=comments_count,
            tags=tags,
            links=links,
            external_issue=external_issue,
            custom_fields=custom_fields,
            voters=voters,
            watchers=watchers,
            attachments=attachments,
            subtasks=subtasks,
            parent=parent,
            id=id,
            type=type,
        )

        issue.additional_properties = d
        return issue

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
