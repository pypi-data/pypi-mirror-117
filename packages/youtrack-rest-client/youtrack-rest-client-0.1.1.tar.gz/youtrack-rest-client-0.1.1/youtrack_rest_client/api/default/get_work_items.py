import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.issue_work_item import IssueWorkItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    query: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.date] = UNSET,
    end_date: Union[Unset, None, datetime.date] = UNSET,
    start: Union[Unset, None, int] = UNSET,
    end: Union[Unset, None, int] = UNSET,
    created_start: Union[Unset, None, int] = UNSET,
    created_end: Union[Unset, None, int] = UNSET,
    updated_start: Union[Unset, None, int] = UNSET,
    updated_end: Union[Unset, None, int] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    creator: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,author($type,id,login,name,ringId),created,creator($type,id,login,name,ringId),date,duration($type,id),id,text,updated,usesMarkdown",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workItems".format(client.youtrack_base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_start_date: Union[Unset, None, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat() if start_date else None

    json_end_date: Union[Unset, None, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat() if end_date else None

    params: Dict[str, Any] = {
        "query": query,
        "startDate": json_start_date,
        "endDate": json_end_date,
        "start": start,
        "end": end,
        "createdStart": created_start,
        "createdEnd": created_end,
        "updatedStart": updated_start,
        "updatedEnd": updated_end,
        "author": author,
        "creator": creator,
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


def _parse_response(*, response: httpx.Response) -> Optional[List[IssueWorkItem]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IssueWorkItem.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[IssueWorkItem]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    query: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.date] = UNSET,
    end_date: Union[Unset, None, datetime.date] = UNSET,
    start: Union[Unset, None, int] = UNSET,
    end: Union[Unset, None, int] = UNSET,
    created_start: Union[Unset, None, int] = UNSET,
    created_end: Union[Unset, None, int] = UNSET,
    updated_start: Union[Unset, None, int] = UNSET,
    updated_end: Union[Unset, None, int] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    creator: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,author($type,id,login,name,ringId),created,creator($type,id,login,name,ringId),date,duration($type,id),id,text,updated,usesMarkdown",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[List[IssueWorkItem]]:
    kwargs = _get_kwargs(
        client=client,
        query=query,
        start_date=start_date,
        end_date=end_date,
        start=start,
        end=end,
        created_start=created_start,
        created_end=created_end,
        updated_start=updated_start,
        updated_end=updated_end,
        author=author,
        creator=creator,
        fields=fields,
        skip=skip,
        top=top,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    query: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.date] = UNSET,
    end_date: Union[Unset, None, datetime.date] = UNSET,
    start: Union[Unset, None, int] = UNSET,
    end: Union[Unset, None, int] = UNSET,
    created_start: Union[Unset, None, int] = UNSET,
    created_end: Union[Unset, None, int] = UNSET,
    updated_start: Union[Unset, None, int] = UNSET,
    updated_end: Union[Unset, None, int] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    creator: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,author($type,id,login,name,ringId),created,creator($type,id,login,name,ringId),date,duration($type,id),id,text,updated,usesMarkdown",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Optional[List[IssueWorkItem]]:
    """ """

    return sync_detailed(
        client=client,
        query=query,
        start_date=start_date,
        end_date=end_date,
        start=start,
        end=end,
        created_start=created_start,
        created_end=created_end,
        updated_start=updated_start,
        updated_end=updated_end,
        author=author,
        creator=creator,
        fields=fields,
        skip=skip,
        top=top,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    query: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.date] = UNSET,
    end_date: Union[Unset, None, datetime.date] = UNSET,
    start: Union[Unset, None, int] = UNSET,
    end: Union[Unset, None, int] = UNSET,
    created_start: Union[Unset, None, int] = UNSET,
    created_end: Union[Unset, None, int] = UNSET,
    updated_start: Union[Unset, None, int] = UNSET,
    updated_end: Union[Unset, None, int] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    creator: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,author($type,id,login,name,ringId),created,creator($type,id,login,name,ringId),date,duration($type,id),id,text,updated,usesMarkdown",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[List[IssueWorkItem]]:
    kwargs = _get_kwargs(
        client=client,
        query=query,
        start_date=start_date,
        end_date=end_date,
        start=start,
        end=end,
        created_start=created_start,
        created_end=created_end,
        updated_start=updated_start,
        updated_end=updated_end,
        author=author,
        creator=creator,
        fields=fields,
        skip=skip,
        top=top,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    query: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.date] = UNSET,
    end_date: Union[Unset, None, datetime.date] = UNSET,
    start: Union[Unset, None, int] = UNSET,
    end: Union[Unset, None, int] = UNSET,
    created_start: Union[Unset, None, int] = UNSET,
    created_end: Union[Unset, None, int] = UNSET,
    updated_start: Union[Unset, None, int] = UNSET,
    updated_end: Union[Unset, None, int] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    creator: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,author($type,id,login,name,ringId),created,creator($type,id,login,name,ringId),date,duration($type,id),id,text,updated,usesMarkdown",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Optional[List[IssueWorkItem]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            start_date=start_date,
            end_date=end_date,
            start=start,
            end=end,
            created_start=created_start,
            created_end=created_end,
            updated_start=updated_start,
            updated_end=updated_end,
            author=author,
            creator=creator,
            fields=fields,
            skip=skip,
            top=top,
        )
    ).parsed
