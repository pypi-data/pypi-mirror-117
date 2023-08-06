from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_custom_field import ProjectCustomField
    from ..models.simple_issue_custom_field_value import SimpleIssueCustomFieldValue
else:
    ProjectCustomField = "ProjectCustomField"
    SimpleIssueCustomFieldValue = "SimpleIssueCustomFieldValue"

from ..models.issue_custom_field import IssueCustomField

T = TypeVar("T", bound="SimpleIssueCustomField")


@attr.s(auto_attribs=True)
class SimpleIssueCustomField(IssueCustomField):
    """Represents the field of simple type in the issue."""

    project_custom_field: Union[Unset, ProjectCustomField] = UNSET
    value: Union[Unset, SimpleIssueCustomFieldValue] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_custom_field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_custom_field, Unset):
            project_custom_field = self.project_custom_field.to_dict()

        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        _IssueCustomField_dict = super().to_dict()
        field_dict.update(_IssueCustomField_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_custom_field is not UNSET:
            field_dict["projectCustomField"] = project_custom_field
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _IssueCustomField_kwargs = super().from_dict(src_dict=d).to_dict()

        _project_custom_field = d.pop("projectCustomField", UNSET)
        project_custom_field: Union[Unset, ProjectCustomField]
        if isinstance(_project_custom_field, Unset):
            project_custom_field = UNSET
        else:
            project_custom_field = ProjectCustomField.from_dict(_project_custom_field)

        _value = d.pop("value", UNSET)
        value: Union[Unset, SimpleIssueCustomFieldValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = SimpleIssueCustomFieldValue.from_dict(_value)

        simple_issue_custom_field = cls(
            project_custom_field=project_custom_field,
            value=value,
            **_IssueCustomField_kwargs,
        )

        simple_issue_custom_field.additional_properties = d
        return simple_issue_custom_field

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
