from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models import agile as agile_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,columnSettings($type,columns($type,id),field($type,fieldType($type,id),id,localizedName,name),id),id,name,owner($type,id,login,name,ringId),projects($type,id,name,shortName),status($type,id,valid),swimlaneSettings($type,enabled,field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,values($type,id,name))",
    skip: "Union[Unset, None, int]" = UNSET,
    top: "Union[Unset, None, int]" = UNSET,
) -> Dict[str, Any]:
    url = "{}/agiles".format(client.youtrack_base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
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


def _parse_response(*, response: httpx.Response) -> Optional[List[agile_m.Agile]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = agile_m.Agile.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[agile_m.Agile]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,columnSettings($type,columns($type,id),field($type,fieldType($type,id),id,localizedName,name),id),id,name,owner($type,id,login,name,ringId),projects($type,id,name,shortName),status($type,id,valid),swimlaneSettings($type,enabled,field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,values($type,id,name))",
    skip: "Union[Unset, None, int]" = UNSET,
    top: "Union[Unset, None, int]" = UNSET,
) -> Response[List[agile_m.Agile]]:
    kwargs = _get_kwargs(
        client=client,
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
    fields: "Union[Unset, None, str]" = "$type,columnSettings($type,columns($type,id),field($type,fieldType($type,id),id,localizedName,name),id),id,name,owner($type,id,login,name,ringId),projects($type,id,name,shortName),status($type,id,valid),swimlaneSettings($type,enabled,field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,values($type,id,name))",
    skip: "Union[Unset, None, int]" = UNSET,
    top: "Union[Unset, None, int]" = UNSET,
) -> Optional[List[agile_m.Agile]]:
    """ """

    return sync_detailed(
        client=client,
        fields=fields,
        skip=skip,
        top=top,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,columnSettings($type,columns($type,id),field($type,fieldType($type,id),id,localizedName,name),id),id,name,owner($type,id,login,name,ringId),projects($type,id,name,shortName),status($type,id,valid),swimlaneSettings($type,enabled,field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,values($type,id,name))",
    skip: "Union[Unset, None, int]" = UNSET,
    top: "Union[Unset, None, int]" = UNSET,
) -> Response[List[agile_m.Agile]]:
    kwargs = _get_kwargs(
        client=client,
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
    fields: "Union[Unset, None, str]" = "$type,columnSettings($type,columns($type,id),field($type,fieldType($type,id),id,localizedName,name),id),id,name,owner($type,id,login,name,ringId),projects($type,id,name,shortName),status($type,id,valid),swimlaneSettings($type,enabled,field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,values($type,id,name))",
    skip: "Union[Unset, None, int]" = UNSET,
    top: "Union[Unset, None, int]" = UNSET,
) -> Optional[List[agile_m.Agile]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
            skip=skip,
            top=top,
        )
    ).parsed
