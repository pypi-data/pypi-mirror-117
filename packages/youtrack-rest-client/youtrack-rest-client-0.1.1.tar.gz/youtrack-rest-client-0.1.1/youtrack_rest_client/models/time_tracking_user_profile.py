from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.period_field_format import PeriodFieldFormat
else:
    PeriodFieldFormat = "PeriodFieldFormat"


T = TypeVar("T", bound="TimeTrackingUserProfile")


@attr.s(auto_attribs=True)
class TimeTrackingUserProfile:
    """Represents time tracking settings in the user's profile."""

    period_format: Union[Unset, PeriodFieldFormat] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period_format, Unset):
            period_format = self.period_format.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period_format is not UNSET:
            field_dict["periodFormat"] = period_format
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _period_format = d.pop("periodFormat", UNSET)
        period_format: Union[Unset, PeriodFieldFormat]
        if isinstance(_period_format, Unset):
            period_format = UNSET
        else:
            period_format = PeriodFieldFormat.from_dict(_period_format)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        time_tracking_user_profile = cls(
            period_format=period_format,
            id=id,
            type=type,
        )

        time_tracking_user_profile.additional_properties = d
        return time_tracking_user_profile

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
