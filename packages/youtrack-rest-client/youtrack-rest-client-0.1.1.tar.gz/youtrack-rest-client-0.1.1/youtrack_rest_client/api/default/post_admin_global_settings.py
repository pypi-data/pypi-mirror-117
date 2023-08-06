from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.global_settings import GlobalSettings
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: GlobalSettings,
    fields: Union[
        Unset, None, str
    ] = "$type,appearanceSettings($type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)),id,license($type,error,id,license,username),localeSettings($type,id,isRTL,locale($type,community,id,language,locale,name)),notificationSettings($type,emailSettings($type,id,isEnabled),id,jabberSettings($type,id,isEnabled)),restSettings($type,allowAllOrigins,allowedOrigins,id),systemSettings($type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize)",
) -> Dict[str, Any]:
    url = "{}/admin/globalSettings".format(client.youtrack_base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "fields": fields,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[GlobalSettings]:
    if response.status_code == 200:
        response_200 = GlobalSettings.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GlobalSettings]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: GlobalSettings,
    fields: Union[
        Unset, None, str
    ] = "$type,appearanceSettings($type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)),id,license($type,error,id,license,username),localeSettings($type,id,isRTL,locale($type,community,id,language,locale,name)),notificationSettings($type,emailSettings($type,id,isEnabled),id,jabberSettings($type,id,isEnabled)),restSettings($type,allowAllOrigins,allowedOrigins,id),systemSettings($type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize)",
) -> Response[GlobalSettings]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: GlobalSettings,
    fields: Union[
        Unset, None, str
    ] = "$type,appearanceSettings($type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)),id,license($type,error,id,license,username),localeSettings($type,id,isRTL,locale($type,community,id,language,locale,name)),notificationSettings($type,emailSettings($type,id,isEnabled),id,jabberSettings($type,id,isEnabled)),restSettings($type,allowAllOrigins,allowedOrigins,id),systemSettings($type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize)",
) -> Optional[GlobalSettings]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: GlobalSettings,
    fields: Union[
        Unset, None, str
    ] = "$type,appearanceSettings($type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)),id,license($type,error,id,license,username),localeSettings($type,id,isRTL,locale($type,community,id,language,locale,name)),notificationSettings($type,emailSettings($type,id,isEnabled),id,jabberSettings($type,id,isEnabled)),restSettings($type,allowAllOrigins,allowedOrigins,id),systemSettings($type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize)",
) -> Response[GlobalSettings]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: GlobalSettings,
    fields: Union[
        Unset, None, str
    ] = "$type,appearanceSettings($type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)),id,license($type,error,id,license,username),localeSettings($type,id,isRTL,locale($type,community,id,language,locale,name)),notificationSettings($type,emailSettings($type,id,isEnabled),id,jabberSettings($type,id,isEnabled)),restSettings($type,allowAllOrigins,allowedOrigins,id),systemSettings($type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize)",
) -> Optional[GlobalSettings]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
