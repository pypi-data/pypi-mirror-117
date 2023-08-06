from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeZoneDescriptor")


@attr.s(auto_attribs=True)
class TimeZoneDescriptor:
    """Represents a time zone."""

    presentation: Union[Unset, str] = UNSET
    offset: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        presentation = self.presentation
        offset = self.offset
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if presentation is not UNSET:
            field_dict["presentation"] = presentation
        if offset is not UNSET:
            field_dict["offset"] = offset
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        presentation = d.pop("presentation", UNSET)

        offset = d.pop("offset", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        time_zone_descriptor = cls(
            presentation=presentation,
            offset=offset,
            id=id,
            type=type,
        )

        time_zone_descriptor.additional_properties = d
        return time_zone_descriptor

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
