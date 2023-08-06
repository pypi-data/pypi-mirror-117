from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateIssueCustomField")


try:
    from ..models import simple_issue_custom_field
except ImportError:
    import sys

    simple_issue_custom_field = sys.modules[__package__ + "simple_issue_custom_field"]


@attr.s(auto_attribs=True)
class DateIssueCustomField(simple_issue_custom_field.SimpleIssueCustomField):
    """Represents the issue custom field of the `date` type."""

    value: "Union[Unset, date_issue_custom_field_value_m.DateIssueCustomFieldValue]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        _SimpleIssueCustomField_dict = super().to_dict()
        field_dict.update(_SimpleIssueCustomField_dict)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import date_issue_custom_field_value as date_issue_custom_field_value_m
        except ImportError:
            import sys

            date_issue_custom_field_value_m = sys.modules[__package__ + "date_issue_custom_field_value"]

        d = src_dict.copy()

        _SimpleIssueCustomField_kwargs = super().from_dict(src_dict=d).to_dict()
        _SimpleIssueCustomField_kwargs.pop("$type")

        _value = d.pop("value", UNSET)
        value: Union[Unset, date_issue_custom_field_value_m.DateIssueCustomFieldValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = date_issue_custom_field_value_m.DateIssueCustomFieldValue.from_dict(_value)

        date_issue_custom_field = cls(
            value=value,
            **_SimpleIssueCustomField_kwargs,
        )

        return date_issue_custom_field
