from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuildBundleElement")


try:
    from ..models import bundle_element
except ImportError:
    import sys

    bundle_element = sys.modules[__package__ + "bundle_element"]


@attr.s(auto_attribs=True)
class BuildBundleElement(bundle_element.BundleElement):
    """Represents a build - a single element of a builds bundle."""

    assemble_date: "Union[Unset, int]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assemble_date = self.assemble_date

        field_dict: Dict[str, Any] = {}
        _BundleElement_dict = super().to_dict()
        field_dict.update(_BundleElement_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assemble_date is not UNSET:
            field_dict["assembleDate"] = assemble_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        assemble_date = d.pop("assembleDate", UNSET)

        build_bundle_element = cls(
            assemble_date=assemble_date,
        )

        build_bundle_element.additional_properties = d
        return build_bundle_element

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
