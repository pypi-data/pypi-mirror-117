from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.visibility import Visibility

T = TypeVar("T", bound="UnlimitedVisibility")


@attr.s(auto_attribs=True)
class UnlimitedVisibility(Visibility):
    """Represents unlimited visibility."""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _Visibility_dict = super().to_dict()
        field_dict.update(_Visibility_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Visibility_kwargs = super().from_dict(src_dict=d).to_dict()

        unlimited_visibility = cls(
            **_Visibility_kwargs,
        )

        unlimited_visibility.additional_properties = d
        return unlimited_visibility

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
