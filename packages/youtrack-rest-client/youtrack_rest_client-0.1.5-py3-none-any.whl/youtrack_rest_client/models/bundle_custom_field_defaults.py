from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="BundleCustomFieldDefaults")


try:
    from ..models import custom_field_defaults
except ImportError:
    import sys

    custom_field_defaults = sys.modules[__package__ + "custom_field_defaults"]


@attr.s(auto_attribs=True)
class BundleCustomFieldDefaults(custom_field_defaults.CustomFieldDefaults):
    """Represents field defaults for bundle fields."""

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _CustomFieldDefaults_dict = super().to_dict()
        field_dict.update(_CustomFieldDefaults_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _CustomFieldDefaults_kwargs = super().from_dict(src_dict=d).to_dict()
        _CustomFieldDefaults_kwargs.pop("$type")

        bundle_custom_field_defaults = cls(
            **_CustomFieldDefaults_kwargs,
        )

        return bundle_custom_field_defaults
