from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SimpleProjectCustomField")


try:
    from ..models import project_custom_field
except ImportError:
    import sys

    project_custom_field = sys.modules[__package__ + "project_custom_field"]


@attr.s(auto_attribs=True)
class SimpleProjectCustomField(project_custom_field.ProjectCustomField):
    """Represents project settings for fields of types integer, float, date, date and time, string."""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _ProjectCustomField_dict = super().to_dict()
        field_dict.update(_ProjectCustomField_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        simple_project_custom_field = cls()

        simple_project_custom_field.additional_properties = d
        return simple_project_custom_field

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
