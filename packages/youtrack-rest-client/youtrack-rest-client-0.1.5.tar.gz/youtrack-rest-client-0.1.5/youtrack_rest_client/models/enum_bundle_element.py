from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="EnumBundleElement")


try:
    from ..models import localizable_bundle_element
except ImportError:
    import sys

    localizable_bundle_element = sys.modules[__package__ + "localizable_bundle_element"]


@attr.s(auto_attribs=True)
class EnumBundleElement(localizable_bundle_element.LocalizableBundleElement):
    """Represents an enumeration value in YouTrack."""

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _LocalizableBundleElement_dict = super().to_dict()
        field_dict.update(_LocalizableBundleElement_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _LocalizableBundleElement_kwargs = super().from_dict(src_dict=d).to_dict()
        _LocalizableBundleElement_kwargs.pop("$type")

        enum_bundle_element = cls(
            **_LocalizableBundleElement_kwargs,
        )

        return enum_bundle_element
