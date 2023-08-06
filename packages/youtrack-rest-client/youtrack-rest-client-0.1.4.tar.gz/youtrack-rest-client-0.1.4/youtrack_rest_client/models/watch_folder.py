from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WatchFolder")


try:
    from ..models import issue_folder
except ImportError:
    import sys

    issue_folder = sys.modules[__package__ + "issue_folder"]


@attr.s(auto_attribs=True)
class WatchFolder(issue_folder.IssueFolder):
    """A `WatchFolder` is an `IssueFolder` that let you enable notifications for a set
    of issues that it enfolds. It is a common abstract ancestor for saved searches and issue tags."""

    owner: "Union[Unset, user_m.User]" = UNSET
    visible_for: "Union[Unset, user_group_m.UserGroup]" = UNSET
    updateable_by: "Union[Unset, user_group_m.UserGroup]" = UNSET

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

        try:
            from ..models import user as user_m
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            user_m = sys.modules[__package__ + "user"]
            user_group_m = sys.modules[__package__ + "user_group"]

        d = src_dict.copy()

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, user_m.User]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = user_m.User.from_dict(_owner)

        _visible_for = d.pop("visibleFor", UNSET)
        visible_for: Union[Unset, user_group_m.UserGroup]
        if isinstance(_visible_for, Unset):
            visible_for = UNSET
        else:
            visible_for = user_group_m.UserGroup.from_dict(_visible_for)

        _updateable_by = d.pop("updateableBy", UNSET)
        updateable_by: Union[Unset, user_group_m.UserGroup]
        if isinstance(_updateable_by, Unset):
            updateable_by = UNSET
        else:
            updateable_by = user_group_m.UserGroup.from_dict(_updateable_by)

        watch_folder = cls(
            owner=owner,
            visible_for=visible_for,
            updateable_by=updateable_by,
        )

        return watch_folder
