from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.localizable_bundle_element import LocalizableBundleElement

T = TypeVar("T", bound="EnumBundleElement")


@attr.s(auto_attribs=True)
class EnumBundleElement(LocalizableBundleElement):
    """Represents an enumeration value in YouTrack."""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _LocalizableBundleElement_dict = super().to_dict()
        field_dict.update(_LocalizableBundleElement_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _LocalizableBundleElement_kwargs = super().from_dict(src_dict=d).to_dict()

        enum_bundle_element = cls(
            **_LocalizableBundleElement_kwargs,
        )

        enum_bundle_element.additional_properties = d
        return enum_bundle_element

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
