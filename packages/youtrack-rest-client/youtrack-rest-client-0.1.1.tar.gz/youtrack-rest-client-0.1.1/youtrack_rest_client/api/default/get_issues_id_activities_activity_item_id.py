from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.activity_item import ActivityItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    activity_item_id: str,
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
) -> Dict[str, Any]:
    url = "{}/issues/{id}/activities/{activityItemId}".format(
        client.youtrack_base_url, id=id, activityItemId=activity_item_id
    )

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


def _parse_response(*, response: httpx.Response) -> Optional[ActivityItem]:
    if response.status_code == 200:
        response_200 = ActivityItem.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActivityItem]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    activity_item_id: str,
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
) -> Response[ActivityItem]:
    kwargs = _get_kwargs(
        id=id,
        activity_item_id=activity_item_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    activity_item_id: str,
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
) -> Optional[ActivityItem]:
    """ """

    return sync_detailed(
        id=id,
        activity_item_id=activity_item_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: str,
    activity_item_id: str,
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
) -> Response[ActivityItem]:
    kwargs = _get_kwargs(
        id=id,
        activity_item_id=activity_item_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    activity_item_id: str,
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
) -> Optional[ActivityItem]:
    """ """

    return (
        await asyncio_detailed(
            id=id,
            activity_item_id=activity_item_id,
            client=client,
            fields=fields,
        )
    ).parsed
