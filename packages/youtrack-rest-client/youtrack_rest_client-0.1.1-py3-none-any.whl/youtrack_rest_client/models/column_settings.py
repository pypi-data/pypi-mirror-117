from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agile_column import AgileColumn
    from ..models.custom_field import CustomField
else:
    AgileColumn = "AgileColumn"
    CustomField = "CustomField"


T = TypeVar("T", bound="ColumnSettings")


@attr.s(auto_attribs=True)
class ColumnSettings:
    """Agile board columns settings."""

    field: Union[Unset, CustomField] = UNSET
    columns: Union[Unset, List[AgileColumn]] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.to_dict()

        columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()

                columns.append(columns_item)

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if columns is not UNSET:
            field_dict["columns"] = columns
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _field = d.pop("field", UNSET)
        field: Union[Unset, CustomField]
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = CustomField.from_dict(_field)

        columns = []
        _columns = d.pop("columns", UNSET)
        for columns_item_data in _columns or []:
            columns_item = AgileColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        column_settings = cls(
            field=field,
            columns=columns,
            id=id,
            type=type,
        )

        column_settings.additional_properties = d
        return column_settings

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
