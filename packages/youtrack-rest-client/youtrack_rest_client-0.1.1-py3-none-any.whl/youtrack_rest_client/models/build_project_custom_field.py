from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.build_bundle import BuildBundle
    from ..models.build_bundle_element import BuildBundleElement
else:
    BuildBundle = "BuildBundle"
    BuildBundleElement = "BuildBundleElement"

from ..models.bundle_project_custom_field import BundleProjectCustomField

T = TypeVar("T", bound="BuildProjectCustomField")


@attr.s(auto_attribs=True)
class BuildProjectCustomField(BundleProjectCustomField):
    """Represents project settings for the build field."""

    bundle: Union[Unset, BuildBundle] = UNSET
    default_values: Union[Unset, List[BuildBundleElement]] = UNSET
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
        d = src_dict.copy()

        _BundleProjectCustomField_kwargs = super().from_dict(src_dict=d).to_dict()

        _bundle = d.pop("bundle", UNSET)
        bundle: Union[Unset, BuildBundle]
        if isinstance(_bundle, Unset):
            bundle = UNSET
        else:
            bundle = BuildBundle.from_dict(_bundle)

        default_values = []
        _default_values = d.pop("defaultValues", UNSET)
        for default_values_item_data in _default_values or []:
            default_values_item = BuildBundleElement.from_dict(default_values_item_data)

            default_values.append(default_values_item)

        build_project_custom_field = cls(
            bundle=bundle,
            default_values=default_values,
            **_BundleProjectCustomField_kwargs,
        )

        build_project_custom_field.additional_properties = d
        return build_project_custom_field

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
