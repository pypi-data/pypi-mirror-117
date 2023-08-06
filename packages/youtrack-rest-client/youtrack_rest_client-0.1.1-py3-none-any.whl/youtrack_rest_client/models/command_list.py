from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.command_visibility import CommandVisibility
    from ..models.issue import Issue
    from ..models.parsed_command import ParsedCommand
    from ..models.suggestion import Suggestion
else:
    Suggestion = "Suggestion"
    ParsedCommand = "ParsedCommand"
    CommandVisibility = "CommandVisibility"
    Issue = "Issue"


T = TypeVar("T", bound="CommandList")


@attr.s(auto_attribs=True)
class CommandList:
    """Represents list of command and related comment in YouTrack.
    Can be used to either apply a command or get command suggestions."""

    comment: Union[Unset, str] = UNSET
    visibility: Union[Unset, CommandVisibility] = UNSET
    query: Union[Unset, str] = UNSET
    caret: Union[Unset, int] = UNSET
    silent: Union[Unset, bool] = UNSET
    uses_markdown: Union[Unset, bool] = UNSET
    run_as: Union[Unset, str] = UNSET
    commands: Union[Unset, List[ParsedCommand]] = UNSET
    issues: Union[Unset, List[Issue]] = UNSET
    suggestions: Union[Unset, List[Suggestion]] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comment = self.comment
        visibility: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        query = self.query
        caret = self.caret
        silent = self.silent
        uses_markdown = self.uses_markdown
        run_as = self.run_as
        commands: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.commands, Unset):
            commands = []
            for commands_item_data in self.commands:
                commands_item = commands_item_data.to_dict()

                commands.append(commands_item)

        issues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()

                issues.append(issues_item)

        suggestions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.suggestions, Unset):
            suggestions = []
            for suggestions_item_data in self.suggestions:
                suggestions_item = suggestions_item_data.to_dict()

                suggestions.append(suggestions_item)

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if query is not UNSET:
            field_dict["query"] = query
        if caret is not UNSET:
            field_dict["caret"] = caret
        if silent is not UNSET:
            field_dict["silent"] = silent
        if uses_markdown is not UNSET:
            field_dict["usesMarkdown"] = uses_markdown
        if run_as is not UNSET:
            field_dict["runAs"] = run_as
        if commands is not UNSET:
            field_dict["commands"] = commands
        if issues is not UNSET:
            field_dict["issues"] = issues
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        comment = d.pop("comment", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, CommandVisibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = CommandVisibility.from_dict(_visibility)

        query = d.pop("query", UNSET)

        caret = d.pop("caret", UNSET)

        silent = d.pop("silent", UNSET)

        uses_markdown = d.pop("usesMarkdown", UNSET)

        run_as = d.pop("runAs", UNSET)

        commands = []
        _commands = d.pop("commands", UNSET)
        for commands_item_data in _commands or []:
            commands_item = ParsedCommand.from_dict(commands_item_data)

            commands.append(commands_item)

        issues = []
        _issues = d.pop("issues", UNSET)
        for issues_item_data in _issues or []:
            issues_item = Issue.from_dict(issues_item_data)

            issues.append(issues_item)

        suggestions = []
        _suggestions = d.pop("suggestions", UNSET)
        for suggestions_item_data in _suggestions or []:
            suggestions_item = Suggestion.from_dict(suggestions_item_data)

            suggestions.append(suggestions_item)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        command_list = cls(
            comment=comment,
            visibility=visibility,
            query=query,
            caret=caret,
            silent=silent,
            uses_markdown=uses_markdown,
            run_as=run_as,
            commands=commands,
            issues=issues,
            suggestions=suggestions,
            id=id,
            type=type,
        )

        command_list.additional_properties = d
        return command_list

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
