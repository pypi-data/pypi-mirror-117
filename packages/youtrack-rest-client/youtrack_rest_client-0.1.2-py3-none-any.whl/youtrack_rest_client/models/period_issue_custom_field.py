from typing import Any, Dict, List, Type, TypeVar, Union

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
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        _IssueCustomField_dict = super().to_dict()
        field_dict.update(_IssueCustomField_dict)
        field_dict.update(self.additional_properties)
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

        _IssueCustomField_kwargs = super().from_dict(src_dict=d).to_dict()

        _value = d.pop("value", UNSET)
        value: Union[Unset, period_value_m.PeriodValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = period_value_m.PeriodValue.from_dict(_value)

        period_issue_custom_field = cls(
            value=value,
            **_IssueCustomField_kwargs,
        )

        period_issue_custom_field.additional_properties = d
        return period_issue_custom_field

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
