from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalSettings")


@attr.s(auto_attribs=True)
class GlobalSettings:
    """Represents application-wide settings."""

    system_settings: "Union[Unset, system_settings_m.SystemSettings]" = UNSET
    notification_settings: "Union[Unset, notification_settings_m.NotificationSettings]" = UNSET
    rest_settings: "Union[Unset, rest_cors_settings_m.RestCorsSettings]" = UNSET
    appearance_settings: "Union[Unset, appearance_settings_m.AppearanceSettings]" = UNSET
    locale_settings: "Union[Unset, locale_settings_m.LocaleSettings]" = UNSET
    license_: "Union[Unset, license__m.License]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        system_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.system_settings, Unset):
            system_settings = self.system_settings.to_dict()

        notification_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notification_settings, Unset):
            notification_settings = self.notification_settings.to_dict()

        rest_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rest_settings, Unset):
            rest_settings = self.rest_settings.to_dict()

        appearance_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appearance_settings, Unset):
            appearance_settings = self.appearance_settings.to_dict()

        locale_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.locale_settings, Unset):
            locale_settings = self.locale_settings.to_dict()

        license_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if system_settings is not UNSET:
            field_dict["systemSettings"] = system_settings
        if notification_settings is not UNSET:
            field_dict["notificationSettings"] = notification_settings
        if rest_settings is not UNSET:
            field_dict["restSettings"] = rest_settings
        if appearance_settings is not UNSET:
            field_dict["appearanceSettings"] = appearance_settings
        if locale_settings is not UNSET:
            field_dict["localeSettings"] = locale_settings
        if license_ is not UNSET:
            field_dict["license"] = license_
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import appearance_settings as appearance_settings_m
            from ..models import license_ as license__m
            from ..models import locale_settings as locale_settings_m
            from ..models import notification_settings as notification_settings_m
            from ..models import rest_cors_settings as rest_cors_settings_m
            from ..models import system_settings as system_settings_m
        except ImportError:
            import sys

            notification_settings_m = sys.modules[__package__ + "notification_settings"]
            system_settings_m = sys.modules[__package__ + "system_settings"]
            rest_cors_settings_m = sys.modules[__package__ + "rest_cors_settings"]
            locale_settings_m = sys.modules[__package__ + "locale_settings"]
            license__m = sys.modules[__package__ + "license_"]
            appearance_settings_m = sys.modules[__package__ + "appearance_settings"]

        d = src_dict.copy()

        _system_settings = d.pop("systemSettings", UNSET)
        system_settings: Union[Unset, system_settings_m.SystemSettings]
        if isinstance(_system_settings, Unset):
            system_settings = UNSET
        else:
            system_settings = system_settings_m.SystemSettings.from_dict(_system_settings)

        _notification_settings = d.pop("notificationSettings", UNSET)
        notification_settings: Union[Unset, notification_settings_m.NotificationSettings]
        if isinstance(_notification_settings, Unset):
            notification_settings = UNSET
        else:
            notification_settings = notification_settings_m.NotificationSettings.from_dict(_notification_settings)

        _rest_settings = d.pop("restSettings", UNSET)
        rest_settings: Union[Unset, rest_cors_settings_m.RestCorsSettings]
        if isinstance(_rest_settings, Unset):
            rest_settings = UNSET
        else:
            rest_settings = rest_cors_settings_m.RestCorsSettings.from_dict(_rest_settings)

        _appearance_settings = d.pop("appearanceSettings", UNSET)
        appearance_settings: Union[Unset, appearance_settings_m.AppearanceSettings]
        if isinstance(_appearance_settings, Unset):
            appearance_settings = UNSET
        else:
            appearance_settings = appearance_settings_m.AppearanceSettings.from_dict(_appearance_settings)

        _locale_settings = d.pop("localeSettings", UNSET)
        locale_settings: Union[Unset, locale_settings_m.LocaleSettings]
        if isinstance(_locale_settings, Unset):
            locale_settings = UNSET
        else:
            locale_settings = locale_settings_m.LocaleSettings.from_dict(_locale_settings)

        _license_ = d.pop("license", UNSET)
        license_: Union[Unset, license__m.License]
        if isinstance(_license_, Unset):
            license_ = UNSET
        else:
            license_ = license__m.License.from_dict(_license_)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        global_settings = cls(
            system_settings=system_settings,
            notification_settings=notification_settings,
            rest_settings=rest_settings,
            appearance_settings=appearance_settings,
            locale_settings=locale_settings,
            license_=license_,
            id=id,
            type=type,
        )

        return global_settings
