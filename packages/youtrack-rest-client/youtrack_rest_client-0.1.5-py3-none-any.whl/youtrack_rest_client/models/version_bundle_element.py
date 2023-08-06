from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VersionBundleElement")


try:
    from ..models import bundle_element
except ImportError:
    import sys

    bundle_element = sys.modules[__package__ + "bundle_element"]


@attr.s(auto_attribs=True)
class VersionBundleElement(bundle_element.BundleElement):
    """Represents a version in YouTrack."""

    archived: "Union[Unset, bool]" = UNSET
    release_date: "Union[Unset, int]" = UNSET
    released: "Union[Unset, bool]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        archived = self.archived
        release_date = self.release_date
        released = self.released

        field_dict: Dict[str, Any] = {}
        _BundleElement_dict = super().to_dict()
        field_dict.update(_BundleElement_dict)
        field_dict.update({})
        if archived is not UNSET:
            field_dict["archived"] = archived
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if released is not UNSET:
            field_dict["released"] = released

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        _BundleElement_kwargs = super().from_dict(src_dict=d).to_dict()
        _BundleElement_kwargs.pop("$type")

        archived = d.pop("archived", UNSET)

        release_date = d.pop("releaseDate", UNSET)

        released = d.pop("released", UNSET)

        version_bundle_element = cls(
            archived=archived,
            release_date=release_date,
            released=released,
            **_BundleElement_kwargs,
        )

        return version_bundle_element
