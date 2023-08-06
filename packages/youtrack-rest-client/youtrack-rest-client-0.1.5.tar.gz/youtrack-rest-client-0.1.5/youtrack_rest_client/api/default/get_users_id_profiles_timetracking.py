from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models import time_tracking_user_profile as time_tracking_user_profile_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,id,periodFormat($type,id)",
) -> Dict[str, Any]:
    url = "{}/users/{id}/profiles/timetracking".format(client.youtrack_base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[time_tracking_user_profile_m.TimeTrackingUserProfile]:
    if response.status_code == 200:
        response_200 = time_tracking_user_profile_m.TimeTrackingUserProfile.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[time_tracking_user_profile_m.TimeTrackingUserProfile]:
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
    fields: "Union[Unset, None, str]" = "$type,id,periodFormat($type,id)",
) -> Response[time_tracking_user_profile_m.TimeTrackingUserProfile]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,id,periodFormat($type,id)",
) -> Optional[time_tracking_user_profile_m.TimeTrackingUserProfile]:
    """ """

    return sync_detailed(
        id=id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,id,periodFormat($type,id)",
) -> Response[time_tracking_user_profile_m.TimeTrackingUserProfile]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,id,periodFormat($type,id)",
) -> Optional[time_tracking_user_profile_m.TimeTrackingUserProfile]:
    """ """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            fields=fields,
        )
    ).parsed
