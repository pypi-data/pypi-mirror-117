from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldBasedColorCoding")


try:
    from ..models import color_coding
except ImportError:
    import sys

    color_coding = sys.modules[__package__ + "color_coding"]


@attr.s(auto_attribs=True)
class FieldBasedColorCoding(color_coding.ColorCoding):
    """Sets a card color based on a value of some custom field."""

    prototype: "Union[Unset, custom_field_m.CustomField]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prototype: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prototype, Unset):
            prototype = self.prototype.to_dict()

        field_dict: Dict[str, Any] = {}
        _ColorCoding_dict = super().to_dict()
        field_dict.update(_ColorCoding_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prototype is not UNSET:
            field_dict["prototype"] = prototype

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import custom_field as custom_field_m
        except ImportError:
            import sys

            custom_field_m = sys.modules[__package__ + "custom_field"]

        d = src_dict.copy()

        _ColorCoding_kwargs = super().from_dict(src_dict=d).to_dict()

        _prototype = d.pop("prototype", UNSET)
        prototype: Union[Unset, custom_field_m.CustomField]
        if isinstance(_prototype, Unset):
            prototype = UNSET
        else:
            prototype = custom_field_m.CustomField.from_dict(_prototype)

        field_based_color_coding = cls(
            prototype=prototype,
            **_ColorCoding_kwargs,
        )

        field_based_color_coding.additional_properties = d
        return field_based_color_coding

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
