from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupProjectCustomField")


try:
    from ..models import project_custom_field
except ImportError:
    import sys

    project_custom_field = sys.modules[__package__ + "project_custom_field"]


@attr.s(auto_attribs=True)
class GroupProjectCustomField(project_custom_field.ProjectCustomField):
    """Represents project settings for group custom field."""

    default_values: "Union[Unset, List[user_group_m.UserGroup]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        default_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.default_values, Unset):
            default_values = []
            for default_values_item_data in self.default_values:
                default_values_item = default_values_item_data.to_dict()

                default_values.append(default_values_item)

        field_dict: Dict[str, Any] = {}
        _ProjectCustomField_dict = super().to_dict()
        field_dict.update(_ProjectCustomField_dict)
        field_dict.update({})
        if default_values is not UNSET:
            field_dict["defaultValues"] = default_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            user_group_m = sys.modules[__package__ + "user_group"]

        d = src_dict.copy()

        default_values = []
        _default_values = d.pop("defaultValues", UNSET)
        for default_values_item_data in _default_values or []:
            default_values_item = user_group_m.UserGroup.from_dict(default_values_item_data)

            default_values.append(default_values_item)

        group_project_custom_field = cls(
            default_values=default_values,
        )

        return group_project_custom_field
