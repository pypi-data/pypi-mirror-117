from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models import sprint as sprint_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: "str",
    *,
    client: Client,
    json_body: sprint_m.Sprint,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,archived,finish,id,isDefault,name,start",
) -> Dict[str, Any]:
    url = "{}/agiles/{id}/sprints".format(client.youtrack_base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "muteUpdateNotifications": mute_update_notifications,
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


def _parse_response(*, response: httpx.Response) -> Optional[sprint_m.Sprint]:
    if response.status_code == 200:
        response_200 = sprint_m.Sprint.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[sprint_m.Sprint]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: "str",
    *,
    client: Client,
    json_body: sprint_m.Sprint,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,archived,finish,id,isDefault,name,start",
) -> Response[sprint_m.Sprint]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        mute_update_notifications=mute_update_notifications,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: "str",
    *,
    client: Client,
    json_body: sprint_m.Sprint,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,archived,finish,id,isDefault,name,start",
) -> Optional[sprint_m.Sprint]:
    """ """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        mute_update_notifications=mute_update_notifications,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: "str",
    *,
    client: Client,
    json_body: sprint_m.Sprint,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,archived,finish,id,isDefault,name,start",
) -> Response[sprint_m.Sprint]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        mute_update_notifications=mute_update_notifications,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: "str",
    *,
    client: Client,
    json_body: sprint_m.Sprint,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,archived,finish,id,isDefault,name,start",
) -> Optional[sprint_m.Sprint]:
    """ """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            mute_update_notifications=mute_update_notifications,
            fields=fields,
        )
    ).parsed
