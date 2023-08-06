from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemSettings")


@attr.s(auto_attribs=True)
class SystemSettings:
    """Represents the System settings that affect core functionality of YouTrack."""

    base_url: "Union[Unset, str]" = UNSET
    max_upload_file_size: "Union[Unset, int]" = UNSET
    max_export_items: "Union[Unset, int]" = UNSET
    administrator_email: "Union[Unset, str]" = UNSET
    allow_statistics_collection: "Union[Unset, bool]" = UNSET
    is_application_read_only: "Union[Unset, bool]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        base_url = self.base_url
        max_upload_file_size = self.max_upload_file_size
        max_export_items = self.max_export_items
        administrator_email = self.administrator_email
        allow_statistics_collection = self.allow_statistics_collection
        is_application_read_only = self.is_application_read_only
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if max_upload_file_size is not UNSET:
            field_dict["maxUploadFileSize"] = max_upload_file_size
        if max_export_items is not UNSET:
            field_dict["maxExportItems"] = max_export_items
        if administrator_email is not UNSET:
            field_dict["administratorEmail"] = administrator_email
        if allow_statistics_collection is not UNSET:
            field_dict["allowStatisticsCollection"] = allow_statistics_collection
        if is_application_read_only is not UNSET:
            field_dict["isApplicationReadOnly"] = is_application_read_only
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()

        base_url = d.pop("baseUrl", UNSET)

        max_upload_file_size = d.pop("maxUploadFileSize", UNSET)

        max_export_items = d.pop("maxExportItems", UNSET)

        administrator_email = d.pop("administratorEmail", UNSET)

        allow_statistics_collection = d.pop("allowStatisticsCollection", UNSET)

        is_application_read_only = d.pop("isApplicationReadOnly", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        system_settings = cls(
            base_url=base_url,
            max_upload_file_size=max_upload_file_size,
            max_export_items=max_export_items,
            administrator_email=administrator_email,
            allow_statistics_collection=allow_statistics_collection,
            is_application_read_only=is_application_read_only,
            id=id,
            type=type,
        )

        return system_settings
