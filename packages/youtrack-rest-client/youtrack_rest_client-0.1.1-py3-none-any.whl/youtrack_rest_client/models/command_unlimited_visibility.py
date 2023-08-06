from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.command_visibility import CommandVisibility

T = TypeVar("T", bound="CommandUnlimitedVisibility")


@attr.s(auto_attribs=True)
class CommandUnlimitedVisibility(CommandVisibility):
    """Comment is visible for all the users who can read the issue."""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _CommandVisibility_dict = super().to_dict()
        field_dict.update(_CommandVisibility_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _CommandVisibility_kwargs = super().from_dict(src_dict=d).to_dict()

        command_unlimited_visibility = cls(
            **_CommandVisibility_kwargs,
        )

        command_unlimited_visibility.additional_properties = d
        return command_unlimited_visibility

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
