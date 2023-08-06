from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="CommandUnlimitedVisibility")


try:
    from ..models import command_visibility
except ImportError:
    import sys

    command_visibility = sys.modules[__package__ + "command_visibility"]


@attr.s(auto_attribs=True)
class CommandUnlimitedVisibility(command_visibility.CommandVisibility):
    """Comment is visible for all the users who can read the issue."""

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _CommandVisibility_dict = super().to_dict()
        field_dict.update(_CommandVisibility_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        src_dict.copy()

        command_unlimited_visibility = cls()

        return command_unlimited_visibility
