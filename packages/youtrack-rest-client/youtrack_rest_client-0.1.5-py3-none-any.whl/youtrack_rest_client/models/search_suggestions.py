from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchSuggestions")


@attr.s(auto_attribs=True)
class SearchSuggestions:
    """Represents the list of search suggestions for the currently entered search query."""

    caret: "Union[Unset, int]" = UNSET
    ignore_unresolved_setting: "Union[Unset, bool]" = UNSET
    query: "Union[Unset, str]" = UNSET
    suggestions: "Union[Unset, List[suggestion_m.Suggestion]]" = UNSET
    folders: "Union[Unset, List[issue_folder_m.IssueFolder]]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        caret = self.caret
        ignore_unresolved_setting = self.ignore_unresolved_setting
        query = self.query
        suggestions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.suggestions, Unset):
            suggestions = []
            for suggestions_item_data in self.suggestions:
                suggestions_item = suggestions_item_data.to_dict()

                suggestions.append(suggestions_item)

        folders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()

                folders.append(folders_item)

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if caret is not UNSET:
            field_dict["caret"] = caret
        if ignore_unresolved_setting is not UNSET:
            field_dict["ignoreUnresolvedSetting"] = ignore_unresolved_setting
        if query is not UNSET:
            field_dict["query"] = query
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions
        if folders is not UNSET:
            field_dict["folders"] = folders
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import issue_folder as issue_folder_m
            from ..models import suggestion as suggestion_m
        except ImportError:
            import sys

            issue_folder_m = sys.modules[__package__ + "issue_folder"]
            suggestion_m = sys.modules[__package__ + "suggestion"]

        d = src_dict.copy()

        caret = d.pop("caret", UNSET)

        ignore_unresolved_setting = d.pop("ignoreUnresolvedSetting", UNSET)

        query = d.pop("query", UNSET)

        suggestions = []
        _suggestions = d.pop("suggestions", UNSET)
        for suggestions_item_data in _suggestions or []:
            suggestions_item = suggestion_m.Suggestion.from_dict(suggestions_item_data)

            suggestions.append(suggestions_item)

        folders = []
        _folders = d.pop("folders", UNSET)
        for folders_item_data in _folders or []:
            folders_item = issue_folder_m.IssueFolder.from_dict(folders_item_data)

            folders.append(folders_item)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        search_suggestions = cls(
            caret=caret,
            ignore_unresolved_setting=ignore_unresolved_setting,
            query=query,
            suggestions=suggestions,
            folders=folders,
            id=id,
            type=type,
        )

        return search_suggestions
