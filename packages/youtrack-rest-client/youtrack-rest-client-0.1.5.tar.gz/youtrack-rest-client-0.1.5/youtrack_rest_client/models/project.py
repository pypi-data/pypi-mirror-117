from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Project")


try:
    from ..models import issue_folder
except ImportError:
    import sys

    issue_folder = sys.modules[__package__ + "issue_folder"]


@attr.s(auto_attribs=True)
class Project(issue_folder.IssueFolder):
    """Represents a YouTrack project."""

    starting_number: "Union[Unset, int]" = UNSET
    short_name: "Union[Unset, str]" = UNSET
    description: "Union[Unset, str]" = UNSET
    leader: "Union[Unset, user_m.User]" = UNSET
    created_by: "Union[Unset, user_m.User]" = UNSET
    issues: "Union[Unset, List[issue_m.Issue]]" = UNSET
    custom_fields: "Union[Unset, project_custom_fields_m.ProjectCustomFields]" = UNSET
    archived: "Union[Unset, bool]" = UNSET
    from_email: "Union[Unset, str]" = UNSET
    reply_to_email: "Union[Unset, str]" = UNSET
    template: "Union[Unset, bool]" = UNSET
    icon_url: "Union[Unset, str]" = UNSET
    team: "Union[Unset, user_group_m.UserGroup]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        starting_number = self.starting_number
        short_name = self.short_name
        description = self.description
        leader: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leader, Unset):
            leader = self.leader.to_dict()

        created_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        issues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()

                issues.append(issues_item)

        custom_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        archived = self.archived
        from_email = self.from_email
        reply_to_email = self.reply_to_email
        template = self.template
        icon_url = self.icon_url
        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        _IssueFolder_dict = super().to_dict()
        field_dict.update(_IssueFolder_dict)
        field_dict.update({})
        if starting_number is not UNSET:
            field_dict["startingNumber"] = starting_number
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if description is not UNSET:
            field_dict["description"] = description
        if leader is not UNSET:
            field_dict["leader"] = leader
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if issues is not UNSET:
            field_dict["issues"] = issues
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if archived is not UNSET:
            field_dict["archived"] = archived
        if from_email is not UNSET:
            field_dict["fromEmail"] = from_email
        if reply_to_email is not UNSET:
            field_dict["replyToEmail"] = reply_to_email
        if template is not UNSET:
            field_dict["template"] = template
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import issue as issue_m
            from ..models import project_custom_fields as project_custom_fields_m
            from ..models import user as user_m
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            issue_m = sys.modules[__package__ + "issue"]
            user_group_m = sys.modules[__package__ + "user_group"]
            user_m = sys.modules[__package__ + "user"]
            project_custom_fields_m = sys.modules[__package__ + "project_custom_fields"]

        d = src_dict.copy()

        _IssueFolder_kwargs = super().from_dict(src_dict=d).to_dict()
        _IssueFolder_kwargs.pop("$type")

        starting_number = d.pop("startingNumber", UNSET)

        short_name = d.pop("shortName", UNSET)

        description = d.pop("description", UNSET)

        _leader = d.pop("leader", UNSET)
        leader: Union[Unset, user_m.User]
        if isinstance(_leader, Unset):
            leader = UNSET
        else:
            leader = user_m.User.from_dict(_leader)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, user_m.User]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = user_m.User.from_dict(_created_by)

        issues = []
        _issues = d.pop("issues", UNSET)
        for issues_item_data in _issues or []:
            issues_item = issue_m.Issue.from_dict(issues_item_data)

            issues.append(issues_item)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, project_custom_fields_m.ProjectCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = project_custom_fields_m.ProjectCustomFields.from_dict(_custom_fields)

        archived = d.pop("archived", UNSET)

        from_email = d.pop("fromEmail", UNSET)

        reply_to_email = d.pop("replyToEmail", UNSET)

        template = d.pop("template", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        _team = d.pop("team", UNSET)
        team: Union[Unset, user_group_m.UserGroup]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = user_group_m.UserGroup.from_dict(_team)

        project = cls(
            starting_number=starting_number,
            short_name=short_name,
            description=description,
            leader=leader,
            created_by=created_by,
            issues=issues,
            custom_fields=custom_fields,
            archived=archived,
            from_email=from_email,
            reply_to_email=reply_to_email,
            template=template,
            icon_url=icon_url,
            team=team,
            **_IssueFolder_kwargs,
        )

        return project
