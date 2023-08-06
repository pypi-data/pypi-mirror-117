from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Agile")


@attr.s(auto_attribs=True)
class Agile:
    """Represents an agile board configuration."""

    name: "Union[Unset, str]" = UNSET
    owner: "Union[Unset, user_m.User]" = UNSET
    visible_for: "Union[Unset, user_group_m.UserGroup]" = UNSET
    visible_for_project_based: "Union[Unset, bool]" = UNSET
    updateable_by: "Union[Unset, user_group_m.UserGroup]" = UNSET
    updateable_by_project_based: "Union[Unset, bool]" = UNSET
    orphans_at_the_top: "Union[Unset, bool]" = UNSET
    hide_orphans_swimlane: "Union[Unset, bool]" = UNSET
    estimation_field: "Union[Unset, custom_field_m.CustomField]" = UNSET
    original_estimation_field: "Union[Unset, custom_field_m.CustomField]" = UNSET
    projects: "Union[Unset, List[project_m.Project]]" = UNSET
    sprints: "Union[Unset, List[sprint_m.Sprint]]" = UNSET
    current_sprint: "Union[Unset, sprint_m.Sprint]" = UNSET
    column_settings: "Union[Unset, column_settings_m.ColumnSettings]" = UNSET
    swimlane_settings: "Union[Unset, swimlane_settings_m.SwimlaneSettings]" = UNSET
    sprints_settings: "Union[Unset, sprints_settings_m.SprintsSettings]" = UNSET
    color_coding: "Union[Unset, color_coding_m.ColorCoding]" = UNSET
    status: "Union[Unset, agile_status_m.AgileStatus]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        visible_for: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.visible_for, Unset):
            visible_for = self.visible_for.to_dict()

        visible_for_project_based = self.visible_for_project_based
        updateable_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updateable_by, Unset):
            updateable_by = self.updateable_by.to_dict()

        updateable_by_project_based = self.updateable_by_project_based
        orphans_at_the_top = self.orphans_at_the_top
        hide_orphans_swimlane = self.hide_orphans_swimlane
        estimation_field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.estimation_field, Unset):
            estimation_field = self.estimation_field.to_dict()

        original_estimation_field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.original_estimation_field, Unset):
            original_estimation_field = self.original_estimation_field.to_dict()

        projects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()

                projects.append(projects_item)

        sprints: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sprints, Unset):
            sprints = []
            for sprints_item_data in self.sprints:
                sprints_item = sprints_item_data.to_dict()

                sprints.append(sprints_item)

        current_sprint: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_sprint, Unset):
            current_sprint = self.current_sprint.to_dict()

        column_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.column_settings, Unset):
            column_settings = self.column_settings.to_dict()

        swimlane_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.swimlane_settings, Unset):
            swimlane_settings = self.swimlane_settings.to_dict()

        sprints_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sprints_settings, Unset):
            sprints_settings = self.sprints_settings.to_dict()

        color_coding: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color_coding, Unset):
            color_coding = self.color_coding.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if visible_for is not UNSET:
            field_dict["visibleFor"] = visible_for
        if visible_for_project_based is not UNSET:
            field_dict["visibleForProjectBased"] = visible_for_project_based
        if updateable_by is not UNSET:
            field_dict["updateableBy"] = updateable_by
        if updateable_by_project_based is not UNSET:
            field_dict["updateableByProjectBased"] = updateable_by_project_based
        if orphans_at_the_top is not UNSET:
            field_dict["orphansAtTheTop"] = orphans_at_the_top
        if hide_orphans_swimlane is not UNSET:
            field_dict["hideOrphansSwimlane"] = hide_orphans_swimlane
        if estimation_field is not UNSET:
            field_dict["estimationField"] = estimation_field
        if original_estimation_field is not UNSET:
            field_dict["originalEstimationField"] = original_estimation_field
        if projects is not UNSET:
            field_dict["projects"] = projects
        if sprints is not UNSET:
            field_dict["sprints"] = sprints
        if current_sprint is not UNSET:
            field_dict["currentSprint"] = current_sprint
        if column_settings is not UNSET:
            field_dict["columnSettings"] = column_settings
        if swimlane_settings is not UNSET:
            field_dict["swimlaneSettings"] = swimlane_settings
        if sprints_settings is not UNSET:
            field_dict["sprintsSettings"] = sprints_settings
        if color_coding is not UNSET:
            field_dict["colorCoding"] = color_coding
        if status is not UNSET:
            field_dict["status"] = status
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import agile_status as agile_status_m
            from ..models import color_coding as color_coding_m
            from ..models import column_settings as column_settings_m
            from ..models import custom_field as custom_field_m
            from ..models import project as project_m
            from ..models import sprint as sprint_m
            from ..models import sprints_settings as sprints_settings_m
            from ..models import swimlane_settings as swimlane_settings_m
            from ..models import user as user_m
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            project_m = sys.modules[__package__ + "project"]
            sprint_m = sys.modules[__package__ + "sprint"]
            user_m = sys.modules[__package__ + "user"]
            sprints_settings_m = sys.modules[__package__ + "sprints_settings"]
            user_group_m = sys.modules[__package__ + "user_group"]
            color_coding_m = sys.modules[__package__ + "color_coding"]
            agile_status_m = sys.modules[__package__ + "agile_status"]
            swimlane_settings_m = sys.modules[__package__ + "swimlane_settings"]
            column_settings_m = sys.modules[__package__ + "column_settings"]
            custom_field_m = sys.modules[__package__ + "custom_field"]

        d = src_dict.copy()

        name = d.pop("name", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, user_m.User]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = user_m.User.from_dict(_owner)

        _visible_for = d.pop("visibleFor", UNSET)
        visible_for: Union[Unset, user_group_m.UserGroup]
        if isinstance(_visible_for, Unset):
            visible_for = UNSET
        else:
            visible_for = user_group_m.UserGroup.from_dict(_visible_for)

        visible_for_project_based = d.pop("visibleForProjectBased", UNSET)

        _updateable_by = d.pop("updateableBy", UNSET)
        updateable_by: Union[Unset, user_group_m.UserGroup]
        if isinstance(_updateable_by, Unset):
            updateable_by = UNSET
        else:
            updateable_by = user_group_m.UserGroup.from_dict(_updateable_by)

        updateable_by_project_based = d.pop("updateableByProjectBased", UNSET)

        orphans_at_the_top = d.pop("orphansAtTheTop", UNSET)

        hide_orphans_swimlane = d.pop("hideOrphansSwimlane", UNSET)

        _estimation_field = d.pop("estimationField", UNSET)
        estimation_field: Union[Unset, custom_field_m.CustomField]
        if isinstance(_estimation_field, Unset):
            estimation_field = UNSET
        else:
            estimation_field = custom_field_m.CustomField.from_dict(_estimation_field)

        _original_estimation_field = d.pop("originalEstimationField", UNSET)
        original_estimation_field: Union[Unset, custom_field_m.CustomField]
        if isinstance(_original_estimation_field, Unset):
            original_estimation_field = UNSET
        else:
            original_estimation_field = custom_field_m.CustomField.from_dict(_original_estimation_field)

        projects = []
        _projects = d.pop("projects", UNSET)
        for projects_item_data in _projects or []:
            projects_item = project_m.Project.from_dict(projects_item_data)

            projects.append(projects_item)

        sprints = []
        _sprints = d.pop("sprints", UNSET)
        for sprints_item_data in _sprints or []:
            sprints_item = sprint_m.Sprint.from_dict(sprints_item_data)

            sprints.append(sprints_item)

        _current_sprint = d.pop("currentSprint", UNSET)
        current_sprint: Union[Unset, sprint_m.Sprint]
        if isinstance(_current_sprint, Unset):
            current_sprint = UNSET
        else:
            current_sprint = sprint_m.Sprint.from_dict(_current_sprint)

        _column_settings = d.pop("columnSettings", UNSET)
        column_settings: Union[Unset, column_settings_m.ColumnSettings]
        if isinstance(_column_settings, Unset):
            column_settings = UNSET
        else:
            column_settings = column_settings_m.ColumnSettings.from_dict(_column_settings)

        _swimlane_settings = d.pop("swimlaneSettings", UNSET)
        swimlane_settings: Union[Unset, swimlane_settings_m.SwimlaneSettings]
        if isinstance(_swimlane_settings, Unset):
            swimlane_settings = UNSET
        else:
            swimlane_settings = swimlane_settings_m.SwimlaneSettings.from_dict(_swimlane_settings)

        _sprints_settings = d.pop("sprintsSettings", UNSET)
        sprints_settings: Union[Unset, sprints_settings_m.SprintsSettings]
        if isinstance(_sprints_settings, Unset):
            sprints_settings = UNSET
        else:
            sprints_settings = sprints_settings_m.SprintsSettings.from_dict(_sprints_settings)

        _color_coding = d.pop("colorCoding", UNSET)
        color_coding: Union[Unset, color_coding_m.ColorCoding]
        if isinstance(_color_coding, Unset):
            color_coding = UNSET
        else:
            color_coding = color_coding_m.ColorCoding.from_dict(_color_coding)

        _status = d.pop("status", UNSET)
        status: Union[Unset, agile_status_m.AgileStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = agile_status_m.AgileStatus.from_dict(_status)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        agile = cls(
            name=name,
            owner=owner,
            visible_for=visible_for,
            visible_for_project_based=visible_for_project_based,
            updateable_by=updateable_by,
            updateable_by_project_based=updateable_by_project_based,
            orphans_at_the_top=orphans_at_the_top,
            hide_orphans_swimlane=hide_orphans_swimlane,
            estimation_field=estimation_field,
            original_estimation_field=original_estimation_field,
            projects=projects,
            sprints=sprints,
            current_sprint=current_sprint,
            column_settings=column_settings,
            swimlane_settings=swimlane_settings,
            sprints_settings=sprints_settings,
            color_coding=color_coding,
            status=status,
            id=id,
            type=type,
        )

        return agile
