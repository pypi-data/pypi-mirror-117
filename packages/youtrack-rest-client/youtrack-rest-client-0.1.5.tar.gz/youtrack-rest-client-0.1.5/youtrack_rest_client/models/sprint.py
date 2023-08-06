from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Sprint")


@attr.s(auto_attribs=True)
class Sprint:
    """Represents a sprint that is associated with an agile board. Each sprint can include issues from one or more projects."""

    agile: "Union[Unset, agile_m.Agile]" = UNSET
    name: "Union[Unset, str]" = UNSET
    goal: "Union[Unset, str]" = UNSET
    start: "Union[Unset, int]" = UNSET
    finish: "Union[Unset, int]" = UNSET
    archived: "Union[Unset, bool]" = UNSET
    is_default: "Union[Unset, bool]" = UNSET
    issues: "Union[Unset, List[issue_m.Issue]]" = UNSET
    unresolved_issues_count: "Union[Unset, int]" = UNSET
    previous_sprint: "Union[Unset, sprint_m.Sprint]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        agile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.agile, Unset):
            agile = self.agile.to_dict()

        name = self.name
        goal = self.goal
        start = self.start
        finish = self.finish
        archived = self.archived
        is_default = self.is_default
        issues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()

                issues.append(issues_item)

        unresolved_issues_count = self.unresolved_issues_count
        previous_sprint: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.previous_sprint, Unset):
            previous_sprint = self.previous_sprint.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if agile is not UNSET:
            field_dict["agile"] = agile
        if name is not UNSET:
            field_dict["name"] = name
        if goal is not UNSET:
            field_dict["goal"] = goal
        if start is not UNSET:
            field_dict["start"] = start
        if finish is not UNSET:
            field_dict["finish"] = finish
        if archived is not UNSET:
            field_dict["archived"] = archived
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if issues is not UNSET:
            field_dict["issues"] = issues
        if unresolved_issues_count is not UNSET:
            field_dict["unresolvedIssuesCount"] = unresolved_issues_count
        if previous_sprint is not UNSET:
            field_dict["previousSprint"] = previous_sprint
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import agile as agile_m
            from ..models import issue as issue_m
            from ..models import sprint as sprint_m
        except ImportError:
            import sys

            agile_m = sys.modules[__package__ + "agile"]
            issue_m = sys.modules[__package__ + "issue"]
            sprint_m = sys.modules[__package__ + "sprint"]

        d = src_dict.copy()

        _agile = d.pop("agile", UNSET)
        agile: Union[Unset, agile_m.Agile]
        if isinstance(_agile, Unset):
            agile = UNSET
        else:
            agile = agile_m.Agile.from_dict(_agile)

        name = d.pop("name", UNSET)

        goal = d.pop("goal", UNSET)

        start = d.pop("start", UNSET)

        finish = d.pop("finish", UNSET)

        archived = d.pop("archived", UNSET)

        is_default = d.pop("isDefault", UNSET)

        issues = []
        _issues = d.pop("issues", UNSET)
        for issues_item_data in _issues or []:
            issues_item = issue_m.Issue.from_dict(issues_item_data)

            issues.append(issues_item)

        unresolved_issues_count = d.pop("unresolvedIssuesCount", UNSET)

        _previous_sprint = d.pop("previousSprint", UNSET)
        previous_sprint: Union[Unset, sprint_m.Sprint]
        if isinstance(_previous_sprint, Unset):
            previous_sprint = UNSET
        else:
            previous_sprint = sprint_m.Sprint.from_dict(_previous_sprint)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        sprint = cls(
            agile=agile,
            name=name,
            goal=goal,
            start=start,
            finish=finish,
            archived=archived,
            is_default=is_default,
            issues=issues,
            unresolved_issues_count=unresolved_issues_count,
            previous_sprint=previous_sprint,
            id=id,
            type=type,
        )

        return sprint
