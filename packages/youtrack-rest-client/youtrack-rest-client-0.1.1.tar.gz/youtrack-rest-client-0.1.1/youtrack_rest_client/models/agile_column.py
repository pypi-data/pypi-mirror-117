from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agile_column_field_value import AgileColumnFieldValue
    from ..models.column_settings import ColumnSettings
    from ..models.wip_limit import WIPLimit
else:
    WIPLimit = "WIPLimit"
    ColumnSettings = "ColumnSettings"
    AgileColumnFieldValue = "AgileColumnFieldValue"


T = TypeVar("T", bound="AgileColumn")


@attr.s(auto_attribs=True)
class AgileColumn:
    """Represents settings for a single board column"""

    presentation: Union[Unset, str] = UNSET
    is_resolved: Union[Unset, bool] = UNSET
    ordinal: Union[Unset, int] = UNSET
    parent: Union[Unset, ColumnSettings] = UNSET
    wip_limit: Union[Unset, WIPLimit] = UNSET
    field_values: Union[Unset, List[AgileColumnFieldValue]] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        presentation = self.presentation
        is_resolved = self.is_resolved
        ordinal = self.ordinal
        parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        wip_limit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wip_limit, Unset):
            wip_limit = self.wip_limit.to_dict()

        field_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.field_values, Unset):
            field_values = []
            for field_values_item_data in self.field_values:
                field_values_item = field_values_item_data.to_dict()

                field_values.append(field_values_item)

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if presentation is not UNSET:
            field_dict["presentation"] = presentation
        if is_resolved is not UNSET:
            field_dict["isResolved"] = is_resolved
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if parent is not UNSET:
            field_dict["parent"] = parent
        if wip_limit is not UNSET:
            field_dict["wipLimit"] = wip_limit
        if field_values is not UNSET:
            field_dict["fieldValues"] = field_values
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        presentation = d.pop("presentation", UNSET)

        is_resolved = d.pop("isResolved", UNSET)

        ordinal = d.pop("ordinal", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, ColumnSettings]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = ColumnSettings.from_dict(_parent)

        _wip_limit = d.pop("wipLimit", UNSET)
        wip_limit: Union[Unset, WIPLimit]
        if isinstance(_wip_limit, Unset):
            wip_limit = UNSET
        else:
            wip_limit = WIPLimit.from_dict(_wip_limit)

        field_values = []
        _field_values = d.pop("fieldValues", UNSET)
        for field_values_item_data in _field_values or []:
            field_values_item = AgileColumnFieldValue.from_dict(field_values_item_data)

            field_values.append(field_values_item)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        agile_column = cls(
            presentation=presentation,
            is_resolved=is_resolved,
            ordinal=ordinal,
            parent=parent,
            wip_limit=wip_limit,
            field_values=field_values,
            id=id,
            type=type,
        )

        agile_column.additional_properties = d
        return agile_column

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
