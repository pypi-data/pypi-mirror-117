from typing import Dict

import attr
from hub_rest_client import Client as HubClient


@attr.s(auto_attribs=True)
class Client(HubClient):
    """A class for keeping track of data related to the API"""

    youtrack_base_url: str = attr.ib("https://youtrack.jetbrains.com/api", kw_only=True)


@attr.s(auto_attribs=True)
class AuthenticatedClient(Client):
    """A Client which has been authenticated for use on secured endpoints"""

    token: str

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        return {"Authorization": f"Bearer {self.token}", **self.headers}
