from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomField")


@attr.s(auto_attribs=True)
class CustomField:
    """Represents a custom field in YouTrack."""

    name: "Union[Unset, str]" = UNSET
    localized_name: "Union[Unset, str]" = UNSET
    field_type: "Union[Unset, field_type_m.FieldType]" = UNSET
    is_auto_attached: "Union[Unset, bool]" = UNSET
    is_displayed_in_issue_list: "Union[Unset, bool]" = UNSET
    ordinal: "Union[Unset, int]" = UNSET
    aliases: "Union[Unset, str]" = UNSET
    field_defaults: "Union[Unset, custom_field_defaults_m.CustomFieldDefaults]" = UNSET
    has_running_job: "Union[Unset, bool]" = UNSET
    is_updateable: "Union[Unset, bool]" = UNSET
    instances: "Union[Unset, List[project_custom_field_m.ProjectCustomField]]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        localized_name = self.localized_name
        field_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.to_dict()

        is_auto_attached = self.is_auto_attached
        is_displayed_in_issue_list = self.is_displayed_in_issue_list
        ordinal = self.ordinal
        aliases = self.aliases
        field_defaults: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_defaults, Unset):
            field_defaults = self.field_defaults.to_dict()

        has_running_job = self.has_running_job
        is_updateable = self.is_updateable
        instances: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for instances_item_data in self.instances:
                instances_item = instances_item_data.to_dict()

                instances.append(instances_item)

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if localized_name is not UNSET:
            field_dict["localizedName"] = localized_name
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type
        if is_auto_attached is not UNSET:
            field_dict["isAutoAttached"] = is_auto_attached
        if is_displayed_in_issue_list is not UNSET:
            field_dict["isDisplayedInIssueList"] = is_displayed_in_issue_list
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if field_defaults is not UNSET:
            field_dict["fieldDefaults"] = field_defaults
        if has_running_job is not UNSET:
            field_dict["hasRunningJob"] = has_running_job
        if is_updateable is not UNSET:
            field_dict["isUpdateable"] = is_updateable
        if instances is not UNSET:
            field_dict["instances"] = instances
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import custom_field_defaults as custom_field_defaults_m
            from ..models import field_type as field_type_m
            from ..models import project_custom_field as project_custom_field_m
        except ImportError:
            import sys

            project_custom_field_m = sys.modules[__package__ + "project_custom_field"]
            field_type_m = sys.modules[__package__ + "field_type"]
            custom_field_defaults_m = sys.modules[__package__ + "custom_field_defaults"]

        d = src_dict.copy()

        name = d.pop("name", UNSET)

        localized_name = d.pop("localizedName", UNSET)

        _field_type = d.pop("fieldType", UNSET)
        field_type: Union[Unset, field_type_m.FieldType]
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = field_type_m.FieldType.from_dict(_field_type)

        is_auto_attached = d.pop("isAutoAttached", UNSET)

        is_displayed_in_issue_list = d.pop("isDisplayedInIssueList", UNSET)

        ordinal = d.pop("ordinal", UNSET)

        aliases = d.pop("aliases", UNSET)

        _field_defaults = d.pop("fieldDefaults", UNSET)
        field_defaults: Union[Unset, custom_field_defaults_m.CustomFieldDefaults]
        if isinstance(_field_defaults, Unset):
            field_defaults = UNSET
        else:
            field_defaults = custom_field_defaults_m.CustomFieldDefaults.from_dict(_field_defaults)

        has_running_job = d.pop("hasRunningJob", UNSET)

        is_updateable = d.pop("isUpdateable", UNSET)

        instances = []
        _instances = d.pop("instances", UNSET)
        for instances_item_data in _instances or []:
            instances_item = project_custom_field_m.ProjectCustomField.from_dict(instances_item_data)

            instances.append(instances_item)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        custom_field = cls(
            name=name,
            localized_name=localized_name,
            field_type=field_type,
            is_auto_attached=is_auto_attached,
            is_displayed_in_issue_list=is_displayed_in_issue_list,
            ordinal=ordinal,
            aliases=aliases,
            field_defaults=field_defaults,
            has_running_job=has_running_job,
            is_updateable=is_updateable,
            instances=instances,
            id=id,
            type=type,
        )

        return custom_field
