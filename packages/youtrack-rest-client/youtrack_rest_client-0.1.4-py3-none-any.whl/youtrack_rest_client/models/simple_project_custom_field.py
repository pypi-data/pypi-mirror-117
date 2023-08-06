from typing import Any, Dict, Type, TypeVar

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

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _ProjectCustomField_dict = super().to_dict()
        field_dict.update(_ProjectCustomField_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        simple_project_custom_field = cls()

        return simple_project_custom_field
