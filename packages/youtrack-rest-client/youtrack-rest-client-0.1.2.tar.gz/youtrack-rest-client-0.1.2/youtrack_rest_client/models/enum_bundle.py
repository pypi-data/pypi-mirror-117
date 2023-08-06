from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnumBundle")


try:
    from ..models import base_bundle
except ImportError:
    import sys

    base_bundle = sys.modules[__package__ + "base_bundle"]


@attr.s(auto_attribs=True)
class EnumBundle(base_bundle.BaseBundle):
    """Represents a set of values of the enumeration type in YouTrack."""

    values: "Union[Unset, List[enum_bundle_element_m.EnumBundleElement]]" = UNSET
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
            from ..models import enum_bundle_element as enum_bundle_element_m
        except ImportError:
            import sys

            enum_bundle_element_m = sys.modules[__package__ + "enum_bundle_element"]

        d = src_dict.copy()

        _BaseBundle_kwargs = super().from_dict(src_dict=d).to_dict()

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = enum_bundle_element_m.EnumBundleElement.from_dict(values_item_data)

            values.append(values_item)

        enum_bundle = cls(
            values=values,
            **_BaseBundle_kwargs,
        )

        enum_bundle.additional_properties = d
        return enum_bundle

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
