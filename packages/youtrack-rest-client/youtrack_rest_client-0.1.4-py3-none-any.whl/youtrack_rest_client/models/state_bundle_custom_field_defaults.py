from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StateBundleCustomFieldDefaults")


try:
    from ..models import bundle_custom_field_defaults
except ImportError:
    import sys

    bundle_custom_field_defaults = sys.modules[__package__ + "bundle_custom_field_defaults"]


@attr.s(auto_attribs=True)
class StateBundleCustomFieldDefaults(bundle_custom_field_defaults.BundleCustomFieldDefaults):
    """Default settings for the state-type field."""

    bundle: "Union[Unset, state_bundle_m.StateBundle]" = UNSET
    default_values: "Union[Unset, List[state_bundle_element_m.StateBundleElement]]" = UNSET

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
            from ..models import state_bundle as state_bundle_m
            from ..models import state_bundle_element as state_bundle_element_m
        except ImportError:
            import sys

            state_bundle_m = sys.modules[__package__ + "state_bundle"]
            state_bundle_element_m = sys.modules[__package__ + "state_bundle_element"]

        d = src_dict.copy()

        _bundle = d.pop("bundle", UNSET)
        bundle: Union[Unset, state_bundle_m.StateBundle]
        if isinstance(_bundle, Unset):
            bundle = UNSET
        else:
            bundle = state_bundle_m.StateBundle.from_dict(_bundle)

        default_values = []
        _default_values = d.pop("defaultValues", UNSET)
        for default_values_item_data in _default_values or []:
            default_values_item = state_bundle_element_m.StateBundleElement.from_dict(default_values_item_data)

            default_values.append(default_values_item)

        state_bundle_custom_field_defaults = cls(
            bundle=bundle,
            default_values=default_values,
        )

        return state_bundle_custom_field_defaults
