from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project import Project
else:
    Project = "Project"


T = TypeVar("T", bound="UserGroup")


@attr.s(auto_attribs=True)
class UserGroup:
    """Represents a group of users."""

    name: Union[Unset, str] = UNSET
    ring_id: Union[Unset, str] = UNSET
    users_count: Union[Unset, int] = UNSET
    icon: Union[Unset, str] = UNSET
    all_users_group: Union[Unset, bool] = UNSET
    team_for_project: Union[Unset, Project] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        ring_id = self.ring_id
        users_count = self.users_count
        icon = self.icon
        all_users_group = self.all_users_group
        team_for_project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team_for_project, Unset):
            team_for_project = self.team_for_project.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if ring_id is not UNSET:
            field_dict["ringId"] = ring_id
        if users_count is not UNSET:
            field_dict["usersCount"] = users_count
        if icon is not UNSET:
            field_dict["icon"] = icon
        if all_users_group is not UNSET:
            field_dict["allUsersGroup"] = all_users_group
        if team_for_project is not UNSET:
            field_dict["teamForProject"] = team_for_project
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        name = d.pop("name", UNSET)

        ring_id = d.pop("ringId", UNSET)

        users_count = d.pop("usersCount", UNSET)

        icon = d.pop("icon", UNSET)

        all_users_group = d.pop("allUsersGroup", UNSET)

        _team_for_project = d.pop("teamForProject", UNSET)
        team_for_project: Union[Unset, Project]
        if isinstance(_team_for_project, Unset):
            team_for_project = UNSET
        else:
            team_for_project = Project.from_dict(_team_for_project)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        user_group = cls(
            name=name,
            ring_id=ring_id,
            users_count=users_count,
            icon=icon,
            all_users_group=all_users_group,
            team_for_project=team_for_project,
            id=id,
            type=type,
        )

        user_group.additional_properties = d
        return user_group

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
