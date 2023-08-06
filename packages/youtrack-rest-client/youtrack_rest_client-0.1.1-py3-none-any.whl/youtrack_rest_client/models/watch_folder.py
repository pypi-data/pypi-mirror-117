from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User
    from ..models.user_group import UserGroup
else:
    UserGroup = "UserGroup"
    User = "User"

from ..models.issue_folder import IssueFolder

T = TypeVar("T", bound="WatchFolder")


@attr.s(auto_attribs=True)
class WatchFolder(IssueFolder):
    """A `WatchFolder` is an `IssueFolder` that let you enable notifications for a set
    of issues that it enfolds. It is a common abstract ancestor for saved searches and issue tags."""

    owner: Union[Unset, User] = UNSET
    visible_for: Union[Unset, UserGroup] = UNSET
    updateable_by: Union[Unset, UserGroup] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        visible_for: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.visible_for, Unset):
            visible_for = self.visible_for.to_dict()

        updateable_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updateable_by, Unset):
            updateable_by = self.updateable_by.to_dict()

        field_dict: Dict[str, Any] = {}
        _IssueFolder_dict = super().to_dict()
        field_dict.update(_IssueFolder_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if owner is not UNSET:
            field_dict["owner"] = owner
        if visible_for is not UNSET:
            field_dict["visibleFor"] = visible_for
        if updateable_by is not UNSET:
            field_dict["updateableBy"] = updateable_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _IssueFolder_kwargs = super().from_dict(src_dict=d).to_dict()

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, User]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = User.from_dict(_owner)

        _visible_for = d.pop("visibleFor", UNSET)
        visible_for: Union[Unset, UserGroup]
        if isinstance(_visible_for, Unset):
            visible_for = UNSET
        else:
            visible_for = UserGroup.from_dict(_visible_for)

        _updateable_by = d.pop("updateableBy", UNSET)
        updateable_by: Union[Unset, UserGroup]
        if isinstance(_updateable_by, Unset):
            updateable_by = UNSET
        else:
            updateable_by = UserGroup.from_dict(_updateable_by)

        watch_folder = cls(
            owner=owner,
            visible_for=visible_for,
            updateable_by=updateable_by,
            **_IssueFolder_kwargs,
        )

        watch_folder.additional_properties = d
        return watch_folder

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
