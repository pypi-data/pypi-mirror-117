from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StateProjectCustomField")


try:
    from ..models import bundle_project_custom_field
except ImportError:
    import sys

    bundle_project_custom_field = sys.modules[__package__ + "bundle_project_custom_field"]


@attr.s(auto_attribs=True)
class StateProjectCustomField(bundle_project_custom_field.BundleProjectCustomField):
    """Represents project settings for the state field."""

    bundle: "Union[Unset, state_bundle_m.StateBundle]" = UNSET
    default_values: "Union[Unset, List[state_bundle_element_m.StateBundleElement]]" = UNSET
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
        _BundleProjectCustomField_dict = super().to_dict()
        field_dict.update(_BundleProjectCustomField_dict)
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
            from ..models import state_bundle as state_bundle_m
            from ..models import state_bundle_element as state_bundle_element_m
        except ImportError:
            import sys

            state_bundle_element_m = sys.modules[__package__ + "state_bundle_element"]
            state_bundle_m = sys.modules[__package__ + "state_bundle"]

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

        state_project_custom_field = cls(
            bundle=bundle,
            default_values=default_values,
        )

        state_project_custom_field.additional_properties = d
        return state_project_custom_field

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
