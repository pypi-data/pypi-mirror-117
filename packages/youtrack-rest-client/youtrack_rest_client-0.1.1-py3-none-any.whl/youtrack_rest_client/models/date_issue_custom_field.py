from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_issue_custom_field_value import DateIssueCustomFieldValue
else:
    DateIssueCustomFieldValue = "DateIssueCustomFieldValue"

from ..models.simple_issue_custom_field import SimpleIssueCustomField

T = TypeVar("T", bound="DateIssueCustomField")


@attr.s(auto_attribs=True)
class DateIssueCustomField(SimpleIssueCustomField):
    """Represents the issue custom field of the `date` type."""

    value: Union[Unset, DateIssueCustomFieldValue] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        _SimpleIssueCustomField_dict = super().to_dict()
        field_dict.update(_SimpleIssueCustomField_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _SimpleIssueCustomField_kwargs = super().from_dict(src_dict=d).to_dict()

        _value = d.pop("value", UNSET)
        value: Union[Unset, DateIssueCustomFieldValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = DateIssueCustomFieldValue.from_dict(_value)

        date_issue_custom_field = cls(
            value=value,
            **_SimpleIssueCustomField_kwargs,
        )

        date_issue_custom_field.additional_properties = d
        return date_issue_custom_field

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
