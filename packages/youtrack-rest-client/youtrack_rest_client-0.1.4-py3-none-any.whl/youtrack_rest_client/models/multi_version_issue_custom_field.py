from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiVersionIssueCustomField")


try:
    from ..models import database_multi_value_issue_custom_field
except ImportError:
    import sys

    database_multi_value_issue_custom_field = sys.modules[__package__ + "database_multi_value_issue_custom_field"]


@attr.s(auto_attribs=True)
class MultiVersionIssueCustomField(database_multi_value_issue_custom_field.DatabaseMultiValueIssueCustomField):
    """Represents the issue custom field of the `version` type that can have multiple values."""

    value: "Union[Unset, version_bundle_element_m.VersionBundleElement]" = UNSET

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
            from ..models import version_bundle_element as version_bundle_element_m
        except ImportError:
            import sys

            version_bundle_element_m = sys.modules[__package__ + "version_bundle_element"]

        d = src_dict.copy()

        _value = d.pop("value", UNSET)
        value: Union[Unset, version_bundle_element_m.VersionBundleElement]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = version_bundle_element_m.VersionBundleElement.from_dict(_value)

        multi_version_issue_custom_field = cls(
            value=value,
        )

        return multi_version_issue_custom_field
