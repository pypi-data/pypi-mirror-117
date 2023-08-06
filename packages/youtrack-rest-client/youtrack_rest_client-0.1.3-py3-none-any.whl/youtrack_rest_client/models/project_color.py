from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectColor")


@attr.s(auto_attribs=True)
class ProjectColor:
    """Represents color setting for one project on the board."""

    project: "Union[Unset, project_m.Project]" = UNSET
    color: "Union[Unset, field_style_m.FieldStyle]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        color: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project is not UNSET:
            field_dict["project"] = project
        if color is not UNSET:
            field_dict["color"] = color
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import field_style as field_style_m
            from ..models import project as project_m
        except ImportError:
            import sys

            project_m = sys.modules[__package__ + "project"]
            field_style_m = sys.modules[__package__ + "field_style"]

        d = src_dict.copy()

        _project = d.pop("project", UNSET)
        project: Union[Unset, project_m.Project]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = project_m.Project.from_dict(_project)

        _color = d.pop("color", UNSET)
        color: Union[Unset, field_style_m.FieldStyle]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = field_style_m.FieldStyle.from_dict(_color)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        project_color = cls(
            project=project,
            color=color,
            id=id,
            type=type,
        )

        project_color.additional_properties = d
        return project_color

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
