from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiEnumIssueCustomField")


try:
    from ..models import database_multi_value_issue_custom_field
except ImportError:
    import sys

    database_multi_value_issue_custom_field = sys.modules[__package__ + "database_multi_value_issue_custom_field"]


@attr.s(auto_attribs=True)
class MultiEnumIssueCustomField(database_multi_value_issue_custom_field.DatabaseMultiValueIssueCustomField):
    """Represents the issue custom field of the `enum` type that can have multiple values."""

    value: "Union[Unset, enum_bundle_element_m.EnumBundleElement]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        _DatabaseMultiValueIssueCustomField_dict = super().to_dict()
        field_dict.update(_DatabaseMultiValueIssueCustomField_dict)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import enum_bundle_element as enum_bundle_element_m
        except ImportError:
            import sys

            enum_bundle_element_m = sys.modules[__package__ + "enum_bundle_element"]

        d = src_dict.copy()

        _DatabaseMultiValueIssueCustomField_kwargs = super().from_dict(src_dict=d).to_dict()
        _DatabaseMultiValueIssueCustomField_kwargs.pop("$type")

        _value = d.pop("value", UNSET)
        value: Union[Unset, enum_bundle_element_m.EnumBundleElement]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = enum_bundle_element_m.EnumBundleElement.from_dict(_value)

        multi_enum_issue_custom_field = cls(
            value=value,
            **_DatabaseMultiValueIssueCustomField_kwargs,
        )

        return multi_enum_issue_custom_field
