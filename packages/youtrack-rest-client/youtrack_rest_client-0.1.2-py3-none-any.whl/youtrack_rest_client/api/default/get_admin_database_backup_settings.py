from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models import database_backup_settings as database_backup_settings_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,availableDiskSpace,backupStatus($type,backupCancelled,backupError($type,date,errorMessage,id),backupInProgress,id),id,isOn,location",
) -> Dict[str, Any]:
    url = "{}/admin/databaseBackup/settings".format(client.youtrack_base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "fields": fields,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[database_backup_settings_m.DatabaseBackupSettings]:
    if response.status_code == 200:
        response_200 = database_backup_settings_m.DatabaseBackupSettings.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[database_backup_settings_m.DatabaseBackupSettings]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,availableDiskSpace,backupStatus($type,backupCancelled,backupError($type,date,errorMessage,id),backupInProgress,id),id,isOn,location",
) -> Response[database_backup_settings_m.DatabaseBackupSettings]:
    kwargs = _get_kwargs(
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,availableDiskSpace,backupStatus($type,backupCancelled,backupError($type,date,errorMessage,id),backupInProgress,id),id,isOn,location",
) -> Optional[database_backup_settings_m.DatabaseBackupSettings]:
    """ """

    return sync_detailed(
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,availableDiskSpace,backupStatus($type,backupCancelled,backupError($type,date,errorMessage,id),backupInProgress,id),id,isOn,location",
) -> Response[database_backup_settings_m.DatabaseBackupSettings]:
    kwargs = _get_kwargs(
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,availableDiskSpace,backupStatus($type,backupCancelled,backupError($type,date,errorMessage,id),backupInProgress,id),id,isOn,location",
) -> Optional[database_backup_settings_m.DatabaseBackupSettings]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
        )
    ).parsed
