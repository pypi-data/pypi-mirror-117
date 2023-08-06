from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueTag")


try:
    from ..models import watch_folder
except ImportError:
    import sys

    watch_folder = sys.modules[__package__ + "watch_folder"]


@attr.s(auto_attribs=True)
class IssueTag(watch_folder.WatchFolder):
    """Represents an issue tag."""

    issues: "Union[Unset, List[issue_m.Issue]]" = UNSET
    color: "Union[Unset, field_style_m.FieldStyle]" = UNSET
    untag_on_resolve: "Union[Unset, bool]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()

                issues.append(issues_item)

        color: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()

        untag_on_resolve = self.untag_on_resolve

        field_dict: Dict[str, Any] = {}
        _WatchFolder_dict = super().to_dict()
        field_dict.update(_WatchFolder_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issues is not UNSET:
            field_dict["issues"] = issues
        if color is not UNSET:
            field_dict["color"] = color
        if untag_on_resolve is not UNSET:
            field_dict["untagOnResolve"] = untag_on_resolve

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import field_style as field_style_m
            from ..models import issue as issue_m
        except ImportError:
            import sys

            field_style_m = sys.modules[__package__ + "field_style"]
            issue_m = sys.modules[__package__ + "issue"]

        d = src_dict.copy()

        _WatchFolder_kwargs = super().from_dict(src_dict=d).to_dict()

        issues = []
        _issues = d.pop("issues", UNSET)
        for issues_item_data in _issues or []:
            issues_item = issue_m.Issue.from_dict(issues_item_data)

            issues.append(issues_item)

        _color = d.pop("color", UNSET)
        color: Union[Unset, field_style_m.FieldStyle]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = field_style_m.FieldStyle.from_dict(_color)

        untag_on_resolve = d.pop("untagOnResolve", UNSET)

        issue_tag = cls(
            issues=issues,
            color=color,
            untag_on_resolve=untag_on_resolve,
            **_WatchFolder_kwargs,
        )

        issue_tag.additional_properties = d
        return issue_tag

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
