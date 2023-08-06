from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectTimeTrackingSettings")


@attr.s(auto_attribs=True)
class ProjectTimeTrackingSettings:
    """Represents time tracking settings of the project."""

    enabled: "Union[Unset, bool]" = UNSET
    estimate: "Union[Unset, project_custom_field_m.ProjectCustomField]" = UNSET
    time_spent: "Union[Unset, project_custom_field_m.ProjectCustomField]" = UNSET
    work_item_types: "Union[Unset, List[work_item_type_m.WorkItemType]]" = UNSET
    project: "Union[Unset, project_m.Project]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        estimate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.estimate, Unset):
            estimate = self.estimate.to_dict()

        time_spent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_spent, Unset):
            time_spent = self.time_spent.to_dict()

        work_item_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.work_item_types, Unset):
            work_item_types = []
            for work_item_types_item_data in self.work_item_types:
                work_item_types_item = work_item_types_item_data.to_dict()

                work_item_types.append(work_item_types_item)

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if estimate is not UNSET:
            field_dict["estimate"] = estimate
        if time_spent is not UNSET:
            field_dict["timeSpent"] = time_spent
        if work_item_types is not UNSET:
            field_dict["workItemTypes"] = work_item_types
        if project is not UNSET:
            field_dict["project"] = project
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import project as project_m
            from ..models import project_custom_field as project_custom_field_m
            from ..models import work_item_type as work_item_type_m
        except ImportError:
            import sys

            project_m = sys.modules[__package__ + "project"]
            project_custom_field_m = sys.modules[__package__ + "project_custom_field"]
            work_item_type_m = sys.modules[__package__ + "work_item_type"]

        d = src_dict.copy()

        enabled = d.pop("enabled", UNSET)

        _estimate = d.pop("estimate", UNSET)
        estimate: Union[Unset, project_custom_field_m.ProjectCustomField]
        if isinstance(_estimate, Unset):
            estimate = UNSET
        else:
            estimate = project_custom_field_m.ProjectCustomField.from_dict(_estimate)

        _time_spent = d.pop("timeSpent", UNSET)
        time_spent: Union[Unset, project_custom_field_m.ProjectCustomField]
        if isinstance(_time_spent, Unset):
            time_spent = UNSET
        else:
            time_spent = project_custom_field_m.ProjectCustomField.from_dict(_time_spent)

        work_item_types = []
        _work_item_types = d.pop("workItemTypes", UNSET)
        for work_item_types_item_data in _work_item_types or []:
            work_item_types_item = work_item_type_m.WorkItemType.from_dict(work_item_types_item_data)

            work_item_types.append(work_item_types_item)

        _project = d.pop("project", UNSET)
        project: Union[Unset, project_m.Project]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = project_m.Project.from_dict(_project)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        project_time_tracking_settings = cls(
            enabled=enabled,
            estimate=estimate,
            time_spent=time_spent,
            work_item_types=work_item_types,
            project=project,
            id=id,
            type=type,
        )

        return project_time_tracking_settings
