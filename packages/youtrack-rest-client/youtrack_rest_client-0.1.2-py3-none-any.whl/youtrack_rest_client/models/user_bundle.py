from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserBundle")


try:
    from ..models import bundle
except ImportError:
    import sys

    bundle = sys.modules[__package__ + "bundle"]


@attr.s(auto_attribs=True)
class UserBundle(bundle.Bundle):
    """Represents a set of values that contains users. You can add to the set both individual user accounts and groups of users."""

    groups: "Union[Unset, List[user_group_m.UserGroup]]" = UNSET
    individuals: "Union[Unset, List[user_m.User]]" = UNSET
    aggregated_users: "Union[Unset, List[user_m.User]]" = UNSET
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

        try:
            from ..models import user as user_m
            from ..models import user_group as user_group_m
        except ImportError:
            import sys

            user_m = sys.modules[__package__ + "user"]
            user_group_m = sys.modules[__package__ + "user_group"]

        d = src_dict.copy()

        _Bundle_kwargs = super().from_dict(src_dict=d).to_dict()

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = user_group_m.UserGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        individuals = []
        _individuals = d.pop("individuals", UNSET)
        for individuals_item_data in _individuals or []:
            individuals_item = user_m.User.from_dict(individuals_item_data)

            individuals.append(individuals_item)

        aggregated_users = []
        _aggregated_users = d.pop("aggregatedUsers", UNSET)
        for aggregated_users_item_data in _aggregated_users or []:
            aggregated_users_item = user_m.User.from_dict(aggregated_users_item_data)

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
