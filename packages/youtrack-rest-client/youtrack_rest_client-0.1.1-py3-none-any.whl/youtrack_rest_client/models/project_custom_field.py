from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field import CustomField
    from ..models.project import Project
else:
    Project = "Project"
    CustomField = "CustomField"


T = TypeVar("T", bound="ProjectCustomField")


@attr.s(auto_attribs=True)
class ProjectCustomField:
    """Represents custom field settings for the particular project."""

    field: Union[Unset, CustomField] = UNSET
    project: Union[Unset, Project] = UNSET
    can_be_empty: Union[Unset, bool] = UNSET
    empty_field_text: Union[Unset, str] = UNSET
    ordinal: Union[Unset, int] = UNSET
    is_public: Union[Unset, bool] = UNSET
    has_running_job: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        can_be_empty = self.can_be_empty
        empty_field_text = self.empty_field_text
        ordinal = self.ordinal
        is_public = self.is_public
        has_running_job = self.has_running_job
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if project is not UNSET:
            field_dict["project"] = project
        if can_be_empty is not UNSET:
            field_dict["canBeEmpty"] = can_be_empty
        if empty_field_text is not UNSET:
            field_dict["emptyFieldText"] = empty_field_text
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if has_running_job is not UNSET:
            field_dict["hasRunningJob"] = has_running_job
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _field = d.pop("field", UNSET)
        field: Union[Unset, CustomField]
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = CustomField.from_dict(_field)

        _project = d.pop("project", UNSET)
        project: Union[Unset, Project]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)

        can_be_empty = d.pop("canBeEmpty", UNSET)

        empty_field_text = d.pop("emptyFieldText", UNSET)

        ordinal = d.pop("ordinal", UNSET)

        is_public = d.pop("isPublic", UNSET)

        has_running_job = d.pop("hasRunningJob", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        project_custom_field = cls(
            field=field,
            project=project,
            can_be_empty=can_be_empty,
            empty_field_text=empty_field_text,
            ordinal=ordinal,
            is_public=is_public,
            has_running_job=has_running_job,
            id=id,
            type=type,
        )

        project_custom_field.additional_properties = d
        return project_custom_field

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
