from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OwnedBundleCustomFieldDefaults")


try:
    from ..models import bundle_custom_field_defaults
except ImportError:
    import sys

    bundle_custom_field_defaults = sys.modules[__package__ + "bundle_custom_field_defaults"]


@attr.s(auto_attribs=True)
class OwnedBundleCustomFieldDefaults(bundle_custom_field_defaults.BundleCustomFieldDefaults):
    """Default settings for the owned-type field."""

    bundle: "Union[Unset, owned_bundle_m.OwnedBundle]" = UNSET
    default_values: "Union[Unset, List[owned_bundle_element_m.OwnedBundleElement]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bundle is not UNSET:
            field_dict["bundle"] = bundle
        if default_values is not UNSET:
            field_dict["defaultValues"] = default_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import owned_bundle as owned_bundle_m
            from ..models import owned_bundle_element as owned_bundle_element_m
        except ImportError:
            import sys

            owned_bundle_m = sys.modules[__package__ + "owned_bundle"]
            owned_bundle_element_m = sys.modules[__package__ + "owned_bundle_element"]

        d = src_dict.copy()

        _BundleCustomFieldDefaults_kwargs = super().from_dict(src_dict=d).to_dict()

        _bundle = d.pop("bundle", UNSET)
        bundle: Union[Unset, owned_bundle_m.OwnedBundle]
        if isinstance(_bundle, Unset):
            bundle = UNSET
        else:
            bundle = owned_bundle_m.OwnedBundle.from_dict(_bundle)

        default_values = []
        _default_values = d.pop("defaultValues", UNSET)
        for default_values_item_data in _default_values or []:
            default_values_item = owned_bundle_element_m.OwnedBundleElement.from_dict(default_values_item_data)

            default_values.append(default_values_item)

        owned_bundle_custom_field_defaults = cls(
            bundle=bundle,
            default_values=default_values,
            **_BundleCustomFieldDefaults_kwargs,
        )

        owned_bundle_custom_field_defaults.additional_properties = d
        return owned_bundle_custom_field_defaults

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
