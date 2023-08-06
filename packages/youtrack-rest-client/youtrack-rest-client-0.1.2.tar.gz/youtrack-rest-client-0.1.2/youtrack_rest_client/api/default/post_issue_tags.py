from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models import issue_tag as issue_tag_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: issue_tag_m.IssueTag,
    fields: "Union[Unset, None, str]" = "$type,id,name,owner($type,id,login,name,ringId)",
) -> Dict[str, Any]:
    url = "{}/issueTags".format(client.youtrack_base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[issue_tag_m.IssueTag]:
    if response.status_code == 200:
        response_200 = issue_tag_m.IssueTag.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[issue_tag_m.IssueTag]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: issue_tag_m.IssueTag,
    fields: "Union[Unset, None, str]" = "$type,id,name,owner($type,id,login,name,ringId)",
) -> Response[issue_tag_m.IssueTag]:
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
    json_body: issue_tag_m.IssueTag,
    fields: "Union[Unset, None, str]" = "$type,id,name,owner($type,id,login,name,ringId)",
) -> Optional[issue_tag_m.IssueTag]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: issue_tag_m.IssueTag,
    fields: "Union[Unset, None, str]" = "$type,id,name,owner($type,id,login,name,ringId)",
) -> Response[issue_tag_m.IssueTag]:
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
    json_body: issue_tag_m.IssueTag,
    fields: "Union[Unset, None, str]" = "$type,id,name,owner($type,id,login,name,ringId)",
) -> Optional[issue_tag_m.IssueTag]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
