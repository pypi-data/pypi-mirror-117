from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.work_item_type import WorkItemType
    from ..models.work_time_settings import WorkTimeSettings
else:
    WorkTimeSettings = "WorkTimeSettings"
    WorkItemType = "WorkItemType"


T = TypeVar("T", bound="GlobalTimeTrackingSettings")


@attr.s(auto_attribs=True)
class GlobalTimeTrackingSettings:
    """Represents time tracking settings of your server."""

    work_item_types: Union[Unset, List[WorkItemType]] = UNSET
    work_time_settings: Union[Unset, WorkTimeSettings] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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
        d = src_dict.copy()

        work_item_types = []
        _work_item_types = d.pop("workItemTypes", UNSET)
        for work_item_types_item_data in _work_item_types or []:
            work_item_types_item = WorkItemType.from_dict(work_item_types_item_data)

            work_item_types.append(work_item_types_item)

        _work_time_settings = d.pop("workTimeSettings", UNSET)
        work_time_settings: Union[Unset, WorkTimeSettings]
        if isinstance(_work_time_settings, Unset):
            work_time_settings = UNSET
        else:
            work_time_settings = WorkTimeSettings.from_dict(_work_time_settings)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        global_time_tracking_settings = cls(
            work_item_types=work_item_types,
            work_time_settings=work_time_settings,
            id=id,
            type=type,
        )

        global_time_tracking_settings.additional_properties = d
        return global_time_tracking_settings

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
