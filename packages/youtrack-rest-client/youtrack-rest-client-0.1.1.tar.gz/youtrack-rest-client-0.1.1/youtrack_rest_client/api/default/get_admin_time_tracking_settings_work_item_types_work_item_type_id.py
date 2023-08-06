from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.work_item_type import WorkItemType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    work_item_type_id: str,
    *,
    client: Client,
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Dict[str, Any]:
    url = "{}/admin/timeTrackingSettings/workItemTypes/{workItemTypeId}".format(
        client.youtrack_base_url, workItemTypeId=work_item_type_id
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


def _parse_response(*, response: httpx.Response) -> Optional[WorkItemType]:
    if response.status_code == 200:
        response_200 = WorkItemType.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[WorkItemType]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    work_item_type_id: str,
    *,
    client: Client,
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Response[WorkItemType]:
    kwargs = _get_kwargs(
        work_item_type_id=work_item_type_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    work_item_type_id: str,
    *,
    client: Client,
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Optional[WorkItemType]:
    """ """

    return sync_detailed(
        work_item_type_id=work_item_type_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    work_item_type_id: str,
    *,
    client: Client,
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Response[WorkItemType]:
    kwargs = _get_kwargs(
        work_item_type_id=work_item_type_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    work_item_type_id: str,
    *,
    client: Client,
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Optional[WorkItemType]:
    """ """

    return (
        await asyncio_detailed(
            work_item_type_id=work_item_type_id,
            client=client,
            fields=fields,
        )
    ).parsed
