from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProfiles")


@attr.s(auto_attribs=True)
class UserProfiles:
    """ """

    general: "Union[Unset, general_user_profile_m.GeneralUserProfile]" = UNSET
    notifications: "Union[Unset, notifications_user_profile_m.NotificationsUserProfile]" = UNSET
    timetracking: "Union[Unset, time_tracking_user_profile_m.TimeTrackingUserProfile]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        general: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.general, Unset):
            general = self.general.to_dict()

        notifications: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = self.notifications.to_dict()

        timetracking: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.timetracking, Unset):
            timetracking = self.timetracking.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if general is not UNSET:
            field_dict["general"] = general
        if notifications is not UNSET:
            field_dict["notifications"] = notifications
        if timetracking is not UNSET:
            field_dict["timetracking"] = timetracking
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import general_user_profile as general_user_profile_m
            from ..models import notifications_user_profile as notifications_user_profile_m
            from ..models import time_tracking_user_profile as time_tracking_user_profile_m
        except ImportError:
            import sys

            general_user_profile_m = sys.modules[__package__ + "general_user_profile"]
            time_tracking_user_profile_m = sys.modules[__package__ + "time_tracking_user_profile"]
            notifications_user_profile_m = sys.modules[__package__ + "notifications_user_profile"]

        d = src_dict.copy()

        _general = d.pop("general", UNSET)
        general: Union[Unset, general_user_profile_m.GeneralUserProfile]
        if isinstance(_general, Unset):
            general = UNSET
        else:
            general = general_user_profile_m.GeneralUserProfile.from_dict(_general)

        _notifications = d.pop("notifications", UNSET)
        notifications: Union[Unset, notifications_user_profile_m.NotificationsUserProfile]
        if isinstance(_notifications, Unset):
            notifications = UNSET
        else:
            notifications = notifications_user_profile_m.NotificationsUserProfile.from_dict(_notifications)

        _timetracking = d.pop("timetracking", UNSET)
        timetracking: Union[Unset, time_tracking_user_profile_m.TimeTrackingUserProfile]
        if isinstance(_timetracking, Unset):
            timetracking = UNSET
        else:
            timetracking = time_tracking_user_profile_m.TimeTrackingUserProfile.from_dict(_timetracking)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        user_profiles = cls(
            general=general,
            notifications=notifications,
            timetracking=timetracking,
            id=id,
            type=type,
        )

        user_profiles.additional_properties = d
        return user_profiles

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
