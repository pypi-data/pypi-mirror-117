from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VcsChangeActivityItem")


try:
    from ..models import created_deleted_activity_item
except ImportError:
    import sys

    created_deleted_activity_item = sys.modules[__package__ + "created_deleted_activity_item"]


@attr.s(auto_attribs=True)
class VcsChangeActivityItem(created_deleted_activity_item.CreatedDeletedActivityItem):
    """Represents an update in the list of VCSChanges of an issue."""

    removed: "Union[Unset, vcs_change_activity_item_removed_m.VcsChangeActivityItemRemoved]" = UNSET
    added: "Union[Unset, vcs_change_activity_item_added_m.VcsChangeActivityItemAdded]" = UNSET
    author: "Union[Unset, user_m.User]" = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        removed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.removed, Unset):
            removed = self.removed.to_dict()

        added: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.to_dict()

        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        field_dict: Dict[str, Any] = {}
        _CreatedDeletedActivityItem_dict = super().to_dict()
        field_dict.update(_CreatedDeletedActivityItem_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if removed is not UNSET:
            field_dict["removed"] = removed
        if added is not UNSET:
            field_dict["added"] = added
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import user as user_m
            from ..models import vcs_change_activity_item_added as vcs_change_activity_item_added_m
            from ..models import vcs_change_activity_item_removed as vcs_change_activity_item_removed_m
        except ImportError:
            import sys

            user_m = sys.modules[__package__ + "user"]
            vcs_change_activity_item_added_m = sys.modules[__package__ + "vcs_change_activity_item_added"]
            vcs_change_activity_item_removed_m = sys.modules[__package__ + "vcs_change_activity_item_removed"]

        d = src_dict.copy()

        _removed = d.pop("removed", UNSET)
        removed: Union[Unset, vcs_change_activity_item_removed_m.VcsChangeActivityItemRemoved]
        if isinstance(_removed, Unset):
            removed = UNSET
        else:
            removed = vcs_change_activity_item_removed_m.VcsChangeActivityItemRemoved.from_dict(_removed)

        _added = d.pop("added", UNSET)
        added: Union[Unset, vcs_change_activity_item_added_m.VcsChangeActivityItemAdded]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = vcs_change_activity_item_added_m.VcsChangeActivityItemAdded.from_dict(_added)

        _author = d.pop("author", UNSET)
        author: Union[Unset, user_m.User]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = user_m.User.from_dict(_author)

        vcs_change_activity_item = cls(
            removed=removed,
            added=added,
            author=author,
        )

        vcs_change_activity_item.additional_properties = d
        return vcs_change_activity_item

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
