from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.activity_cursor_page import ActivityCursorPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    issue_query: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,activities($type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter,hasBefore,id",
) -> Dict[str, Any]:
    url = "{}/activitiesPage".format(client.youtrack_base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "categories": categories,
        "reverse": reverse,
        "start": start,
        "end": end,
        "author": author,
        "issueQuery": issue_query,
        "cursor": cursor,
        "activityId": activity_id,
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


def _parse_response(*, response: httpx.Response) -> Optional[ActivityCursorPage]:
    if response.status_code == 200:
        response_200 = ActivityCursorPage.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActivityCursorPage]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    issue_query: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,activities($type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter,hasBefore,id",
) -> Response[ActivityCursorPage]:
    kwargs = _get_kwargs(
        client=client,
        categories=categories,
        reverse=reverse,
        start=start,
        end=end,
        author=author,
        issue_query=issue_query,
        cursor=cursor,
        activity_id=activity_id,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    issue_query: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,activities($type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter,hasBefore,id",
) -> Optional[ActivityCursorPage]:
    """ """

    return sync_detailed(
        client=client,
        categories=categories,
        reverse=reverse,
        start=start,
        end=end,
        author=author,
        issue_query=issue_query,
        cursor=cursor,
        activity_id=activity_id,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    issue_query: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,activities($type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter,hasBefore,id",
) -> Response[ActivityCursorPage]:
    kwargs = _get_kwargs(
        client=client,
        categories=categories,
        reverse=reverse,
        start=start,
        end=end,
        author=author,
        issue_query=issue_query,
        cursor=cursor,
        activity_id=activity_id,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    issue_query: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,activities($type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter,hasBefore,id",
) -> Optional[ActivityCursorPage]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            categories=categories,
            reverse=reverse,
            start=start,
            end=end,
            author=author,
            issue_query=issue_query,
            cursor=cursor,
            activity_id=activity_id,
            fields=fields,
        )
    ).parsed
