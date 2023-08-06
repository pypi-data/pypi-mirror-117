from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.issue_comment import IssueComment
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: IssueComment,
    draft_id: Union[Unset, None, str] = UNSET,
    mute_update_notifications: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,attachments($type,id),author($type,id,login,name,ringId),created,deleted,id,text,updated,usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
) -> Dict[str, Any]:
    url = "{}/issues/{id}/comments".format(client.youtrack_base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "draftId": draft_id,
        "muteUpdateNotifications": mute_update_notifications,
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


def _parse_response(*, response: httpx.Response) -> Optional[IssueComment]:
    if response.status_code == 200:
        response_200 = IssueComment.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IssueComment]:
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
    json_body: IssueComment,
    draft_id: Union[Unset, None, str] = UNSET,
    mute_update_notifications: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,attachments($type,id),author($type,id,login,name,ringId),created,deleted,id,text,updated,usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
) -> Response[IssueComment]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        draft_id=draft_id,
        mute_update_notifications=mute_update_notifications,
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
    json_body: IssueComment,
    draft_id: Union[Unset, None, str] = UNSET,
    mute_update_notifications: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,attachments($type,id),author($type,id,login,name,ringId),created,deleted,id,text,updated,usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
) -> Optional[IssueComment]:
    """ """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        draft_id=draft_id,
        mute_update_notifications=mute_update_notifications,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: IssueComment,
    draft_id: Union[Unset, None, str] = UNSET,
    mute_update_notifications: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,attachments($type,id),author($type,id,login,name,ringId),created,deleted,id,text,updated,usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
) -> Response[IssueComment]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        draft_id=draft_id,
        mute_update_notifications=mute_update_notifications,
        fields=fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: IssueComment,
    draft_id: Union[Unset, None, str] = UNSET,
    mute_update_notifications: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,attachments($type,id),author($type,id,login,name,ringId),created,deleted,id,text,updated,usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
) -> Optional[IssueComment]:
    """ """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            draft_id=draft_id,
            mute_update_notifications=mute_update_notifications,
            fields=fields,
        )
    ).parsed
