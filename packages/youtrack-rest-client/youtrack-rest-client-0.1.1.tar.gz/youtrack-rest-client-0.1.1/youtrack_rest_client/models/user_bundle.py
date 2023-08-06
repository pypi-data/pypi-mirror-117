from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User
    from ..models.user_group import UserGroup
else:
    UserGroup = "UserGroup"
    User = "User"

from ..models.bundle import Bundle

T = TypeVar("T", bound="UserBundle")


@attr.s(auto_attribs=True)
class UserBundle(Bundle):
    """Represents a set of values that contains users. You can add to the set both individual user accounts and groups of users."""

    groups: Union[Unset, List[UserGroup]] = UNSET
    individuals: Union[Unset, List[User]] = UNSET
    aggregated_users: Union[Unset, List[User]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()

                groups.append(groups_item)

        individuals: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.individuals, Unset):
            individuals = []
            for individuals_item_data in self.individuals:
                individuals_item = individuals_item_data.to_dict()

                individuals.append(individuals_item)

        aggregated_users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aggregated_users, Unset):
            aggregated_users = []
            for aggregated_users_item_data in self.aggregated_users:
                aggregated_users_item = aggregated_users_item_data.to_dict()

                aggregated_users.append(aggregated_users_item)

        field_dict: Dict[str, Any] = {}
        _Bundle_dict = super().to_dict()
        field_dict.update(_Bundle_dict)
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups
        if individuals is not UNSET:
            field_dict["individuals"] = individuals
        if aggregated_users is not UNSET:
            field_dict["aggregatedUsers"] = aggregated_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        _Bundle_kwargs = super().from_dict(src_dict=d).to_dict()

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = UserGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        individuals = []
        _individuals = d.pop("individuals", UNSET)
        for individuals_item_data in _individuals or []:
            individuals_item = User.from_dict(individuals_item_data)

            individuals.append(individuals_item)

        aggregated_users = []
        _aggregated_users = d.pop("aggregatedUsers", UNSET)
        for aggregated_users_item_data in _aggregated_users or []:
            aggregated_users_item = User.from_dict(aggregated_users_item_data)

            aggregated_users.append(aggregated_users_item)

        user_bundle = cls(
            groups=groups,
            individuals=individuals,
            aggregated_users=aggregated_users,
            **_Bundle_kwargs,
        )

        user_bundle.additional_properties = d
        return user_bundle

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
