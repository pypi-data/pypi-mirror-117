from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.localizable_bundle_element import LocalizableBundleElement
from ..types import UNSET, Unset

T = TypeVar("T", bound="StateBundleElement")


@attr.s(auto_attribs=True)
class StateBundleElement(LocalizableBundleElement):
    """Represents the state of an issue in YouTrack."""

    is_resolved: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_resolved = self.is_resolved

        field_dict: Dict[str, Any] = {}
        _LocalizableBundleElement_dict = super().to_dict()
        field_dict.update(_LocalizableBundleElement_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_resolved is not UNSET:
            field_dict["isResolved"] = is_resolved

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _LocalizableBundleElement_kwargs = super().from_dict(src_dict=d).to_dict()

        is_resolved = d.pop("isResolved", UNSET)

        state_bundle_element = cls(
            is_resolved=is_resolved,
            **_LocalizableBundleElement_kwargs,
        )

        state_bundle_element.additional_properties = d
        return state_bundle_element

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
