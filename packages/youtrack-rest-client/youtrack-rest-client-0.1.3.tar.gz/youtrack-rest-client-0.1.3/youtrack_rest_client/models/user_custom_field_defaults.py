from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserCustomFieldDefaults")


try:
    from ..models import custom_field_defaults
except ImportError:
    import sys

    custom_field_defaults = sys.modules[__package__ + "custom_field_defaults"]


@attr.s(auto_attribs=True)
class UserCustomFieldDefaults(custom_field_defaults.CustomFieldDefaults):
    """Represents default settings for the user-type field."""

    bundle: "Union[Unset, user_bundle_m.UserBundle]" = UNSET
    default_values: "Union[Unset, List[user_m.User]]" = UNSET
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
        _CustomFieldDefaults_dict = super().to_dict()
        field_dict.update(_CustomFieldDefaults_dict)
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
            from ..models import user as user_m
            from ..models import user_bundle as user_bundle_m
        except ImportError:
            import sys

            user_m = sys.modules[__package__ + "user"]
            user_bundle_m = sys.modules[__package__ + "user_bundle"]

        d = src_dict.copy()

        _bundle = d.pop("bundle", UNSET)
        bundle: Union[Unset, user_bundle_m.UserBundle]
        if isinstance(_bundle, Unset):
            bundle = UNSET
        else:
            bundle = user_bundle_m.UserBundle.from_dict(_bundle)

        default_values = []
        _default_values = d.pop("defaultValues", UNSET)
        for default_values_item_data in _default_values or []:
            default_values_item = user_m.User.from_dict(default_values_item_data)

            default_values.append(default_values_item)

        user_custom_field_defaults = cls(
            bundle=bundle,
            default_values=default_values,
        )

        user_custom_field_defaults.additional_properties = d
        return user_custom_field_defaults

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
