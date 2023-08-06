from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models import issue as issue_m
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: "str",
    issue_link_id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,created,customFields($type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,name,ringId),resolved,summary,updated,updater($type,id,login,name,ringId),usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
    skip: "Union[Unset, None, int]" = UNSET,
    top: "Union[Unset, None, int]" = UNSET,
) -> Dict[str, Any]:
    url = "{}/issues/{id}/links/{issueLinkId}/issues".format(client.youtrack_base_url, id=id, issueLinkId=issue_link_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[List[issue_m.Issue]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = issue_m.Issue.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[issue_m.Issue]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: "str",
    issue_link_id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,created,customFields($type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,name,ringId),resolved,summary,updated,updater($type,id,login,name,ringId),usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
    skip: "Union[Unset, None, int]" = UNSET,
    top: "Union[Unset, None, int]" = UNSET,
) -> Response[List[issue_m.Issue]]:
    kwargs = _get_kwargs(
        id=id,
        issue_link_id=issue_link_id,
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
    id: "str",
    issue_link_id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,created,customFields($type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,name,ringId),resolved,summary,updated,updater($type,id,login,name,ringId),usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
    skip: "Union[Unset, None, int]" = UNSET,
    top: "Union[Unset, None, int]" = UNSET,
) -> Optional[List[issue_m.Issue]]:
    """ """

    return sync_detailed(
        id=id,
        issue_link_id=issue_link_id,
        client=client,
        fields=fields,
        skip=skip,
        top=top,
    ).parsed


async def asyncio_detailed(
    id: "str",
    issue_link_id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,created,customFields($type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,name,ringId),resolved,summary,updated,updater($type,id,login,name,ringId),usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
    skip: "Union[Unset, None, int]" = UNSET,
    top: "Union[Unset, None, int]" = UNSET,
) -> Response[List[issue_m.Issue]]:
    kwargs = _get_kwargs(
        id=id,
        issue_link_id=issue_link_id,
        client=client,
        fields=fields,
        skip=skip,
        top=top,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: "str",
    issue_link_id: "str",
    *,
    client: Client,
    fields: "Union[Unset, None, str]" = "$type,created,customFields($type,id,name,projectCustomField($type,field($type,fieldType($type,id),id,localizedName,name),id),value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,name,ringId),resolved,summary,updated,updater($type,id,login,name,ringId),usesMarkdown,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,name,ringId))",
    skip: "Union[Unset, None, int]" = UNSET,
    top: "Union[Unset, None, int]" = UNSET,
) -> Optional[List[issue_m.Issue]]:
    """ """

    return (
        await asyncio_detailed(
            id=id,
            issue_link_id=issue_link_id,
            client=client,
            fields=fields,
            skip=skip,
            top=top,
        )
    ).parsed
