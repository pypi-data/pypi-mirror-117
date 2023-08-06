from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="Me")


try:
    from ..models import user
except ImportError:
    import sys

    user = sys.modules[__package__ + "user"]


@attr.s(auto_attribs=True)
class Me(user.User):
    """Represents the currently logged in user in YouTrack."""

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        _User_dict = super().to_dict()
        field_dict.update(_User_dict)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _User_kwargs = super().from_dict(src_dict=d).to_dict()
        _User_kwargs.pop("$type")

        me = cls(
            **_User_kwargs,
        )

        return me
