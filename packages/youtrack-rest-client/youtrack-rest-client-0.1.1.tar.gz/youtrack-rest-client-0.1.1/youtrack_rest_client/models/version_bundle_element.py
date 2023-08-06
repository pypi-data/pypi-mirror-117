from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.bundle_element import BundleElement
from ..types import UNSET, Unset

T = TypeVar("T", bound="VersionBundleElement")


@attr.s(auto_attribs=True)
class VersionBundleElement(BundleElement):
    """Represents a version in YouTrack."""

    archived: Union[Unset, bool] = UNSET
    release_date: Union[Unset, int] = UNSET
    released: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        archived = self.archived
        release_date = self.release_date
        released = self.released

        field_dict: Dict[str, Any] = {}
        _BundleElement_dict = super().to_dict()
        field_dict.update(_BundleElement_dict)
        field_dict.update(self.additional_properties)
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

        archived = d.pop("archived", UNSET)

        release_date = d.pop("releaseDate", UNSET)

        released = d.pop("released", UNSET)

        version_bundle_element = cls(
            archived=archived,
            release_date=release_date,
            released=released,
            **_BundleElement_kwargs,
        )

        version_bundle_element.additional_properties = d
        return version_bundle_element

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
