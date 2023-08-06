from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PredefinedFilterField")


try:
    from ..models import filter_field
except ImportError:
    import sys

    filter_field = sys.modules[__package__ + "filter_field"]


@attr.s(auto_attribs=True)
class PredefinedFilterField(filter_field.FilterField):
    """Represents a predefined field of the issue. Predefined fields are always present in an issue and
    |cannot be customized in a project. For example, `project`, `created`,
    |`updated`, `tags`, and so on."""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _FilterField_dict = super().to_dict()
        field_dict.update(_FilterField_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        predefined_filter_field = cls()

        predefined_filter_field.additional_properties = d
        return predefined_filter_field

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
