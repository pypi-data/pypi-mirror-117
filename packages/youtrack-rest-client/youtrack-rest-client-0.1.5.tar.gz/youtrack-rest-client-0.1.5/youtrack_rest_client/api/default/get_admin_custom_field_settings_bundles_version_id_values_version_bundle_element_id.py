from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models import version_bundle_element as version_bundle_element_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: "str",
    version_bundle_element_id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,archived,color($type,background,foreground,id),id,name,ordinal,releaseDate,released",
) -> Dict[str, Any]:
    url = "{}/admin/customFieldSettings/bundles/version/{id}/values/{versionBundleElementId}".format(
        client.youtrack_base_url, id=id, versionBundleElementId=version_bundle_element_id
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


def _parse_response(*, response: httpx.Response) -> Optional[version_bundle_element_m.VersionBundleElement]:
    if response.status_code == 200:
        response_200 = version_bundle_element_m.VersionBundleElement.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[version_bundle_element_m.VersionBundleElement]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: "str",
    version_bundle_element_id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,archived,color($type,background,foreground,id),id,name,ordinal,releaseDate,released",
) -> Response[version_bundle_element_m.VersionBundleElement]:
    kwargs = _get_kwargs(
        id=id,
        version_bundle_element_id=version_bundle_element_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: "str",
    version_bundle_element_id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,archived,color($type,background,foreground,id),id,name,ordinal,releaseDate,released",
) -> Optional[version_bundle_element_m.VersionBundleElement]:
    """ """

    return sync_detailed(
        id=id,
        version_bundle_element_id=version_bundle_element_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: "str",
    version_bundle_element_id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,archived,color($type,background,foreground,id),id,name,ordinal,releaseDate,released",
) -> Response[version_bundle_element_m.VersionBundleElement]:
    kwargs = _get_kwargs(
        id=id,
        version_bundle_element_id=version_bundle_element_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: "str",
    version_bundle_element_id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,archived,color($type,background,foreground,id),id,name,ordinal,releaseDate,released",
) -> Optional[version_bundle_element_m.VersionBundleElement]:
    """ """

    return (
        await asyncio_detailed(
            id=id,
            version_bundle_element_id=version_bundle_element_id,
            client=client,
            fields=fields,
        )
    ).parsed
