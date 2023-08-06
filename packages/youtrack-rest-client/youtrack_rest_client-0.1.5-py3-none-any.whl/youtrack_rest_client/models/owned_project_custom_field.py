from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OwnedProjectCustomField")


try:
    from ..models import bundle_project_custom_field
except ImportError:
    import sys

    bundle_project_custom_field = sys.modules[__package__ + "bundle_project_custom_field"]


@attr.s(auto_attribs=True)
class OwnedProjectCustomField(bundle_project_custom_field.BundleProjectCustomField):
    """Represents project settings for the owned field."""

    bundle: "Union[Unset, owned_bundle_m.OwnedBundle]" = UNSET
    default_values: "Union[Unset, List[owned_bundle_element_m.OwnedBundleElement]]" = UNSET

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
        _BundleProjectCustomField_dict = super().to_dict()
        field_dict.update(_BundleProjectCustomField_dict)
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

            owned_bundle_element_m = sys.modules[__package__ + "owned_bundle_element"]
            owned_bundle_m = sys.modules[__package__ + "owned_bundle"]

        d = src_dict.copy()

        _BundleProjectCustomField_kwargs = super().from_dict(src_dict=d).to_dict()
        _BundleProjectCustomField_kwargs.pop("$type")

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

        owned_project_custom_field = cls(
            bundle=bundle,
            default_values=default_values,
            **_BundleProjectCustomField_kwargs,
        )

        return owned_project_custom_field
