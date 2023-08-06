from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.custom_field_defaults import CustomFieldDefaults

T = TypeVar("T", bound="BundleCustomFieldDefaults")


@attr.s(auto_attribs=True)
class BundleCustomFieldDefaults(CustomFieldDefaults):
    """Represents field defaults for bundle fields."""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _CustomFieldDefaults_dict = super().to_dict()
        field_dict.update(_CustomFieldDefaults_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _CustomFieldDefaults_kwargs = super().from_dict(src_dict=d).to_dict()

        bundle_custom_field_defaults = cls(
            **_CustomFieldDefaults_kwargs,
        )

        bundle_custom_field_defaults.additional_properties = d
        return bundle_custom_field_defaults

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
