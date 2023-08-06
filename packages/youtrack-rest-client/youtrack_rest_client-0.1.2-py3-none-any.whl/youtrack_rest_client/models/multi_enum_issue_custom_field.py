from typing import Any, Dict, List, Type, TypeVar, Union

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
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        _DatabaseMultiValueIssueCustomField_dict = super().to_dict()
        field_dict.update(_DatabaseMultiValueIssueCustomField_dict)
        field_dict.update(self.additional_properties)
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

        multi_enum_issue_custom_field.additional_properties = d
        return multi_enum_issue_custom_field

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
