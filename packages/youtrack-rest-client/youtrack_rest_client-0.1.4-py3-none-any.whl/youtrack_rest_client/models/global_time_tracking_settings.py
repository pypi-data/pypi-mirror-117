from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalTimeTrackingSettings")


@attr.s(auto_attribs=True)
class GlobalTimeTrackingSettings:
    """Represents time tracking settings of your server."""

    work_item_types: "Union[Unset, List[work_item_type_m.WorkItemType]]" = UNSET
    work_time_settings: "Union[Unset, work_time_settings_m.WorkTimeSettings]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        work_item_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.work_item_types, Unset):
            work_item_types = []
            for work_item_types_item_data in self.work_item_types:
                work_item_types_item = work_item_types_item_data.to_dict()

                work_item_types.append(work_item_types_item)

        work_time_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.work_time_settings, Unset):
            work_time_settings = self.work_time_settings.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if work_item_types is not UNSET:
            field_dict["workItemTypes"] = work_item_types
        if work_time_settings is not UNSET:
            field_dict["workTimeSettings"] = work_time_settings
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import work_item_type as work_item_type_m
            from ..models import work_time_settings as work_time_settings_m
        except ImportError:
            import sys

            work_item_type_m = sys.modules[__package__ + "work_item_type"]
            work_time_settings_m = sys.modules[__package__ + "work_time_settings"]

        d = src_dict.copy()

        work_item_types = []
        _work_item_types = d.pop("workItemTypes", UNSET)
        for work_item_types_item_data in _work_item_types or []:
            work_item_types_item = work_item_type_m.WorkItemType.from_dict(work_item_types_item_data)

            work_item_types.append(work_item_types_item)

        _work_time_settings = d.pop("workTimeSettings", UNSET)
        work_time_settings: Union[Unset, work_time_settings_m.WorkTimeSettings]
        if isinstance(_work_time_settings, Unset):
            work_time_settings = UNSET
        else:
            work_time_settings = work_time_settings_m.WorkTimeSettings.from_dict(_work_time_settings)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        global_time_tracking_settings = cls(
            work_item_types=work_item_types,
            work_time_settings=work_time_settings,
            id=id,
            type=type,
        )

        return global_time_tracking_settings
