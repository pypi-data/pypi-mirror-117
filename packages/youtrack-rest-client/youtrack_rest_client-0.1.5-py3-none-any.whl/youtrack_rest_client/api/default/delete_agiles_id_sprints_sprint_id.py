from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    id: "str",
    sprint_id: "str",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/agiles/{id}/sprints/{sprintId}".format(client.youtrack_base_url, id=id, sprintId=sprint_id)

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
    id: "str",
    sprint_id: "str",
    *,
    client: Client,
) -> Response[Any]:
    kwargs = _get_kwargs(
        id=id,
        sprint_id=sprint_id,
        client=client,
    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    id: "str",
    sprint_id: "str",
    *,
    client: Client,
) -> Response[Any]:
    kwargs = _get_kwargs(
        id=id,
        sprint_id=sprint_id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)
