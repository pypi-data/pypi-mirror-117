from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.database_attribute_value import DatabaseAttributeValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgileColumnFieldValue")


@attr.s(auto_attribs=True)
class AgileColumnFieldValue(DatabaseAttributeValue):
    """Represents a field value or values, parameterizing agile column."""

    name: Union[Unset, str] = UNSET
    is_resolved: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        is_resolved = self.is_resolved

        field_dict: Dict[str, Any] = {}
        _DatabaseAttributeValue_dict = super().to_dict()
        field_dict.update(_DatabaseAttributeValue_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if is_resolved is not UNSET:
            field_dict["isResolved"] = is_resolved

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _DatabaseAttributeValue_kwargs = super().from_dict(src_dict=d).to_dict()

        name = d.pop("name", UNSET)

        is_resolved = d.pop("isResolved", UNSET)

        agile_column_field_value = cls(
            name=name,
            is_resolved=is_resolved,
            **_DatabaseAttributeValue_kwargs,
        )

        agile_column_field_value.additional_properties = d
        return agile_column_field_value

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
