from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="BaseBundle")


try:
    from ..models import bundle
except ImportError:
    import sys

    bundle = sys.modules[__package__ + "bundle"]


@attr.s(auto_attribs=True)
class BaseBundle(bundle.Bundle):
    """Represents a set of field values in YouTrack."""

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _Bundle_dict = super().to_dict()
        field_dict.update(_Bundle_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _Bundle_kwargs = super().from_dict(src_dict=d).to_dict()
        _Bundle_kwargs.pop("$type")

        base_bundle = cls(
            **_Bundle_kwargs,
        )

        return base_bundle
