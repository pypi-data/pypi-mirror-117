from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.bundle_element import BundleElement
from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalizableBundleElement")


@attr.s(auto_attribs=True)
class LocalizableBundleElement(BundleElement):
    """Represents field value that can be localized."""

    localized_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        localized_name = self.localized_name

        field_dict: Dict[str, Any] = {}
        _BundleElement_dict = super().to_dict()
        field_dict.update(_BundleElement_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if localized_name is not UNSET:
            field_dict["localizedName"] = localized_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _BundleElement_kwargs = super().from_dict(src_dict=d).to_dict()

        localized_name = d.pop("localizedName", UNSET)

        localizable_bundle_element = cls(
            localized_name=localized_name,
            **_BundleElement_kwargs,
        )

        localizable_bundle_element.additional_properties = d
        return localizable_bundle_element

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
