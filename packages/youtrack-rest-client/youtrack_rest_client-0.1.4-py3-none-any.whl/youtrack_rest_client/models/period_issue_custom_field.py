from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeriodIssueCustomField")


try:
    from ..models import issue_custom_field
except ImportError:
    import sys

    issue_custom_field = sys.modules[__package__ + "issue_custom_field"]


@attr.s(auto_attribs=True)
class PeriodIssueCustomField(issue_custom_field.IssueCustomField):
    """Represents the period field in the issue."""

    value: "Union[Unset, period_value_m.PeriodValue]" = UNSET

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
            from ..models import period_value as period_value_m
        except ImportError:
            import sys

            period_value_m = sys.modules[__package__ + "period_value"]

        d = src_dict.copy()

        _value = d.pop("value", UNSET)
        value: Union[Unset, period_value_m.PeriodValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = period_value_m.PeriodValue.from_dict(_value)

        period_issue_custom_field = cls(
            value=value,
        )

        return period_issue_custom_field
