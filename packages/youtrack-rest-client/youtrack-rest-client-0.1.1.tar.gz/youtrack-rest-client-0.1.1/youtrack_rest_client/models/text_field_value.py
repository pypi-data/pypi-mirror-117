from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextFieldValue")


@attr.s(auto_attribs=True)
class TextFieldValue:
    """Represents a value of the text field. Returns both source and rendered text."""

    text: Union[Unset, str] = UNSET
    markdown_text: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        markdown_text = self.markdown_text
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if markdown_text is not UNSET:
            field_dict["markdownText"] = markdown_text
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        text = d.pop("text", UNSET)

        markdown_text = d.pop("markdownText", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        text_field_value = cls(
            text=text,
            markdown_text=markdown_text,
            id=id,
            type=type,
        )

        text_field_value.additional_properties = d
        return text_field_value

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
