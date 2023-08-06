from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommandLimitedVisibility")


try:
    from ..models import command_visibility
except ImportError:
    import sys

    command_visibility = sys.modules[__package__ + "command_visibility"]


@attr.s(auto_attribs=True)
class CommandLimitedVisibility(command_visibility.CommandVisibility):
    """Stores the restricted visibility settings for the command."""

    permitted_groups: "Union[Unset, List[user_group_m.UserGroup]]" = UNSET
    permitted_users: "Union[Unset, List[user_m.User]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        permitted_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.permitted_groups, Unset):
            permitted_groups = []
            for permitted_groups_item_data in self.permitted_groups:
                permitted_groups_item = permitted_groups_item_data.to_dict()

                permitted_groups.append(permitted_groups_item)

        permitted_users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.permitted_users, Unset):
            permitted_users = []
            for permitted_users_item_data in self.permitted_users:
                permitted_users_item = permitted_users_item_data.to_dict()

                permitted_users.append(permitted_users_item)

        field_dict: Dict[str, Any] = {}
        _CommandVisibility_dict = super().to_dict()
        field_dict.update(_CommandVisibility_dict)
        field_dict.update({})
        if permitted_groups is not UNSET:
            field_dict["permittedGroups"] = permitted_groups
        if permitted_users is not UNSET:
            field_dict["permittedUsers"] = permitted_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import user as user_m
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            user_group_m = sys.modules[__package__ + "user_group"]
            user_m = sys.modules[__package__ + "user"]

        d = src_dict.copy()

        _CommandVisibility_kwargs = super().from_dict(src_dict=d).to_dict()
        _CommandVisibility_kwargs.pop("$type")

        permitted_groups = []
        _permitted_groups = d.pop("permittedGroups", UNSET)
        for permitted_groups_item_data in _permitted_groups or []:
            permitted_groups_item = user_group_m.UserGroup.from_dict(permitted_groups_item_data)

            permitted_groups.append(permitted_groups_item)

        permitted_users = []
        _permitted_users = d.pop("permittedUsers", UNSET)
        for permitted_users_item_data in _permitted_users or []:
            permitted_users_item = user_m.User.from_dict(permitted_users_item_data)

            permitted_users.append(permitted_users_item)

        command_limited_visibility = cls(
            permitted_groups=permitted_groups,
            permitted_users=permitted_users,
            **_CommandVisibility_kwargs,
        )

        return command_limited_visibility
