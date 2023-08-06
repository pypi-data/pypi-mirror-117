from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeneralUserProfile")


@attr.s(auto_attribs=True)
class GeneralUserProfile:
    """Represents the user profile in YouTrack."""

    date_field_format: "Union[Unset, date_format_descriptor_m.DateFormatDescriptor]" = UNSET
    timezone: "Union[Unset, time_zone_descriptor_m.TimeZoneDescriptor]" = UNSET
    locale: "Union[Unset, locale_descriptor_m.LocaleDescriptor]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        date_field_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.date_field_format, Unset):
            date_field_format = self.date_field_format.to_dict()

        timezone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.timezone, Unset):
            timezone = self.timezone.to_dict()

        locale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if date_field_format is not UNSET:
            field_dict["dateFieldFormat"] = date_field_format
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if locale is not UNSET:
            field_dict["locale"] = locale
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import date_format_descriptor as date_format_descriptor_m
            from ..models import locale_descriptor as locale_descriptor_m
            from ..models import time_zone_descriptor as time_zone_descriptor_m
        except ImportError:
            import sys

            locale_descriptor_m = sys.modules[__package__ + "locale_descriptor"]
            date_format_descriptor_m = sys.modules[__package__ + "date_format_descriptor"]
            time_zone_descriptor_m = sys.modules[__package__ + "time_zone_descriptor"]

        d = src_dict.copy()

        _date_field_format = d.pop("dateFieldFormat", UNSET)
        date_field_format: Union[Unset, date_format_descriptor_m.DateFormatDescriptor]
        if isinstance(_date_field_format, Unset):
            date_field_format = UNSET
        else:
            date_field_format = date_format_descriptor_m.DateFormatDescriptor.from_dict(_date_field_format)

        _timezone = d.pop("timezone", UNSET)
        timezone: Union[Unset, time_zone_descriptor_m.TimeZoneDescriptor]
        if isinstance(_timezone, Unset):
            timezone = UNSET
        else:
            timezone = time_zone_descriptor_m.TimeZoneDescriptor.from_dict(_timezone)

        _locale = d.pop("locale", UNSET)
        locale: Union[Unset, locale_descriptor_m.LocaleDescriptor]
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = locale_descriptor_m.LocaleDescriptor.from_dict(_locale)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        general_user_profile = cls(
            date_field_format=date_field_format,
            timezone=timezone,
            locale=locale,
            id=id,
            type=type,
        )

        return general_user_profile
