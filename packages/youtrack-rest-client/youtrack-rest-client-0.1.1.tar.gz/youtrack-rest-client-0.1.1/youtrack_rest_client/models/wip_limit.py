from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agile_column import AgileColumn
else:
    AgileColumn = "AgileColumn"


T = TypeVar("T", bound="WIPLimit")


@attr.s(auto_attribs=True)
class WIPLimit:
    """Represents WIP limits for particular column. If they are not satisfied, the column will be highlighted in UI."""

    max_: Union[Unset, int] = UNSET
    min_: Union[Unset, int] = UNSET
    column: Union[Unset, AgileColumn] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_ = self.max_
        min_ = self.min_
        column: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.column, Unset):
            column = self.column.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if column is not UNSET:
            field_dict["column"] = column
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        _column = d.pop("column", UNSET)
        column: Union[Unset, AgileColumn]
        if isinstance(_column, Unset):
            column = UNSET
        else:
            column = AgileColumn.from_dict(_column)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        wip_limit = cls(
            max_=max_,
            min_=min_,
            column=column,
            id=id,
            type=type,
        )

        wip_limit.additional_properties = d
        return wip_limit

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
