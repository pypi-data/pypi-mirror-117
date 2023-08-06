from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="CustomFieldActivityItemRemoved")


@attr.s(auto_attribs=True)
class CustomFieldActivityItemRemoved:
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        custom_field_activity_item_removed = cls()

        return custom_field_activity_item_removed
