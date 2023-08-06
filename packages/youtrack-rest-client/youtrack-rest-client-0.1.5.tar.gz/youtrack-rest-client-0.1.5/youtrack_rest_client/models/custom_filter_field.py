from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFilterField")


try:
    from ..models import filter_field
except ImportError:
    import sys

    filter_field = sys.modules[__package__ + "filter_field"]


@attr.s(auto_attribs=True)
class CustomFilterField(filter_field.FilterField):
    """Represents a custom field of the issue."""

    custom_field: "Union[Unset, custom_field_m.CustomField]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        custom_field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_field, Unset):
            custom_field = self.custom_field.to_dict()

        field_dict: Dict[str, Any] = {}
        _FilterField_dict = super().to_dict()
        field_dict.update(_FilterField_dict)
        field_dict.update({})
        if custom_field is not UNSET:
            field_dict["customField"] = custom_field

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import custom_field as custom_field_m
        except ImportError:
            import sys

            custom_field_m = sys.modules[__package__ + "custom_field"]

        d = src_dict.copy()

        _FilterField_kwargs = super().from_dict(src_dict=d).to_dict()
        _FilterField_kwargs.pop("$type")

        _custom_field = d.pop("customField", UNSET)
        custom_field: Union[Unset, custom_field_m.CustomField]
        if isinstance(_custom_field, Unset):
            custom_field = UNSET
        else:
            custom_field = custom_field_m.CustomField.from_dict(_custom_field)

        custom_filter_field = cls(
            custom_field=custom_field,
            **_FilterField_kwargs,
        )

        return custom_filter_field
