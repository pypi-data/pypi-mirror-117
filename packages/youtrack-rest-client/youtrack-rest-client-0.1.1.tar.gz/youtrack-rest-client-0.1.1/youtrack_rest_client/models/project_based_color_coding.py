from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_color import ProjectColor
else:
    ProjectColor = "ProjectColor"

from ..models.color_coding import ColorCoding

T = TypeVar("T", bound="ProjectBasedColorCoding")


@attr.s(auto_attribs=True)
class ProjectBasedColorCoding(ColorCoding):
    """Lets you set a color for a card based on its project."""

    project_colors: Union[Unset, List[ProjectColor]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_colors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.project_colors, Unset):
            project_colors = []
            for project_colors_item_data in self.project_colors:
                project_colors_item = project_colors_item_data.to_dict()

                project_colors.append(project_colors_item)

        field_dict: Dict[str, Any] = {}
        _ColorCoding_dict = super().to_dict()
        field_dict.update(_ColorCoding_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_colors is not UNSET:
            field_dict["projectColors"] = project_colors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _ColorCoding_kwargs = super().from_dict(src_dict=d).to_dict()

        project_colors = []
        _project_colors = d.pop("projectColors", UNSET)
        for project_colors_item_data in _project_colors or []:
            project_colors_item = ProjectColor.from_dict(project_colors_item_data)

            project_colors.append(project_colors_item)

        project_based_color_coding = cls(
            project_colors=project_colors,
            **_ColorCoding_kwargs,
        )

        project_based_color_coding.additional_properties = d
        return project_based_color_coding

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
