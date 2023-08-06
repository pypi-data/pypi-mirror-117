from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TextProjectCustomField")


try:
    from ..models import simple_project_custom_field
except ImportError:
    import sys

    simple_project_custom_field = sys.modules[__package__ + "simple_project_custom_field"]


@attr.s(auto_attribs=True)
class TextProjectCustomField(simple_project_custom_field.SimpleProjectCustomField):
    """Represents settings of the text-type field in the project."""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _SimpleProjectCustomField_dict = super().to_dict()
        field_dict.update(_SimpleProjectCustomField_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        text_project_custom_field = cls()

        text_project_custom_field.additional_properties = d
        return text_project_custom_field

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
