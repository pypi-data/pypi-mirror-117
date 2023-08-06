from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    id: str,
    version_bundle_element_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/admin/customFieldSettings/bundles/version/{id}/values/{versionBundleElementId}".format(
        client.youtrack_base_url, id=id, versionBundleElementId=version_bundle_element_id
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    id: str,
    version_bundle_element_id: str,
    *,
    client: Client,
) -> Response[Any]:
    kwargs = _get_kwargs(
        id=id,
        version_bundle_element_id=version_bundle_element_id,
        client=client,
    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    id: str,
    version_bundle_element_id: str,
    *,
    client: Client,
) -> Response[Any]:
    kwargs = _get_kwargs(
        id=id,
        version_bundle_element_id=version_bundle_element_id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)
