# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hub_rest_client',
 'hub_rest_client.api',
 'hub_rest_client.api.default',
 'hub_rest_client.models']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=20.1.0,<22.0.0',
 'httpx>=0.15.4,<0.19.0',
 'python-dateutil>=2.8.0,<3.0.0']

setup_kwargs = {
    'name': 'hub-rest-client',
    'version': '0.1.1',
    'description': 'A client library for accessing Hub REST API',
    'long_description': '# hub-rest-client `0.1.1`\nA client library for accessing Hub REST API\n\n⚠️This SDK generated using `2021.1.13439` [OpenAPI](https://hub.jetbrains.com/api/rest/openapi.json) version by custom [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) which is under development.\n It may have some bugs. Use with caution.⚠️\n\nIf you find a bug or want to request a new feature, please create an issue in [YouTrack](https://youtrack.jetbrains.com/newIssue?project=JT&c=State%20Open&c=Subsystem%20Python%20client%20library).\n\n## Usage\nFirst, create a client:\n\n```python\nfrom hub_rest_client import Client\n\nclient = Client(hub_base_url="https://hub.jetbrains.com/api/rest")\n```\n\nIf the endpoints you\'re going to hit require authentication, use `AuthenticatedClient` instead:\n\n```python\nimport os\n\nfrom hub_rest_client import AuthenticatedClient\n\n\nclient = AuthenticatedClient(hub_base_url="https://hub.jetbrains.com/api/rest", token=os.getenv("HUB_TOKEN"))\n```\n\nNow call your endpoint and use your models:\n\n```python\nfrom hub_rest_client.models import MyDataModel\nfrom hub_rest_client.api.my_tag import get_my_data_model\nfrom hub_rest_client.types import Response\n\nmy_data: MyDataModel = get_my_data_model.sync(client=client)\n# or if you need more info (e.g. status_code)\nresponse: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)\n```\n\nOr do the same thing with an async version:\n\n```python\nfrom hub_rest_client.models import MyDataModel\nfrom hub_rest_client.api.my_tag import get_my_data_model\nfrom hub_rest_client.types import Response\n\nmy_data: MyDataModel = await get_my_data_model.asyncio(client=client)\nresponse: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)\n```\n\nThings to know:\n1. Every path/method combo becomes a Python module with four functions:\n    1. `sync`: Blocking request that returns parsed data (if successful) or `None`\n    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.\n    1. `asyncio`: Like `sync` but the async instead of blocking\n    1. `asyncio_detailed`: Like `sync_detailed` by async instead of blocking\n1. All path/query params, and bodies become method arguments.\n1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)\n1. Any endpoint which did not have a tag will be in `hub_rest_client.api.default`',
    'author': 'Matvey Ovtsin',
    'author_email': 'matvey.ovtsin@jetbrains.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
