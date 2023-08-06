from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field import CustomField
    from ..models.sprint import Sprint
else:
    Sprint = "Sprint"
    CustomField = "CustomField"


T = TypeVar("T", bound="SprintsSettings")


@attr.s(auto_attribs=True)
class SprintsSettings:
    """Describes sprints configuration."""

    is_explicit: Union[Unset, bool] = UNSET
    card_on_several_sprints: Union[Unset, bool] = UNSET
    default_sprint: Union[Unset, Sprint] = UNSET
    disable_sprints: Union[Unset, bool] = UNSET
    explicit_query: Union[Unset, str] = UNSET
    sprint_sync_field: Union[Unset, CustomField] = UNSET
    hide_subtasks_of_cards: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_explicit = self.is_explicit
        card_on_several_sprints = self.card_on_several_sprints
        default_sprint: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_sprint, Unset):
            default_sprint = self.default_sprint.to_dict()

        disable_sprints = self.disable_sprints
        explicit_query = self.explicit_query
        sprint_sync_field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sprint_sync_field, Unset):
            sprint_sync_field = self.sprint_sync_field.to_dict()

        hide_subtasks_of_cards = self.hide_subtasks_of_cards
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_explicit is not UNSET:
            field_dict["isExplicit"] = is_explicit
        if card_on_several_sprints is not UNSET:
            field_dict["cardOnSeveralSprints"] = card_on_several_sprints
        if default_sprint is not UNSET:
            field_dict["defaultSprint"] = default_sprint
        if disable_sprints is not UNSET:
            field_dict["disableSprints"] = disable_sprints
        if explicit_query is not UNSET:
            field_dict["explicitQuery"] = explicit_query
        if sprint_sync_field is not UNSET:
            field_dict["sprintSyncField"] = sprint_sync_field
        if hide_subtasks_of_cards is not UNSET:
            field_dict["hideSubtasksOfCards"] = hide_subtasks_of_cards
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        is_explicit = d.pop("isExplicit", UNSET)

        card_on_several_sprints = d.pop("cardOnSeveralSprints", UNSET)

        _default_sprint = d.pop("defaultSprint", UNSET)
        default_sprint: Union[Unset, Sprint]
        if isinstance(_default_sprint, Unset):
            default_sprint = UNSET
        else:
            default_sprint = Sprint.from_dict(_default_sprint)

        disable_sprints = d.pop("disableSprints", UNSET)

        explicit_query = d.pop("explicitQuery", UNSET)

        _sprint_sync_field = d.pop("sprintSyncField", UNSET)
        sprint_sync_field: Union[Unset, CustomField]
        if isinstance(_sprint_sync_field, Unset):
            sprint_sync_field = UNSET
        else:
            sprint_sync_field = CustomField.from_dict(_sprint_sync_field)

        hide_subtasks_of_cards = d.pop("hideSubtasksOfCards", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        sprints_settings = cls(
            is_explicit=is_explicit,
            card_on_several_sprints=card_on_several_sprints,
            default_sprint=default_sprint,
            disable_sprints=disable_sprints,
            explicit_query=explicit_query,
            sprint_sync_field=sprint_sync_field,
            hide_subtasks_of_cards=hide_subtasks_of_cards,
            id=id,
            type=type,
        )

        sprints_settings.additional_properties = d
        return sprints_settings

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
