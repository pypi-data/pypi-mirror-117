from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgileColumnFieldValue")


try:
    from ..models import database_attribute_value
except ImportError:
    import sys

    database_attribute_value = sys.modules[__package__ + "database_attribute_value"]


@attr.s(auto_attribs=True)
class AgileColumnFieldValue(database_attribute_value.DatabaseAttributeValue):
    """Represents a field value or values, parameterizing agile column."""

    name: "Union[Unset, str]" = UNSET
    is_resolved: "Union[Unset, bool]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        is_resolved = self.is_resolved

        field_dict: Dict[str, Any] = {}
        _DatabaseAttributeValue_dict = super().to_dict()
        field_dict.update(_DatabaseAttributeValue_dict)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if is_resolved is not UNSET:
            field_dict["isResolved"] = is_resolved

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        name = d.pop("name", UNSET)

        is_resolved = d.pop("isResolved", UNSET)

        agile_column_field_value = cls(
            name=name,
            is_resolved=is_resolved,
        )

        return agile_column_field_value
