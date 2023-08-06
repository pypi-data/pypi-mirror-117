from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextIssueCustomField")


try:
    from ..models import issue_custom_field
except ImportError:
    import sys

    issue_custom_field = sys.modules[__package__ + "issue_custom_field"]


@attr.s(auto_attribs=True)
class TextIssueCustomField(issue_custom_field.IssueCustomField):
    """Represents the issue custom field of the `text` type."""

    value: "Union[Unset, text_field_value_m.TextFieldValue]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        _IssueCustomField_dict = super().to_dict()
        field_dict.update(_IssueCustomField_dict)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import text_field_value as text_field_value_m
        except ImportError:
            import sys

            text_field_value_m = sys.modules[__package__ + "text_field_value"]

        d = src_dict.copy()

        _value = d.pop("value", UNSET)
        value: Union[Unset, text_field_value_m.TextFieldValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = text_field_value_m.TextFieldValue.from_dict(_value)

        text_issue_custom_field = cls(
            value=value,
        )

        return text_issue_custom_field
