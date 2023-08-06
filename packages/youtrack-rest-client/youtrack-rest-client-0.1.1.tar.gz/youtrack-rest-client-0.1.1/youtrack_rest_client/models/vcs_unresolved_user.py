from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user import User
from ..types import UNSET, Unset

T = TypeVar("T", bound="VcsUnresolvedUser")


@attr.s(auto_attribs=True)
class VcsUnresolvedUser(User):
    """Represents an author of a VCS change that could not be found in the list of YouTrack users."""

    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        field_dict: Dict[str, Any] = {}
        _User_dict = super().to_dict()
        field_dict.update(_User_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _User_kwargs = super().from_dict(src_dict=d).to_dict()

        name = d.pop("name", UNSET)

        vcs_unresolved_user = cls(
            name=name,
            **_User_kwargs,
        )

        vcs_unresolved_user.additional_properties = d
        return vcs_unresolved_user

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
