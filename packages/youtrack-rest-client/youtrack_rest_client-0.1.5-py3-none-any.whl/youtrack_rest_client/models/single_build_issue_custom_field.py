from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleBuildIssueCustomField")


try:
    from ..models import database_single_value_issue_custom_field
except ImportError:
    import sys

    database_single_value_issue_custom_field = sys.modules[__package__ + "database_single_value_issue_custom_field"]


@attr.s(auto_attribs=True)
class SingleBuildIssueCustomField(database_single_value_issue_custom_field.DatabaseSingleValueIssueCustomField):
    """Represents the issue custom field of the `build` type that can only have a single value."""

    value: "Union[Unset, build_bundle_element_m.BuildBundleElement]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        _DatabaseSingleValueIssueCustomField_dict = super().to_dict()
        field_dict.update(_DatabaseSingleValueIssueCustomField_dict)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import build_bundle_element as build_bundle_element_m
        except ImportError:
            import sys

            build_bundle_element_m = sys.modules[__package__ + "build_bundle_element"]

        d = src_dict.copy()

        _DatabaseSingleValueIssueCustomField_kwargs = super().from_dict(src_dict=d).to_dict()
        _DatabaseSingleValueIssueCustomField_kwargs.pop("$type")

        _value = d.pop("value", UNSET)
        value: Union[Unset, build_bundle_element_m.BuildBundleElement]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = build_bundle_element_m.BuildBundleElement.from_dict(_value)

        single_build_issue_custom_field = cls(
            value=value,
            **_DatabaseSingleValueIssueCustomField_kwargs,
        )

        return single_build_issue_custom_field
