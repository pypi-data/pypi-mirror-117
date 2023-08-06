from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue import Issue
    from ..models.issue_link_direction import IssueLinkDirection
    from ..models.issue_link_type import IssueLinkType
else:
    IssueLinkType = "IssueLinkType"
    IssueLinkDirection = "IssueLinkDirection"
    Issue = "Issue"


T = TypeVar("T", bound="IssueLink")


@attr.s(auto_attribs=True)
class IssueLink:
    """Represents issue links of a particular link type (for example, 'relates to')."""

    direction: Union[Unset, IssueLinkDirection] = UNSET
    link_type: Union[Unset, IssueLinkType] = UNSET
    issues: Union[Unset, List[Issue]] = UNSET
    trimmed_issues: Union[Unset, List[Issue]] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        direction: Union[Unset, str] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        link_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.link_type, Unset):
            link_type = self.link_type.to_dict()

        issues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()

                issues.append(issues_item)

        trimmed_issues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.trimmed_issues, Unset):
            trimmed_issues = []
            for trimmed_issues_item_data in self.trimmed_issues:
                trimmed_issues_item = trimmed_issues_item_data.to_dict()

                trimmed_issues.append(trimmed_issues_item)

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if direction is not UNSET:
            field_dict["direction"] = direction
        if link_type is not UNSET:
            field_dict["linkType"] = link_type
        if issues is not UNSET:
            field_dict["issues"] = issues
        if trimmed_issues is not UNSET:
            field_dict["trimmedIssues"] = trimmed_issues
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, IssueLinkDirection]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = IssueLinkDirection(_direction)

        _link_type = d.pop("linkType", UNSET)
        link_type: Union[Unset, IssueLinkType]
        if isinstance(_link_type, Unset):
            link_type = UNSET
        else:
            link_type = IssueLinkType.from_dict(_link_type)

        issues = []
        _issues = d.pop("issues", UNSET)
        for issues_item_data in _issues or []:
            issues_item = Issue.from_dict(issues_item_data)

            issues.append(issues_item)

        trimmed_issues = []
        _trimmed_issues = d.pop("trimmedIssues", UNSET)
        for trimmed_issues_item_data in _trimmed_issues or []:
            trimmed_issues_item = Issue.from_dict(trimmed_issues_item_data)

            trimmed_issues.append(trimmed_issues_item)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        issue_link = cls(
            direction=direction,
            link_type=link_type,
            issues=issues,
            trimmed_issues=trimmed_issues,
            id=id,
            type=type,
        )

        issue_link.additional_properties = d
        return issue_link

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
