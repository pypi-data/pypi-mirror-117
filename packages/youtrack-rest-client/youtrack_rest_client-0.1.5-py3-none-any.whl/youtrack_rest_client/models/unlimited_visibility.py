from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="UnlimitedVisibility")


try:
    from ..models import visibility
except ImportError:
    import sys

    visibility = sys.modules[__package__ + "visibility"]


@attr.s(auto_attribs=True)
class UnlimitedVisibility(visibility.Visibility):
    """Represents unlimited visibility."""

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _Visibility_dict = super().to_dict()
        field_dict.update(_Visibility_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _Visibility_kwargs = super().from_dict(src_dict=d).to_dict()
        _Visibility_kwargs.pop("$type")

        unlimited_visibility = cls(
            **_Visibility_kwargs,
        )

        return unlimited_visibility
