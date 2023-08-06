from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Suggestion")


@attr.s(auto_attribs=True)
class Suggestion:
    """Represents query suggestion."""

    completion_start: Union[Unset, int] = UNSET
    completion_end: Union[Unset, int] = UNSET
    matching_start: Union[Unset, int] = UNSET
    matching_end: Union[Unset, int] = UNSET
    caret: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    option: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    suffix: Union[Unset, str] = UNSET
    group: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    auxiliary_icon: Union[Unset, str] = UNSET
    class_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completion_start = self.completion_start
        completion_end = self.completion_end
        matching_start = self.matching_start
        matching_end = self.matching_end
        caret = self.caret
        description = self.description
        option = self.option
        prefix = self.prefix
        suffix = self.suffix
        group = self.group
        icon = self.icon
        auxiliary_icon = self.auxiliary_icon
        class_name = self.class_name
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completion_start is not UNSET:
            field_dict["completionStart"] = completion_start
        if completion_end is not UNSET:
            field_dict["completionEnd"] = completion_end
        if matching_start is not UNSET:
            field_dict["matchingStart"] = matching_start
        if matching_end is not UNSET:
            field_dict["matchingEnd"] = matching_end
        if caret is not UNSET:
            field_dict["caret"] = caret
        if description is not UNSET:
            field_dict["description"] = description
        if option is not UNSET:
            field_dict["option"] = option
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if group is not UNSET:
            field_dict["group"] = group
        if icon is not UNSET:
            field_dict["icon"] = icon
        if auxiliary_icon is not UNSET:
            field_dict["auxiliaryIcon"] = auxiliary_icon
        if class_name is not UNSET:
            field_dict["className"] = class_name
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        completion_start = d.pop("completionStart", UNSET)

        completion_end = d.pop("completionEnd", UNSET)

        matching_start = d.pop("matchingStart", UNSET)

        matching_end = d.pop("matchingEnd", UNSET)

        caret = d.pop("caret", UNSET)

        description = d.pop("description", UNSET)

        option = d.pop("option", UNSET)

        prefix = d.pop("prefix", UNSET)

        suffix = d.pop("suffix", UNSET)

        group = d.pop("group", UNSET)

        icon = d.pop("icon", UNSET)

        auxiliary_icon = d.pop("auxiliaryIcon", UNSET)

        class_name = d.pop("className", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        suggestion = cls(
            completion_start=completion_start,
            completion_end=completion_end,
            matching_start=matching_start,
            matching_end=matching_end,
            caret=caret,
            description=description,
            option=option,
            prefix=prefix,
            suffix=suffix,
            group=group,
            icon=icon,
            auxiliary_icon=auxiliary_icon,
            class_name=class_name,
            id=id,
            type=type,
        )

        suggestion.additional_properties = d
        return suggestion

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
