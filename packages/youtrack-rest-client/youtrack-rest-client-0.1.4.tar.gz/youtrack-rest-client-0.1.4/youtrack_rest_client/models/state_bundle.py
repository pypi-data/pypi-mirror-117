from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StateBundle")


try:
    from ..models import base_bundle
except ImportError:
    import sys

    base_bundle = sys.modules[__package__ + "base_bundle"]


@attr.s(auto_attribs=True)
class StateBundle(base_bundle.BaseBundle):
    """Represents a set of states in YouTrack."""

    values: "Union[Unset, List[state_bundle_element_m.StateBundleElement]]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()

                values.append(values_item)

        field_dict: Dict[str, Any] = {}
        _BaseBundle_dict = super().to_dict()
        field_dict.update(_BaseBundle_dict)
        field_dict.update({})
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import state_bundle_element as state_bundle_element_m
        except ImportError:
            import sys

            state_bundle_element_m = sys.modules[__package__ + "state_bundle_element"]

        d = src_dict.copy()

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = state_bundle_element_m.StateBundleElement.from_dict(values_item_data)

            values.append(values_item)

        state_bundle = cls(
            values=values,
        )

        return state_bundle
