from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuildBundleCustomFieldDefaults")


try:
    from ..models import bundle_custom_field_defaults
except ImportError:
    import sys

    bundle_custom_field_defaults = sys.modules[__package__ + "bundle_custom_field_defaults"]


@attr.s(auto_attribs=True)
class BuildBundleCustomFieldDefaults(bundle_custom_field_defaults.BundleCustomFieldDefaults):
    """Default settings for the build-type field."""

    bundle: "Union[Unset, build_bundle_m.BuildBundle]" = UNSET
    default_values: "Union[Unset, List[build_bundle_element_m.BuildBundleElement]]" = UNSET

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
            from ..models import build_bundle as build_bundle_m
            from ..models import build_bundle_element as build_bundle_element_m
        except ImportError:
            import sys

            build_bundle_m = sys.modules[__package__ + "build_bundle"]
            build_bundle_element_m = sys.modules[__package__ + "build_bundle_element"]

        d = src_dict.copy()

        _BundleCustomFieldDefaults_kwargs = super().from_dict(src_dict=d).to_dict()
        _BundleCustomFieldDefaults_kwargs.pop("$type")

        _bundle = d.pop("bundle", UNSET)
        bundle: Union[Unset, build_bundle_m.BuildBundle]
        if isinstance(_bundle, Unset):
            bundle = UNSET
        else:
            bundle = build_bundle_m.BuildBundle.from_dict(_bundle)

        default_values = []
        _default_values = d.pop("defaultValues", UNSET)
        for default_values_item_data in _default_values or []:
            default_values_item = build_bundle_element_m.BuildBundleElement.from_dict(default_values_item_data)

            default_values.append(default_values_item)

        build_bundle_custom_field_defaults = cls(
            bundle=bundle,
            default_values=default_values,
            **_BundleCustomFieldDefaults_kwargs,
        )

        return build_bundle_custom_field_defaults
