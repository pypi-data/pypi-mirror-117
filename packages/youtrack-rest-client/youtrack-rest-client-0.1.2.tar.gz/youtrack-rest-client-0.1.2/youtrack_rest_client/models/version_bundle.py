from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VersionBundle")


try:
    from ..models import base_bundle
except ImportError:
    import sys

    base_bundle = sys.modules[__package__ + "base_bundle"]


@attr.s(auto_attribs=True)
class VersionBundle(base_bundle.BaseBundle):
    """Represents a set of versions in YouTrack."""

    values: "Union[Unset, List[version_bundle_element_m.VersionBundleElement]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()

                values.append(values_item)

        field_dict: Dict[str, Any] = {}
        _BaseBundle_dict = super().to_dict()
        field_dict.update(_BaseBundle_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import version_bundle_element as version_bundle_element_m
        except ImportError:
            import sys

            version_bundle_element_m = sys.modules[__package__ + "version_bundle_element"]

        d = src_dict.copy()

        _BaseBundle_kwargs = super().from_dict(src_dict=d).to_dict()

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = version_bundle_element_m.VersionBundleElement.from_dict(values_item_data)

            values.append(values_item)

        version_bundle = cls(
            values=values,
            **_BaseBundle_kwargs,
        )

        version_bundle.additional_properties = d
        return version_bundle

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
