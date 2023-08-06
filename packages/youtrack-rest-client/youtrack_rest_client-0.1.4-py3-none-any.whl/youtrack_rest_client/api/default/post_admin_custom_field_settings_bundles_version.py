from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models import version_bundle as version_bundle_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: version_bundle_m.VersionBundle,
    fields: "Union[Unset, None, str]" = "$type,id",
) -> Dict[str, Any]:
    url = "{}/admin/customFieldSettings/bundles/version".format(client.youtrack_base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[version_bundle_m.VersionBundle]:
    if response.status_code == 200:
        response_200 = version_bundle_m.VersionBundle.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[version_bundle_m.VersionBundle]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: version_bundle_m.VersionBundle,
    fields: "Union[Unset, None, str]" = "$type,id",
) -> Response[version_bundle_m.VersionBundle]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        fields=fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: version_bundle_m.VersionBundle,
    fields: "Union[Unset, None, str]" = "$type,id",
) -> Optional[version_bundle_m.VersionBundle]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: version_bundle_m.VersionBundle,
    fields: "Union[Unset, None, str]" = "$type,id",
) -> Response[version_bundle_m.VersionBundle]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: version_bundle_m.VersionBundle,
    fields: "Union[Unset, None, str]" = "$type,id",
) -> Optional[version_bundle_m.VersionBundle]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
