from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bundle import Bundle
    from ..models.field_style import FieldStyle
else:
    Bundle = "Bundle"
    FieldStyle = "FieldStyle"


T = TypeVar("T", bound="BundleElement")


@attr.s(auto_attribs=True)
class BundleElement:
    """Represents a field value in YouTrack."""

    name: Union[Unset, str] = UNSET
    bundle: Union[Unset, Bundle] = UNSET
    description: Union[Unset, str] = UNSET
    ordinal: Union[Unset, int] = UNSET
    color: Union[Unset, FieldStyle] = UNSET
    has_running_job: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        bundle: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bundle, Unset):
            bundle = self.bundle.to_dict()

        description = self.description
        ordinal = self.ordinal
        color: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()

        has_running_job = self.has_running_job
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if bundle is not UNSET:
            field_dict["bundle"] = bundle
        if description is not UNSET:
            field_dict["description"] = description
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if color is not UNSET:
            field_dict["color"] = color
        if has_running_job is not UNSET:
            field_dict["hasRunningJob"] = has_running_job
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        name = d.pop("name", UNSET)

        _bundle = d.pop("bundle", UNSET)
        bundle: Union[Unset, Bundle]
        if isinstance(_bundle, Unset):
            bundle = UNSET
        else:
            bundle = Bundle.from_dict(_bundle)

        description = d.pop("description", UNSET)

        ordinal = d.pop("ordinal", UNSET)

        _color = d.pop("color", UNSET)
        color: Union[Unset, FieldStyle]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = FieldStyle.from_dict(_color)

        has_running_job = d.pop("hasRunningJob", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        bundle_element = cls(
            name=name,
            bundle=bundle,
            description=description,
            ordinal=ordinal,
            color=color,
            has_running_job=has_running_job,
            id=id,
            type=type,
        )

        bundle_element.additional_properties = d
        return bundle_element

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
