from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkItemType")


@attr.s(auto_attribs=True)
class WorkItemType:
    """Represents a work type that can be assigned to a work item."""

    name: Union[Unset, str] = UNSET
    auto_attached: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        auto_attached = self.auto_attached
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if auto_attached is not UNSET:
            field_dict["autoAttached"] = auto_attached
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        name = d.pop("name", UNSET)

        auto_attached = d.pop("autoAttached", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        work_item_type = cls(
            name=name,
            auto_attached=auto_attached,
            id=id,
            type=type,
        )

        work_item_type.additional_properties = d
        return work_item_type

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
