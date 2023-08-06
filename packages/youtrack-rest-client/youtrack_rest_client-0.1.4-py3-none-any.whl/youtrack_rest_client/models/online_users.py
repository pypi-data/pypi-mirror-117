from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnlineUsers")


@attr.s(auto_attribs=True)
class OnlineUsers:
    """Stores number of online user."""

    users: "Union[Unset, int]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        users = self.users
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        users = d.pop("users", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        online_users = cls(
            users=users,
            id=id,
            type=type,
        )

        return online_users
