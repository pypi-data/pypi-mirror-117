from typing import Any, Dict, Type, TypeVar

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

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _FilterField_dict = super().to_dict()
        field_dict.update(_FilterField_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _FilterField_kwargs = super().from_dict(src_dict=d).to_dict()
        _FilterField_kwargs.pop("$type")

        predefined_filter_field = cls(
            **_FilterField_kwargs,
        )

        return predefined_filter_field
