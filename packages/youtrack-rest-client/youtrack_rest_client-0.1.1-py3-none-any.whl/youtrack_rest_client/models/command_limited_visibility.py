from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User
    from ..models.user_group import UserGroup
else:
    UserGroup = "UserGroup"
    User = "User"

from ..models.command_visibility import CommandVisibility

T = TypeVar("T", bound="CommandLimitedVisibility")


@attr.s(auto_attribs=True)
class CommandLimitedVisibility(CommandVisibility):
    """Stores the restricted visibility settings for the command."""

    permitted_groups: Union[Unset, List[UserGroup]] = UNSET
    permitted_users: Union[Unset, List[User]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permitted_groups is not UNSET:
            field_dict["permittedGroups"] = permitted_groups
        if permitted_users is not UNSET:
            field_dict["permittedUsers"] = permitted_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _CommandVisibility_kwargs = super().from_dict(src_dict=d).to_dict()

        permitted_groups = []
        _permitted_groups = d.pop("permittedGroups", UNSET)
        for permitted_groups_item_data in _permitted_groups or []:
            permitted_groups_item = UserGroup.from_dict(permitted_groups_item_data)

            permitted_groups.append(permitted_groups_item)

        permitted_users = []
        _permitted_users = d.pop("permittedUsers", UNSET)
        for permitted_users_item_data in _permitted_users or []:
            permitted_users_item = User.from_dict(permitted_users_item_data)

            permitted_users.append(permitted_users_item)

        command_limited_visibility = cls(
            permitted_groups=permitted_groups,
            permitted_users=permitted_users,
            **_CommandVisibility_kwargs,
        )

        command_limited_visibility.additional_properties = d
        return command_limited_visibility

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
