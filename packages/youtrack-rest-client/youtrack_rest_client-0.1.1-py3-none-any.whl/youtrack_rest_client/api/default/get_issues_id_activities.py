from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.activity_item import ActivityItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/issues/{id}/activities".format(client.youtrack_base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "categories": categories,
        "reverse": reverse,
        "start": start,
        "end": end,
        "author": author,
        "fields": fields,
        "$skip": skip,
        "$top": top,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ActivityItem]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ActivityItem.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ActivityItem]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[List[ActivityItem]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        categories=categories,
        reverse=reverse,
        start=start,
        end=end,
        author=author,
        fields=fields,
        skip=skip,
        top=top,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Optional[List[ActivityItem]]:
    """ """

    return sync_detailed(
        id=id,
        client=client,
        categories=categories,
        reverse=reverse,
        start=start,
        end=end,
        author=author,
        fields=fields,
        skip=skip,
        top=top,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[List[ActivityItem]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        categories=categories,
        reverse=reverse,
        start=start,
        end=end,
        author=author,
        fields=fields,
        skip=skip,
        top=top,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Optional[List[ActivityItem]]:
    """ """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            categories=categories,
            reverse=reverse,
            start=start,
            end=end,
            author=author,
            fields=fields,
            skip=skip,
            top=top,
        )
    ).parsed
