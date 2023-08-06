from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OwnedBundleElement")


try:
    from ..models import bundle_element
except ImportError:
    import sys

    bundle_element = sys.modules[__package__ + "bundle_element"]


@attr.s(auto_attribs=True)
class OwnedBundleElement(bundle_element.BundleElement):
    """Represents a single owned value of a set. For example, a subsystem."""

    owner: "Union[Unset, user_m.User]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        field_dict: Dict[str, Any] = {}
        _BundleElement_dict = super().to_dict()
        field_dict.update(_BundleElement_dict)
        field_dict.update({})
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import user as user_m
        except ImportError:
            import sys

            user_m = sys.modules[__package__ + "user"]

        d = src_dict.copy()

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, user_m.User]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = user_m.User.from_dict(_owner)

        owned_bundle_element = cls(
            owner=owner,
        )

        return owned_bundle_element
