from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field import CustomField
else:
    CustomField = "CustomField"

from ..models.filter_field import FilterField

T = TypeVar("T", bound="CustomFilterField")


@attr.s(auto_attribs=True)
class CustomFilterField(FilterField):
    """Represents a custom field of the issue."""

    custom_field: Union[Unset, CustomField] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_field, Unset):
            custom_field = self.custom_field.to_dict()

        field_dict: Dict[str, Any] = {}
        _FilterField_dict = super().to_dict()
        field_dict.update(_FilterField_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_field is not UNSET:
            field_dict["customField"] = custom_field

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _FilterField_kwargs = super().from_dict(src_dict=d).to_dict()

        _custom_field = d.pop("customField", UNSET)
        custom_field: Union[Unset, CustomField]
        if isinstance(_custom_field, Unset):
            custom_field = UNSET
        else:
            custom_field = CustomField.from_dict(_custom_field)

        custom_filter_field = cls(
            custom_field=custom_field,
            **_FilterField_kwargs,
        )

        custom_filter_field.additional_properties = d
        return custom_filter_field

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
