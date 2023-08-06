# youtrack-rest-client `0.1.1`
A client library for accessing YouTrack REST API

⚠️This SDK generated using `2021.3` [OpenAPI](https://youtrack.jetbrains.com/api/openapi.json) version by custom [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) which is under development.
 It may have some bugs. Use with caution.⚠️

If you find a bug or want to request a new feature, please create an issue in [YouTrack](https://youtrack.jetbrains.com/newIssue?project=JT&c=State%20Open&c=Subsystem%20Python%20client%20library).

## Usage
First, create a client:

```python
from youtrack_rest_client import Client

client = Client(
    hub_base_url="https://hub.jetbrains.com/api/rest",
    youtrack_base_url="https://youtrack.jetbrains.com/api"
)
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from youtrack_rest_client import AuthenticatedClient

client = AuthenticatedClient(
    hub_base_url="https://hub.jetbrains.com/api/rest",
    youtrack_base_url="https://youtrack.jetbrains.com/api",
    token=os.getenv("YOUTRACK_TOKEN")
)
```

Now call your endpoint and use your models:

```python
from youtrack_rest_client.models import MyDataModel
from youtrack_rest_client.api.my_tag import get_my_data_model
from youtrack_rest_client.types import Response

my_data: MyDataModel = get_my_data_model.sync(client=client)
# or if you need more info (e.g. status_code)
response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from youtrack_rest_client.models import MyDataModel
from youtrack_rest_client.api.my_tag import get_my_data_model
from youtrack_rest_client.types import Response

my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but the async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` by async instead of blocking
1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `youtrack_rest_client.api.default`