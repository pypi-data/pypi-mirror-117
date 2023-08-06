from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SimpleIssueCustomField")


try:
    from ..models import issue_custom_field
except ImportError:
    import sys

    issue_custom_field = sys.modules[__package__ + "issue_custom_field"]


@attr.s(auto_attribs=True)
class SimpleIssueCustomField(issue_custom_field.IssueCustomField):
    """Represents the field of simple type in the issue."""

    project_custom_field: "Union[Unset, project_custom_field_m.ProjectCustomField]" = UNSET
    value: "Union[Unset, simple_issue_custom_field_value_m.SimpleIssueCustomFieldValue]" = UNSET

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
        field_dict.update({})
        if project_custom_field is not UNSET:
            field_dict["projectCustomField"] = project_custom_field
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import project_custom_field as project_custom_field_m
            from ..models import simple_issue_custom_field_value as simple_issue_custom_field_value_m
        except ImportError:
            import sys

            simple_issue_custom_field_value_m = sys.modules[__package__ + "simple_issue_custom_field_value"]
            project_custom_field_m = sys.modules[__package__ + "project_custom_field"]

        d = src_dict.copy()

        _IssueCustomField_kwargs = super().from_dict(src_dict=d).to_dict()
        _IssueCustomField_kwargs.pop("$type")

        _project_custom_field = d.pop("projectCustomField", UNSET)
        project_custom_field: Union[Unset, project_custom_field_m.ProjectCustomField]
        if isinstance(_project_custom_field, Unset):
            project_custom_field = UNSET
        else:
            project_custom_field = project_custom_field_m.ProjectCustomField.from_dict(_project_custom_field)

        _value = d.pop("value", UNSET)
        value: Union[Unset, simple_issue_custom_field_value_m.SimpleIssueCustomFieldValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = simple_issue_custom_field_value_m.SimpleIssueCustomFieldValue.from_dict(_value)

        simple_issue_custom_field = cls(
            project_custom_field=project_custom_field,
            value=value,
            **_IssueCustomField_kwargs,
        )

        return simple_issue_custom_field
