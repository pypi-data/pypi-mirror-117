from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttributeBasedSwimlaneSettings")


try:
    from ..models import swimlane_settings
except ImportError:
    import sys

    swimlane_settings = sys.modules[__package__ + "swimlane_settings"]


@attr.s(auto_attribs=True)
class AttributeBasedSwimlaneSettings(swimlane_settings.SwimlaneSettings):
    """ """

    field: "Union[Unset, filter_field_m.FilterField]" = UNSET
    values: "Union[Unset, List[swimlane_entity_attribute_value_m.SwimlaneEntityAttributeValue]]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.to_dict()

        values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()

                values.append(values_item)

        field_dict: Dict[str, Any] = {}
        _SwimlaneSettings_dict = super().to_dict()
        field_dict.update(_SwimlaneSettings_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import filter_field as filter_field_m
            from ..models import swimlane_entity_attribute_value as swimlane_entity_attribute_value_m
        except ImportError:
            import sys

            swimlane_entity_attribute_value_m = sys.modules[__package__ + "swimlane_entity_attribute_value"]
            filter_field_m = sys.modules[__package__ + "filter_field"]

        d = src_dict.copy()

        _field = d.pop("field", UNSET)
        field: Union[Unset, filter_field_m.FilterField]
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = filter_field_m.FilterField.from_dict(_field)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = swimlane_entity_attribute_value_m.SwimlaneEntityAttributeValue.from_dict(values_item_data)

            values.append(values_item)

        attribute_based_swimlane_settings = cls(
            field=field,
            values=values,
        )

        attribute_based_swimlane_settings.additional_properties = d
        return attribute_based_swimlane_settings

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
