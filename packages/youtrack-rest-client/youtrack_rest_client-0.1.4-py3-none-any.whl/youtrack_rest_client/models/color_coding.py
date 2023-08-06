from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ColorCoding")


@attr.s(auto_attribs=True)
class ColorCoding:
    """Describes rules that define which colors are used for cards on the agile board."""

    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        color_coding = cls(
            id=id,
            type=type,
        )

        return color_coding
