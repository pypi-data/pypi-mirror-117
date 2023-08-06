from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocaleDescriptor")


@attr.s(auto_attribs=True)
class LocaleDescriptor:
    """Represents a language locale that is used in UI."""

    locale: "Union[Unset, str]" = UNSET
    language: "Union[Unset, str]" = UNSET
    community: "Union[Unset, bool]" = UNSET
    name: "Union[Unset, str]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        locale = self.locale
        language = self.language
        community = self.community
        name = self.name
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if locale is not UNSET:
            field_dict["locale"] = locale
        if language is not UNSET:
            field_dict["language"] = language
        if community is not UNSET:
            field_dict["community"] = community
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        locale = d.pop("locale", UNSET)

        language = d.pop("language", UNSET)

        community = d.pop("community", UNSET)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        locale_descriptor = cls(
            locale=locale,
            language=language,
            community=community,
            name=name,
            id=id,
            type=type,
        )

        return locale_descriptor
