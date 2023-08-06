from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectBasedColorCoding")


try:
    from ..models import color_coding
except ImportError:
    import sys

    color_coding = sys.modules[__package__ + "color_coding"]


@attr.s(auto_attribs=True)
class ProjectBasedColorCoding(color_coding.ColorCoding):
    """Lets you set a color for a card based on its project."""

    project_colors: "Union[Unset, List[project_color_m.ProjectColor]]" = UNSET

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
        field_dict.update({})
        if project_colors is not UNSET:
            field_dict["projectColors"] = project_colors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import project_color as project_color_m
        except ImportError:
            import sys

            project_color_m = sys.modules[__package__ + "project_color"]

        d = src_dict.copy()

        project_colors = []
        _project_colors = d.pop("projectColors", UNSET)
        for project_colors_item_data in _project_colors or []:
            project_colors_item = project_color_m.ProjectColor.from_dict(project_colors_item_data)

            project_colors.append(project_colors_item)

        project_based_color_coding = cls(
            project_colors=project_colors,
        )

        return project_based_color_coding
