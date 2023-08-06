from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeTrackingUserProfile")


@attr.s(auto_attribs=True)
class TimeTrackingUserProfile:
    """Represents time tracking settings in the user's profile."""

    period_format: "Union[Unset, period_field_format_m.PeriodFieldFormat]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        period_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period_format, Unset):
            period_format = self.period_format.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
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

        try:
            from ..models import period_field_format as period_field_format_m
        except ImportError:
            import sys

            period_field_format_m = sys.modules[__package__ + "period_field_format"]

        d = src_dict.copy()

        _period_format = d.pop("periodFormat", UNSET)
        period_format: Union[Unset, period_field_format_m.PeriodFieldFormat]
        if isinstance(_period_format, Unset):
            period_format = UNSET
        else:
            period_format = period_field_format_m.PeriodFieldFormat.from_dict(_period_format)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        time_tracking_user_profile = cls(
            period_format=period_format,
            id=id,
            type=type,
        )

        return time_tracking_user_profile
