from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.owned_bundle_element import OwnedBundleElement
else:
    OwnedBundleElement = "OwnedBundleElement"

from ..models.database_multi_value_issue_custom_field import DatabaseMultiValueIssueCustomField

T = TypeVar("T", bound="MultiOwnedIssueCustomField")


@attr.s(auto_attribs=True)
class MultiOwnedIssueCustomField(DatabaseMultiValueIssueCustomField):
    """Represents the issue custom field of the `ownedField` type that can have multiple values. The predefined Subsystem field is the example of the owned fields."""

    value: Union[Unset, OwnedBundleElement] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        _DatabaseMultiValueIssueCustomField_dict = super().to_dict()
        field_dict.update(_DatabaseMultiValueIssueCustomField_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _DatabaseMultiValueIssueCustomField_kwargs = super().from_dict(src_dict=d).to_dict()

        _value = d.pop("value", UNSET)
        value: Union[Unset, OwnedBundleElement]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = OwnedBundleElement.from_dict(_value)

        multi_owned_issue_custom_field = cls(
            value=value,
            **_DatabaseMultiValueIssueCustomField_kwargs,
        )

        multi_owned_issue_custom_field.additional_properties = d
        return multi_owned_issue_custom_field

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
