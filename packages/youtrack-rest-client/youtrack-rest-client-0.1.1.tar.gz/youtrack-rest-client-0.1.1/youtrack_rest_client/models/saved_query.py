from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue import Issue
else:
    Issue = "Issue"

from ..models.watch_folder import WatchFolder

T = TypeVar("T", bound="SavedQuery")


@attr.s(auto_attribs=True)
class SavedQuery(WatchFolder):
    """Represents a saved search."""

    query: Union[Unset, str] = UNSET
    issues: Union[Unset, List[Issue]] = UNSET
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
        d = src_dict.copy()

        _WatchFolder_kwargs = super().from_dict(src_dict=d).to_dict()

        query = d.pop("query", UNSET)

        issues = []
        _issues = d.pop("issues", UNSET)
        for issues_item_data in _issues or []:
            issues_item = Issue.from_dict(issues_item_data)

            issues.append(issues_item)

        saved_query = cls(
            query=query,
            issues=issues,
            **_WatchFolder_kwargs,
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
