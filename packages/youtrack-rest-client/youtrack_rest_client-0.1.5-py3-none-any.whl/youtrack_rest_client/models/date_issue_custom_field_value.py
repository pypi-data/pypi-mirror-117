from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="DateIssueCustomFieldValue")


@attr.s(auto_attribs=True)
class DateIssueCustomFieldValue:
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        date_issue_custom_field_value = cls()

        return date_issue_custom_field_value
