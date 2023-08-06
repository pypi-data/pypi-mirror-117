from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_field import FilterField
    from ..models.swimlane_value import SwimlaneValue
else:
    FilterField = "FilterField"
    SwimlaneValue = "SwimlaneValue"

from ..models.swimlane_settings import SwimlaneSettings

T = TypeVar("T", bound="IssueBasedSwimlaneSettings")


@attr.s(auto_attribs=True)
class IssueBasedSwimlaneSettings(SwimlaneSettings):
    """Swimlane settings for the case, when each swimlane is represented by an issue and contains this issue's subtasks."""

    field: Union[Unset, FilterField] = UNSET
    default_card_type: Union[Unset, SwimlaneValue] = UNSET
    values: Union[Unset, List[SwimlaneValue]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.to_dict()

        default_card_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_card_type, Unset):
            default_card_type = self.default_card_type.to_dict()

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
        if default_card_type is not UNSET:
            field_dict["defaultCardType"] = default_card_type
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _SwimlaneSettings_kwargs = super().from_dict(src_dict=d).to_dict()

        _field = d.pop("field", UNSET)
        field: Union[Unset, FilterField]
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = FilterField.from_dict(_field)

        _default_card_type = d.pop("defaultCardType", UNSET)
        default_card_type: Union[Unset, SwimlaneValue]
        if isinstance(_default_card_type, Unset):
            default_card_type = UNSET
        else:
            default_card_type = SwimlaneValue.from_dict(_default_card_type)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = SwimlaneValue.from_dict(values_item_data)

            values.append(values_item)

        issue_based_swimlane_settings = cls(
            field=field,
            default_card_type=default_card_type,
            values=values,
            **_SwimlaneSettings_kwargs,
        )

        issue_based_swimlane_settings.additional_properties = d
        return issue_based_swimlane_settings

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
