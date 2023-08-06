from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="BundleProjectCustomField")


try:
    from ..models import project_custom_field
except ImportError:
    import sys

    project_custom_field = sys.modules[__package__ + "project_custom_field"]


@attr.s(auto_attribs=True)
class BundleProjectCustomField(project_custom_field.ProjectCustomField):
    """Represents project settings for the field with a defined set of values."""

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _ProjectCustomField_dict = super().to_dict()
        field_dict.update(_ProjectCustomField_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        bundle_project_custom_field = cls()

        return bundle_project_custom_field
