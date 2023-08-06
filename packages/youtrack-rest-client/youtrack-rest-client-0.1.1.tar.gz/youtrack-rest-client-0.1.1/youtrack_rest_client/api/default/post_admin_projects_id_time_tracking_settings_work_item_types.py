from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.work_item_type import WorkItemType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: WorkItemType,
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Dict[str, Any]:
    url = "{}/admin/projects/{id}/timeTrackingSettings/workItemTypes".format(client.youtrack_base_url, id=id)

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
    id: str,
    *,
    client: Client,
    json_body: WorkItemType,
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Response[WorkItemType]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: WorkItemType,
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Optional[WorkItemType]:
    """ """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: WorkItemType,
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Response[WorkItemType]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: WorkItemType,
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Optional[WorkItemType]:
    """ """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
