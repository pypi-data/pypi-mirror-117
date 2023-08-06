from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiGroupIssueCustomField")


try:
    from ..models import database_multi_value_issue_custom_field
except ImportError:
    import sys

    database_multi_value_issue_custom_field = sys.modules[__package__ + "database_multi_value_issue_custom_field"]


@attr.s(auto_attribs=True)
class MultiGroupIssueCustomField(database_multi_value_issue_custom_field.DatabaseMultiValueIssueCustomField):
    """Represents the issue custom field of the `group` type that can have multiple values."""

    value: "Union[Unset, user_group_m.UserGroup]" = UNSET

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
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            user_group_m = sys.modules[__package__ + "user_group"]

        d = src_dict.copy()

        _value = d.pop("value", UNSET)
        value: Union[Unset, user_group_m.UserGroup]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = user_group_m.UserGroup.from_dict(_value)

        multi_group_issue_custom_field = cls(
            value=value,
        )

        return multi_group_issue_custom_field
