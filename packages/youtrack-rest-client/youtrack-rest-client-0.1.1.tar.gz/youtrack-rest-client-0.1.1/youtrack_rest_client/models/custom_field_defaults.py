from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field import CustomField
else:
    CustomField = "CustomField"


T = TypeVar("T", bound="CustomFieldDefaults")


@attr.s(auto_attribs=True)
class CustomFieldDefaults:
    """Represents default project-related settings of the custom field. These settings are applied at the moment when the custom field is attached to a project. After that, any changes in default settings do not affect the field settings for this project."""

    can_be_empty: Union[Unset, bool] = UNSET
    empty_field_text: Union[Unset, str] = UNSET
    is_public: Union[Unset, bool] = UNSET
    parent: Union[Unset, CustomField] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        can_be_empty = self.can_be_empty
        empty_field_text = self.empty_field_text
        is_public = self.is_public
        parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_be_empty is not UNSET:
            field_dict["canBeEmpty"] = can_be_empty
        if empty_field_text is not UNSET:
            field_dict["emptyFieldText"] = empty_field_text
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if parent is not UNSET:
            field_dict["parent"] = parent
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        can_be_empty = d.pop("canBeEmpty", UNSET)

        empty_field_text = d.pop("emptyFieldText", UNSET)

        is_public = d.pop("isPublic", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, CustomField]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = CustomField.from_dict(_parent)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        custom_field_defaults = cls(
            can_be_empty=can_be_empty,
            empty_field_text=empty_field_text,
            is_public=is_public,
            parent=parent,
            id=id,
            type=type,
        )

        custom_field_defaults.additional_properties = d
        return custom_field_defaults

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
