from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeriodValue")


@attr.s(auto_attribs=True)
class PeriodValue:
    """Represents the period field value."""

    minutes: Union[Unset, int] = UNSET
    presentation: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        minutes = self.minutes
        presentation = self.presentation
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if presentation is not UNSET:
            field_dict["presentation"] = presentation
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        minutes = d.pop("minutes", UNSET)

        presentation = d.pop("presentation", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        period_value = cls(
            minutes=minutes,
            presentation=presentation,
            id=id,
            type=type,
        )

        period_value.additional_properties = d
        return period_value

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
