from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_field_value import TextFieldValue
else:
    TextFieldValue = "TextFieldValue"

from ..models.issue_custom_field import IssueCustomField

T = TypeVar("T", bound="TextIssueCustomField")


@attr.s(auto_attribs=True)
class TextIssueCustomField(IssueCustomField):
    """Represents the issue custom field of the `text` type."""

    value: Union[Unset, TextFieldValue] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        _IssueCustomField_dict = super().to_dict()
        field_dict.update(_IssueCustomField_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _IssueCustomField_kwargs = super().from_dict(src_dict=d).to_dict()

        _value = d.pop("value", UNSET)
        value: Union[Unset, TextFieldValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = TextFieldValue.from_dict(_value)

        text_issue_custom_field = cls(
            value=value,
            **_IssueCustomField_kwargs,
        )

        text_issue_custom_field.additional_properties = d
        return text_issue_custom_field

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
