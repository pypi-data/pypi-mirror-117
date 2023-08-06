from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models import command_list as command_list_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,caret,commands($type,description,error,id),comment,id,issues($type,id,idReadable,numberInProject),query,suggestions($type,caret,completionEnd,completionStart,description,id,matchingEnd,matchingStart,option,prefix,suffix)",
) -> Dict[str, Any]:
    url = "{}/commands".format(client.youtrack_base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "muteUpdateNotifications": mute_update_notifications,
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


def _parse_response(*, response: httpx.Response) -> Optional[command_list_m.CommandList]:
    if response.status_code == 200:
        response_200 = command_list_m.CommandList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[command_list_m.CommandList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,caret,commands($type,description,error,id),comment,id,issues($type,id,idReadable,numberInProject),query,suggestions($type,caret,completionEnd,completionStart,description,id,matchingEnd,matchingStart,option,prefix,suffix)",
) -> Response[command_list_m.CommandList]:
    kwargs = _get_kwargs(
        client=client,
        mute_update_notifications=mute_update_notifications,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,caret,commands($type,description,error,id),comment,id,issues($type,id,idReadable,numberInProject),query,suggestions($type,caret,completionEnd,completionStart,description,id,matchingEnd,matchingStart,option,prefix,suffix)",
) -> Optional[command_list_m.CommandList]:
    """ """

    return sync_detailed(
        client=client,
        mute_update_notifications=mute_update_notifications,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,caret,commands($type,description,error,id),comment,id,issues($type,id,idReadable,numberInProject),query,suggestions($type,caret,completionEnd,completionStart,description,id,matchingEnd,matchingStart,option,prefix,suffix)",
) -> Response[command_list_m.CommandList]:
    kwargs = _get_kwargs(
        client=client,
        mute_update_notifications=mute_update_notifications,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,caret,commands($type,description,error,id),comment,id,issues($type,id,idReadable,numberInProject),query,suggestions($type,caret,completionEnd,completionStart,description,id,matchingEnd,matchingStart,option,prefix,suffix)",
) -> Optional[command_list_m.CommandList]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            mute_update_notifications=mute_update_notifications,
            fields=fields,
        )
    ).parsed
