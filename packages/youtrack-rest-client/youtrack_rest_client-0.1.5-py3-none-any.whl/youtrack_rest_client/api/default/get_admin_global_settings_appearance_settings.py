from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models import appearance_settings as appearance_settings_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Dict[str, Any]:
    url = "{}/admin/globalSettings/appearanceSettings".format(client.youtrack_base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[appearance_settings_m.AppearanceSettings]:
    if response.status_code == 200:
        response_200 = appearance_settings_m.AppearanceSettings.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[appearance_settings_m.AppearanceSettings]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Response[appearance_settings_m.AppearanceSettings]:
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
    fields: "Union[Unset, None, str]" = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Optional[appearance_settings_m.AppearanceSettings]:
    """ """

    return sync_detailed(
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Response[appearance_settings_m.AppearanceSettings]:
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
    fields: "Union[Unset, None, str]" = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Optional[appearance_settings_m.AppearanceSettings]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
        )
    ).parsed
