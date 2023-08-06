from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SavedQuery")


try:
    from ..models import watch_folder
except ImportError:
    import sys

    watch_folder = sys.modules[__package__ + "watch_folder"]


@attr.s(auto_attribs=True)
class SavedQuery(watch_folder.WatchFolder):
    """Represents a saved search."""

    query: "Union[Unset, str]" = UNSET
    issues: "Union[Unset, List[issue_m.Issue]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query = self.query
        issues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()

                issues.append(issues_item)

        field_dict: Dict[str, Any] = {}
        _WatchFolder_dict = super().to_dict()
        field_dict.update(_WatchFolder_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if issues is not UNSET:
            field_dict["issues"] = issues

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import issue as issue_m
        except ImportError:
            import sys

            issue_m = sys.modules[__package__ + "issue"]

        d = src_dict.copy()

        query = d.pop("query", UNSET)

        issues = []
        _issues = d.pop("issues", UNSET)
        for issues_item_data in _issues or []:
            issues_item = issue_m.Issue.from_dict(issues_item_data)

            issues.append(issues_item)

        saved_query = cls(
            query=query,
            issues=issues,
        )

        saved_query.additional_properties = d
        return saved_query

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
