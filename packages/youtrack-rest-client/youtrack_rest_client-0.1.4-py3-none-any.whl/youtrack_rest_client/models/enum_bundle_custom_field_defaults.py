from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnumBundleCustomFieldDefaults")


try:
    from ..models import bundle_custom_field_defaults
except ImportError:
    import sys

    bundle_custom_field_defaults = sys.modules[__package__ + "bundle_custom_field_defaults"]


@attr.s(auto_attribs=True)
class EnumBundleCustomFieldDefaults(bundle_custom_field_defaults.BundleCustomFieldDefaults):
    """Default settings for the enum-type field."""

    bundle: "Union[Unset, enum_bundle_m.EnumBundle]" = UNSET
    default_values: "Union[Unset, List[enum_bundle_element_m.EnumBundleElement]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        bundle: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bundle, Unset):
            bundle = self.bundle.to_dict()

        default_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.default_values, Unset):
            default_values = []
            for default_values_item_data in self.default_values:
                default_values_item = default_values_item_data.to_dict()

                default_values.append(default_values_item)

        field_dict: Dict[str, Any] = {}
        _BundleCustomFieldDefaults_dict = super().to_dict()
        field_dict.update(_BundleCustomFieldDefaults_dict)
        field_dict.update({})
        if bundle is not UNSET:
            field_dict["bundle"] = bundle
        if default_values is not UNSET:
            field_dict["defaultValues"] = default_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import enum_bundle as enum_bundle_m
            from ..models import enum_bundle_element as enum_bundle_element_m
        except ImportError:
            import sys

            enum_bundle_element_m = sys.modules[__package__ + "enum_bundle_element"]
            enum_bundle_m = sys.modules[__package__ + "enum_bundle"]

        d = src_dict.copy()

        _bundle = d.pop("bundle", UNSET)
        bundle: Union[Unset, enum_bundle_m.EnumBundle]
        if isinstance(_bundle, Unset):
            bundle = UNSET
        else:
            bundle = enum_bundle_m.EnumBundle.from_dict(_bundle)

        default_values = []
        _default_values = d.pop("defaultValues", UNSET)
        for default_values_item_data in _default_values or []:
            default_values_item = enum_bundle_element_m.EnumBundleElement.from_dict(default_values_item_data)

            default_values.append(default_values_item)

        enum_bundle_custom_field_defaults = cls(
            bundle=bundle,
            default_values=default_values,
        )

        return enum_bundle_custom_field_defaults
