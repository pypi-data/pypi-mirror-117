from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.version_bundle import VersionBundle
    from ..models.version_bundle_element import VersionBundleElement
else:
    VersionBundleElement = "VersionBundleElement"
    VersionBundle = "VersionBundle"

from ..models.bundle_project_custom_field import BundleProjectCustomField

T = TypeVar("T", bound="VersionProjectCustomField")


@attr.s(auto_attribs=True)
class VersionProjectCustomField(BundleProjectCustomField):
    """Represents project settings for the version field."""

    bundle: Union[Unset, VersionBundle] = UNSET
    default_values: Union[Unset, List[VersionBundleElement]] = UNSET
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
        bundle: Union[Unset, VersionBundle]
        if isinstance(_bundle, Unset):
            bundle = UNSET
        else:
            bundle = VersionBundle.from_dict(_bundle)

        default_values = []
        _default_values = d.pop("defaultValues", UNSET)
        for default_values_item_data in _default_values or []:
            default_values_item = VersionBundleElement.from_dict(default_values_item_data)

            default_values.append(default_values_item)

        version_project_custom_field = cls(
            bundle=bundle,
            default_values=default_values,
            **_BundleProjectCustomField_kwargs,
        )

        version_project_custom_field.additional_properties = d
        return version_project_custom_field

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
