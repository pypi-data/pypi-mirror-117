from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_tag import IssueTag
    from ..models.saved_query import SavedQuery
    from ..models.user_profiles import UserProfiles
else:
    IssueTag = "IssueTag"
    UserProfiles = "UserProfiles"
    SavedQuery = "SavedQuery"


T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """Represents a user in YouTrack. Please note that the read-only properties of a user account, like
    credentials, or email and so on, you can only change in
    <a href="https://www.jetbrains.com/help/youtrack/devportal/?Hub-REST-API">Hub REST API</a>."""

    login: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    jabber_account_name: Union[Unset, str] = UNSET
    ring_id: Union[Unset, str] = UNSET
    guest: Union[Unset, bool] = UNSET
    online: Union[Unset, bool] = UNSET
    banned: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[IssueTag]] = UNSET
    saved_queries: Union[Unset, List[SavedQuery]] = UNSET
    avatar_url: Union[Unset, str] = UNSET
    profiles: Union[Unset, UserProfiles] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login = self.login
        full_name = self.full_name
        email = self.email
        jabber_account_name = self.jabber_account_name
        ring_id = self.ring_id
        guest = self.guest
        online = self.online
        banned = self.banned
        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        saved_queries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.saved_queries, Unset):
            saved_queries = []
            for saved_queries_item_data in self.saved_queries:
                saved_queries_item = saved_queries_item_data.to_dict()

                saved_queries.append(saved_queries_item)

        avatar_url = self.avatar_url
        profiles: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profiles, Unset):
            profiles = self.profiles.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if login is not UNSET:
            field_dict["login"] = login
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if email is not UNSET:
            field_dict["email"] = email
        if jabber_account_name is not UNSET:
            field_dict["jabberAccountName"] = jabber_account_name
        if ring_id is not UNSET:
            field_dict["ringId"] = ring_id
        if guest is not UNSET:
            field_dict["guest"] = guest
        if online is not UNSET:
            field_dict["online"] = online
        if banned is not UNSET:
            field_dict["banned"] = banned
        if tags is not UNSET:
            field_dict["tags"] = tags
        if saved_queries is not UNSET:
            field_dict["savedQueries"] = saved_queries
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if profiles is not UNSET:
            field_dict["profiles"] = profiles
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        login = d.pop("login", UNSET)

        full_name = d.pop("fullName", UNSET)

        email = d.pop("email", UNSET)

        jabber_account_name = d.pop("jabberAccountName", UNSET)

        ring_id = d.pop("ringId", UNSET)

        guest = d.pop("guest", UNSET)

        online = d.pop("online", UNSET)

        banned = d.pop("banned", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = IssueTag.from_dict(tags_item_data)

            tags.append(tags_item)

        saved_queries = []
        _saved_queries = d.pop("savedQueries", UNSET)
        for saved_queries_item_data in _saved_queries or []:
            saved_queries_item = SavedQuery.from_dict(saved_queries_item_data)

            saved_queries.append(saved_queries_item)

        avatar_url = d.pop("avatarUrl", UNSET)

        _profiles = d.pop("profiles", UNSET)
        profiles: Union[Unset, UserProfiles]
        if isinstance(_profiles, Unset):
            profiles = UNSET
        else:
            profiles = UserProfiles.from_dict(_profiles)

        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        user = cls(
            login=login,
            full_name=full_name,
            email=email,
            jabber_account_name=jabber_account_name,
            ring_id=ring_id,
            guest=guest,
            online=online,
            banned=banned,
            tags=tags,
            saved_queries=saved_queries,
            avatar_url=avatar_url,
            profiles=profiles,
            id=id,
            type=type,
        )

        user.additional_properties = d
        return user

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
