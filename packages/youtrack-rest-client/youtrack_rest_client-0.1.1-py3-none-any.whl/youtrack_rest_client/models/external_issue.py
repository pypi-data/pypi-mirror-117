from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalIssue")


@attr.s(auto_attribs=True)
class ExternalIssue:
    """For an issue that was imported from another service, represents the reference to the issue in the external system."""

    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        url = self.url
        key = self.key
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if key is not UNSET:
            field_dict["key"] = key
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        key = d.pop("key", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        external_issue = cls(
            name=name,
            url=url,
            key=key,
            id=id,
            type=type,
        )

        external_issue.additional_properties = d
        return external_issue

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
