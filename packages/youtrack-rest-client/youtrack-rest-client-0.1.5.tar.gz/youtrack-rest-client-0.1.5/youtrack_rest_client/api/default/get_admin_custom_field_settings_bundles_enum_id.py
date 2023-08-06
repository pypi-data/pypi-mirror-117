from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models import enum_bundle as enum_bundle_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,id",
) -> Dict[str, Any]:
    url = "{}/admin/customFieldSettings/bundles/enum/{id}".format(client.youtrack_base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[enum_bundle_m.EnumBundle]:
    if response.status_code == 200:
        response_200 = enum_bundle_m.EnumBundle.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[enum_bundle_m.EnumBundle]:
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
    fields: "Union[Unset, None, str]" = "$type,id",
) -> Response[enum_bundle_m.EnumBundle]:
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
    fields: "Union[Unset, None, str]" = "$type,id",
) -> Optional[enum_bundle_m.EnumBundle]:
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
    fields: "Union[Unset, None, str]" = "$type,id",
) -> Response[enum_bundle_m.EnumBundle]:
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
    fields: "Union[Unset, None, str]" = "$type,id",
) -> Optional[enum_bundle_m.EnumBundle]:
    """ """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            fields=fields,
        )
    ).parsed
