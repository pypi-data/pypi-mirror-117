from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailSettings")


@attr.s(auto_attribs=True)
class EmailSettings:
    """Represents email settings for this YouTrack installation."""

    is_enabled: "Union[Unset, bool]" = UNSET
    host: "Union[Unset, str]" = UNSET
    port: "Union[Unset, int]" = UNSET
    mail_protocol: "Union[Unset, EmailSettingsMailProtocol]" = UNSET
    anonymous: "Union[Unset, bool]" = UNSET
    login: "Union[Unset, str]" = UNSET
    ssl_key: "Union[Unset, storage_entry_m.StorageEntry]" = UNSET
    from_: "Union[Unset, str]" = UNSET
    reply_to: "Union[Unset, str]" = UNSET
    id: "Union[Unset, str]" = UNSET
    type: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_enabled = self.is_enabled
        host = self.host
        port = self.port
        mail_protocol: Union[Unset, str] = UNSET
        if not isinstance(self.mail_protocol, Unset):
            mail_protocol = self.mail_protocol.value

        anonymous = self.anonymous
        login = self.login
        ssl_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ssl_key, Unset):
            ssl_key = self.ssl_key.to_dict()

        from_ = self.from_
        reply_to = self.reply_to
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if mail_protocol is not UNSET:
            field_dict["mailProtocol"] = mail_protocol
        if anonymous is not UNSET:
            field_dict["anonymous"] = anonymous
        if login is not UNSET:
            field_dict["login"] = login
        if ssl_key is not UNSET:
            field_dict["sslKey"] = ssl_key
        if from_ is not UNSET:
            field_dict["from"] = from_
        if reply_to is not UNSET:
            field_dict["replyTo"] = reply_to
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import storage_entry as storage_entry_m
            from ..models.email_settings_mail_protocol import EmailSettingsMailProtocol
        except ImportError:
            import sys

            storage_entry_m = sys.modules[__package__ + "storage_entry"]
            EmailSettingsMailProtocol = sys.modules[__package__ + "EmailSettingsMailProtoc"]

        d = src_dict.copy()

        is_enabled = d.pop("isEnabled", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        _mail_protocol = d.pop("mailProtocol", UNSET)
        mail_protocol: Union[Unset, EmailSettingsMailProtocol]
        if isinstance(_mail_protocol, Unset):
            mail_protocol = UNSET
        else:
            mail_protocol = EmailSettingsMailProtocol(_mail_protocol)

        anonymous = d.pop("anonymous", UNSET)

        login = d.pop("login", UNSET)

        _ssl_key = d.pop("sslKey", UNSET)
        ssl_key: Union[Unset, storage_entry_m.StorageEntry]
        if isinstance(_ssl_key, Unset):
            ssl_key = UNSET
        else:
            ssl_key = storage_entry_m.StorageEntry.from_dict(_ssl_key)

        from_ = d.pop("from", UNSET)

        reply_to = d.pop("replyTo", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        email_settings = cls(
            is_enabled=is_enabled,
            host=host,
            port=port,
            mail_protocol=mail_protocol,
            anonymous=anonymous,
            login=login,
            ssl_key=ssl_key,
            from_=from_,
            reply_to=reply_to,
            id=id,
            type=type,
        )

        return email_settings
