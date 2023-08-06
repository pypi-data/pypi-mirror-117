from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.issue_custom_field import IssueCustomField
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    issue_custom_field_id: str,
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)",
) -> Dict[str, Any]:
    url = "{}/issues/{id}/customFields/{issueCustomFieldId}".format(
        client.youtrack_base_url, id=id, issueCustomFieldId=issue_custom_field_id
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


def _parse_response(*, response: httpx.Response) -> Optional[IssueCustomField]:
    if response.status_code == 200:
        response_200 = IssueCustomField.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IssueCustomField]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    issue_custom_field_id: str,
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)",
) -> Response[IssueCustomField]:
    kwargs = _get_kwargs(
        id=id,
        issue_custom_field_id=issue_custom_field_id,
        client=client,
        fields=fields,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    issue_custom_field_id: str,
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)",
) -> Optional[IssueCustomField]:
    """ """

    return sync_detailed(
        id=id,
        issue_custom_field_id=issue_custom_field_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: str,
    issue_custom_field_id: str,
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)",
) -> Response[IssueCustomField]:
    kwargs = _get_kwargs(
        id=id,
        issue_custom_field_id=issue_custom_field_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    issue_custom_field_id: str,
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)",
) -> Optional[IssueCustomField]:
    """ """

    return (
        await asyncio_detailed(
            id=id,
            issue_custom_field_id=issue_custom_field_id,
            client=client,
            fields=fields,
        )
    ).parsed
