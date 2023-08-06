from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models import issue as issue_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: issue_m.Issue,
    draft_id: "Union[Unset, None, str]" = UNSET,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,created,customFields($type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,name,ringId),resolved,summary,updated,updater($type,id,login,name,ringId),usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
) -> Dict[str, Any]:
    url = "{}/issues".format(client.youtrack_base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[issue_m.Issue]:
    if response.status_code == 200:
        response_200 = issue_m.Issue.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[issue_m.Issue]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: issue_m.Issue,
    draft_id: "Union[Unset, None, str]" = UNSET,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,created,customFields($type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,name,ringId),resolved,summary,updated,updater($type,id,login,name,ringId),usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
) -> Response[issue_m.Issue]:
    kwargs = _get_kwargs(
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
    *,
    client: Client,
    json_body: issue_m.Issue,
    draft_id: "Union[Unset, None, str]" = UNSET,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,created,customFields($type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,name,ringId),resolved,summary,updated,updater($type,id,login,name,ringId),usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
) -> Optional[issue_m.Issue]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
        draft_id=draft_id,
        mute_update_notifications=mute_update_notifications,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: issue_m.Issue,
    draft_id: "Union[Unset, None, str]" = UNSET,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,created,customFields($type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,name,ringId),resolved,summary,updated,updater($type,id,login,name,ringId),usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
) -> Response[issue_m.Issue]:
    kwargs = _get_kwargs(
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
    *,
    client: Client,
    json_body: issue_m.Issue,
    draft_id: "Union[Unset, None, str]" = UNSET,
    mute_update_notifications: "Union[Unset, None, bool]" = UNSET,
    fields: "Union[Unset, None, str]" = "$type,created,customFields($type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,name,ringId),resolved,summary,updated,updater($type,id,login,name,ringId),usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
) -> Optional[issue_m.Issue]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            draft_id=draft_id,
            mute_update_notifications=mute_update_notifications,
            fields=fields,
        )
    ).parsed
