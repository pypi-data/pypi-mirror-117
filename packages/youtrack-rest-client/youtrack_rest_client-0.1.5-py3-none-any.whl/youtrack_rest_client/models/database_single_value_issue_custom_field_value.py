from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="DatabaseSingleValueIssueCustomFieldValue")


@attr.s(auto_attribs=True)
class DatabaseSingleValueIssueCustomFieldValue:
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        database_single_value_issue_custom_field_value = cls()

        return database_single_value_issue_custom_field_value
