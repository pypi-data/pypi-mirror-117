from typing import Any, Dict, Type, TypeVar

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

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _SimpleProjectCustomField_dict = super().to_dict()
        field_dict.update(_SimpleProjectCustomField_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        text_project_custom_field = cls()

        return text_project_custom_field
